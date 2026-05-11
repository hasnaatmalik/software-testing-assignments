"""
Migration Context Manager
Manages shared state between agents during multi-file migration.

The context accumulates migrated file results so that later agents
(Migration Agent for file B) can see what happened to earlier files
(file A). This enables cross-file awareness.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import copy


class MigrationContext:
    """
    Shared context for multi-agent migration pipeline.
    
    Tracks:
    - Original file contents
    - Migrated file results
    - Dependency graph
    - Validation results
    - Repair history
    """
    
    def __init__(
        self,
        repo_id: str,
        source_version: str = "2.x",
        target_version: str = "5.1",
        dependency_graph: Optional[Dict] = None
    ):
        self.repo_id = repo_id
        self.source_version = source_version
        self.target_version = target_version
        self.dependency_graph = dependency_graph or {}
        
        # File tracking
        self.original_files: Dict[str, str] = {}       # path -> original content
        self.migrated_files: Dict[str, str] = {}        # path -> migrated content
        self.file_types: Dict[str, str] = {}            # path -> django file type
        self.execution_logs: List[str] = []
        
        # Migration results per file
        self.migration_results: Dict[str, Dict] = {}    # path -> full result dict
        
        # Validation results per file
        self.validation_results: Dict[str, Dict] = {}   # path -> validation report
        
        # Repair history: path -> [list of repair attempts]
        self.repair_history: Dict[str, List[Dict]] = {} # path -> list of repair dicts
        
        # Pipeline state
        self.pipeline_status = "initialized"
        self.current_batch = 0
        self.started_at = datetime.utcnow()
        self.completed_at = None
        
        # Statistics
        self.stats = {
            "total_files": 0,
            "migrated_count": 0,
            "validated_count": 0,
            "passed_count": 0,
            "failed_count": 0,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def add_log(self, msg: str):
        import sys
        print(msg, file=sys.stderr)
        self.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] {msg}")
    
    def add_original_file(self, file_path: str, content: str, file_type: str = "unknown"):
        """Register an original file before migration."""
        self.original_files[file_path] = content
        self.file_types[file_path] = file_type
        self.stats["total_files"] = len(self.original_files)
    
    def add_migration_result(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def add_validation_result(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def add_repair_attempt(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def get_repair_count(self, file_path: str) -> int:
        """Get number of repair attempts for a file."""
        return len(self.repair_history.get(file_path, []))
    
    def get_related_files(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", []):
                source = dep_info.get("source", "")
                target = dep_info.get("target", "")
                
                if source == file_path and target in self.migrated_files:
                    related[target] = self.migrated_files[target]
                elif target == file_path and source in self.migrated_files:
                    related[source] = self.migrated_files[source]
        
        # Also check files_by_type for same-app relationships
        file_parts = file_path.replace("\\", "/").split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def get_context_for_migration(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "stats": copy.deepcopy(self.stats),
            "files_migrated": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "stats": self.stats,
            "migration_results": {
                path: {
                    "success": r.get("success"),
                    "changes_made": r.get("changes_made", []),
                    "file_type": r.get("file_type"),
                }
                for path, r in self.migration_results.items()
            },
            "validation_results": self.validation_results,
            "repair_history": {
                path: [
                    {"success": a.get("success"), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
