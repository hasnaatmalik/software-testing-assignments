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
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


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
        args = [repo_id, source_version, target_version, dependency_graph]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁ__init____mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁ__init____mutmut_orig(
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
    
    def xǁMigrationContextǁ__init____mutmut_1(
        self,
        repo_id: str,
        source_version: str = "XX2.xXX",
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
    
    def xǁMigrationContextǁ__init____mutmut_2(
        self,
        repo_id: str,
        source_version: str = "2.X",
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
    
    def xǁMigrationContextǁ__init____mutmut_3(
        self,
        repo_id: str,
        source_version: str = "2.x",
        target_version: str = "XX5.1XX",
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
    
    def xǁMigrationContextǁ__init____mutmut_4(
        self,
        repo_id: str,
        source_version: str = "2.x",
        target_version: str = "5.1",
        dependency_graph: Optional[Dict] = None
    ):
        self.repo_id = None
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
    
    def xǁMigrationContextǁ__init____mutmut_5(
        self,
        repo_id: str,
        source_version: str = "2.x",
        target_version: str = "5.1",
        dependency_graph: Optional[Dict] = None
    ):
        self.repo_id = repo_id
        self.source_version = None
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
    
    def xǁMigrationContextǁ__init____mutmut_6(
        self,
        repo_id: str,
        source_version: str = "2.x",
        target_version: str = "5.1",
        dependency_graph: Optional[Dict] = None
    ):
        self.repo_id = repo_id
        self.source_version = source_version
        self.target_version = None
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
    
    def xǁMigrationContextǁ__init____mutmut_7(
        self,
        repo_id: str,
        source_version: str = "2.x",
        target_version: str = "5.1",
        dependency_graph: Optional[Dict] = None
    ):
        self.repo_id = repo_id
        self.source_version = source_version
        self.target_version = target_version
        self.dependency_graph = None
        
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
    
    def xǁMigrationContextǁ__init____mutmut_8(
        self,
        repo_id: str,
        source_version: str = "2.x",
        target_version: str = "5.1",
        dependency_graph: Optional[Dict] = None
    ):
        self.repo_id = repo_id
        self.source_version = source_version
        self.target_version = target_version
        self.dependency_graph = dependency_graph and {}
        
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
    
    def xǁMigrationContextǁ__init____mutmut_9(
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
        self.original_files: Dict[str, str] = None       # path -> original content
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
    
    def xǁMigrationContextǁ__init____mutmut_10(
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
        self.migrated_files: Dict[str, str] = None        # path -> migrated content
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
    
    def xǁMigrationContextǁ__init____mutmut_11(
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
        self.file_types: Dict[str, str] = None            # path -> django file type
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
    
    def xǁMigrationContextǁ__init____mutmut_12(
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
        self.execution_logs: List[str] = None
        
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
    
    def xǁMigrationContextǁ__init____mutmut_13(
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
        self.migration_results: Dict[str, Dict] = None    # path -> full result dict
        
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
    
    def xǁMigrationContextǁ__init____mutmut_14(
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
        self.validation_results: Dict[str, Dict] = None   # path -> validation report
        
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
    
    def xǁMigrationContextǁ__init____mutmut_15(
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
        self.repair_history: Dict[str, List[Dict]] = None # path -> list of repair dicts
        
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
    
    def xǁMigrationContextǁ__init____mutmut_16(
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
        self.pipeline_status = None
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
    
    def xǁMigrationContextǁ__init____mutmut_17(
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
        self.pipeline_status = "XXinitializedXX"
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
    
    def xǁMigrationContextǁ__init____mutmut_18(
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
        self.pipeline_status = "INITIALIZED"
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
    
    def xǁMigrationContextǁ__init____mutmut_19(
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
        self.current_batch = None
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
    
    def xǁMigrationContextǁ__init____mutmut_20(
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
        self.current_batch = 1
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
    
    def xǁMigrationContextǁ__init____mutmut_21(
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
        self.started_at = None
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
    
    def xǁMigrationContextǁ__init____mutmut_22(
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
        self.completed_at = ""
        
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
    
    def xǁMigrationContextǁ__init____mutmut_23(
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
        self.stats = None
    
    def xǁMigrationContextǁ__init____mutmut_24(
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
            "XXtotal_filesXX": 0,
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
    
    def xǁMigrationContextǁ__init____mutmut_25(
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
            "TOTAL_FILES": 0,
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
    
    def xǁMigrationContextǁ__init____mutmut_26(
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
            "total_files": 1,
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
    
    def xǁMigrationContextǁ__init____mutmut_27(
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
            "XXmigrated_countXX": 0,
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
    
    def xǁMigrationContextǁ__init____mutmut_28(
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
            "MIGRATED_COUNT": 0,
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
    
    def xǁMigrationContextǁ__init____mutmut_29(
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
            "migrated_count": 1,
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
    
    def xǁMigrationContextǁ__init____mutmut_30(
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
            "XXvalidated_countXX": 0,
            "passed_count": 0,
            "failed_count": 0,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_31(
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
            "VALIDATED_COUNT": 0,
            "passed_count": 0,
            "failed_count": 0,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_32(
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
            "validated_count": 1,
            "passed_count": 0,
            "failed_count": 0,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_33(
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
            "XXpassed_countXX": 0,
            "failed_count": 0,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_34(
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
            "PASSED_COUNT": 0,
            "failed_count": 0,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_35(
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
            "passed_count": 1,
            "failed_count": 0,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_36(
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
            "XXfailed_countXX": 0,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_37(
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
            "FAILED_COUNT": 0,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_38(
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
            "failed_count": 1,
            "repaired_count": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_39(
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
            "XXrepaired_countXX": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_40(
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
            "REPAIRED_COUNT": 0,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_41(
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
            "repaired_count": 1,
            "total_repair_attempts": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_42(
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
            "XXtotal_repair_attemptsXX": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_43(
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
            "TOTAL_REPAIR_ATTEMPTS": 0,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_44(
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
            "total_repair_attempts": 1,
            "tier1_issues": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_45(
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
            "XXtier1_issuesXX": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_46(
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
            "TIER1_ISSUES": 0,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_47(
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
            "tier1_issues": 1,
            "tier2_issues": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_48(
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
            "XXtier2_issuesXX": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_49(
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
            "TIER2_ISSUES": 0,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_50(
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
            "tier2_issues": 1,
            "tier3_issues": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_51(
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
            "XXtier3_issuesXX": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_52(
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
            "TIER3_ISSUES": 0,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_53(
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
            "tier3_issues": 1,
            "tier4_issues": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_54(
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
            "XXtier4_issuesXX": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_55(
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
            "TIER4_ISSUES": 0,
        }
    
    def xǁMigrationContextǁ__init____mutmut_56(
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
            "tier4_issues": 1,
        }
    
    xǁMigrationContextǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁ__init____mutmut_1': xǁMigrationContextǁ__init____mutmut_1, 
        'xǁMigrationContextǁ__init____mutmut_2': xǁMigrationContextǁ__init____mutmut_2, 
        'xǁMigrationContextǁ__init____mutmut_3': xǁMigrationContextǁ__init____mutmut_3, 
        'xǁMigrationContextǁ__init____mutmut_4': xǁMigrationContextǁ__init____mutmut_4, 
        'xǁMigrationContextǁ__init____mutmut_5': xǁMigrationContextǁ__init____mutmut_5, 
        'xǁMigrationContextǁ__init____mutmut_6': xǁMigrationContextǁ__init____mutmut_6, 
        'xǁMigrationContextǁ__init____mutmut_7': xǁMigrationContextǁ__init____mutmut_7, 
        'xǁMigrationContextǁ__init____mutmut_8': xǁMigrationContextǁ__init____mutmut_8, 
        'xǁMigrationContextǁ__init____mutmut_9': xǁMigrationContextǁ__init____mutmut_9, 
        'xǁMigrationContextǁ__init____mutmut_10': xǁMigrationContextǁ__init____mutmut_10, 
        'xǁMigrationContextǁ__init____mutmut_11': xǁMigrationContextǁ__init____mutmut_11, 
        'xǁMigrationContextǁ__init____mutmut_12': xǁMigrationContextǁ__init____mutmut_12, 
        'xǁMigrationContextǁ__init____mutmut_13': xǁMigrationContextǁ__init____mutmut_13, 
        'xǁMigrationContextǁ__init____mutmut_14': xǁMigrationContextǁ__init____mutmut_14, 
        'xǁMigrationContextǁ__init____mutmut_15': xǁMigrationContextǁ__init____mutmut_15, 
        'xǁMigrationContextǁ__init____mutmut_16': xǁMigrationContextǁ__init____mutmut_16, 
        'xǁMigrationContextǁ__init____mutmut_17': xǁMigrationContextǁ__init____mutmut_17, 
        'xǁMigrationContextǁ__init____mutmut_18': xǁMigrationContextǁ__init____mutmut_18, 
        'xǁMigrationContextǁ__init____mutmut_19': xǁMigrationContextǁ__init____mutmut_19, 
        'xǁMigrationContextǁ__init____mutmut_20': xǁMigrationContextǁ__init____mutmut_20, 
        'xǁMigrationContextǁ__init____mutmut_21': xǁMigrationContextǁ__init____mutmut_21, 
        'xǁMigrationContextǁ__init____mutmut_22': xǁMigrationContextǁ__init____mutmut_22, 
        'xǁMigrationContextǁ__init____mutmut_23': xǁMigrationContextǁ__init____mutmut_23, 
        'xǁMigrationContextǁ__init____mutmut_24': xǁMigrationContextǁ__init____mutmut_24, 
        'xǁMigrationContextǁ__init____mutmut_25': xǁMigrationContextǁ__init____mutmut_25, 
        'xǁMigrationContextǁ__init____mutmut_26': xǁMigrationContextǁ__init____mutmut_26, 
        'xǁMigrationContextǁ__init____mutmut_27': xǁMigrationContextǁ__init____mutmut_27, 
        'xǁMigrationContextǁ__init____mutmut_28': xǁMigrationContextǁ__init____mutmut_28, 
        'xǁMigrationContextǁ__init____mutmut_29': xǁMigrationContextǁ__init____mutmut_29, 
        'xǁMigrationContextǁ__init____mutmut_30': xǁMigrationContextǁ__init____mutmut_30, 
        'xǁMigrationContextǁ__init____mutmut_31': xǁMigrationContextǁ__init____mutmut_31, 
        'xǁMigrationContextǁ__init____mutmut_32': xǁMigrationContextǁ__init____mutmut_32, 
        'xǁMigrationContextǁ__init____mutmut_33': xǁMigrationContextǁ__init____mutmut_33, 
        'xǁMigrationContextǁ__init____mutmut_34': xǁMigrationContextǁ__init____mutmut_34, 
        'xǁMigrationContextǁ__init____mutmut_35': xǁMigrationContextǁ__init____mutmut_35, 
        'xǁMigrationContextǁ__init____mutmut_36': xǁMigrationContextǁ__init____mutmut_36, 
        'xǁMigrationContextǁ__init____mutmut_37': xǁMigrationContextǁ__init____mutmut_37, 
        'xǁMigrationContextǁ__init____mutmut_38': xǁMigrationContextǁ__init____mutmut_38, 
        'xǁMigrationContextǁ__init____mutmut_39': xǁMigrationContextǁ__init____mutmut_39, 
        'xǁMigrationContextǁ__init____mutmut_40': xǁMigrationContextǁ__init____mutmut_40, 
        'xǁMigrationContextǁ__init____mutmut_41': xǁMigrationContextǁ__init____mutmut_41, 
        'xǁMigrationContextǁ__init____mutmut_42': xǁMigrationContextǁ__init____mutmut_42, 
        'xǁMigrationContextǁ__init____mutmut_43': xǁMigrationContextǁ__init____mutmut_43, 
        'xǁMigrationContextǁ__init____mutmut_44': xǁMigrationContextǁ__init____mutmut_44, 
        'xǁMigrationContextǁ__init____mutmut_45': xǁMigrationContextǁ__init____mutmut_45, 
        'xǁMigrationContextǁ__init____mutmut_46': xǁMigrationContextǁ__init____mutmut_46, 
        'xǁMigrationContextǁ__init____mutmut_47': xǁMigrationContextǁ__init____mutmut_47, 
        'xǁMigrationContextǁ__init____mutmut_48': xǁMigrationContextǁ__init____mutmut_48, 
        'xǁMigrationContextǁ__init____mutmut_49': xǁMigrationContextǁ__init____mutmut_49, 
        'xǁMigrationContextǁ__init____mutmut_50': xǁMigrationContextǁ__init____mutmut_50, 
        'xǁMigrationContextǁ__init____mutmut_51': xǁMigrationContextǁ__init____mutmut_51, 
        'xǁMigrationContextǁ__init____mutmut_52': xǁMigrationContextǁ__init____mutmut_52, 
        'xǁMigrationContextǁ__init____mutmut_53': xǁMigrationContextǁ__init____mutmut_53, 
        'xǁMigrationContextǁ__init____mutmut_54': xǁMigrationContextǁ__init____mutmut_54, 
        'xǁMigrationContextǁ__init____mutmut_55': xǁMigrationContextǁ__init____mutmut_55, 
        'xǁMigrationContextǁ__init____mutmut_56': xǁMigrationContextǁ__init____mutmut_56
    }
    xǁMigrationContextǁ__init____mutmut_orig.__name__ = 'xǁMigrationContextǁ__init__'
    
    def add_log(self, msg: str):
        args = [msg]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁadd_log__mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁadd_log__mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁadd_log__mutmut_orig(self, msg: str):
        import sys
        print(msg, file=sys.stderr)
        self.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] {msg}")
    
    def xǁMigrationContextǁadd_log__mutmut_1(self, msg: str):
        import sys
        print(None, file=sys.stderr)
        self.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] {msg}")
    
    def xǁMigrationContextǁadd_log__mutmut_2(self, msg: str):
        import sys
        print(msg, file=None)
        self.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] {msg}")
    
    def xǁMigrationContextǁadd_log__mutmut_3(self, msg: str):
        import sys
        print(file=sys.stderr)
        self.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] {msg}")
    
    def xǁMigrationContextǁadd_log__mutmut_4(self, msg: str):
        import sys
        print(msg, )
        self.execution_logs.append(f"[{datetime.utcnow().strftime('%H:%M:%S')}] {msg}")
    
    def xǁMigrationContextǁadd_log__mutmut_5(self, msg: str):
        import sys
        print(msg, file=sys.stderr)
        self.execution_logs.append(None)
    
    def xǁMigrationContextǁadd_log__mutmut_6(self, msg: str):
        import sys
        print(msg, file=sys.stderr)
        self.execution_logs.append(f"[{datetime.utcnow().strftime(None)}] {msg}")
    
    def xǁMigrationContextǁadd_log__mutmut_7(self, msg: str):
        import sys
        print(msg, file=sys.stderr)
        self.execution_logs.append(f"[{datetime.utcnow().strftime('XX%H:%M:%SXX')}] {msg}")
    
    def xǁMigrationContextǁadd_log__mutmut_8(self, msg: str):
        import sys
        print(msg, file=sys.stderr)
        self.execution_logs.append(f"[{datetime.utcnow().strftime('%h:%m:%s')}] {msg}")
    
    xǁMigrationContextǁadd_log__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁadd_log__mutmut_1': xǁMigrationContextǁadd_log__mutmut_1, 
        'xǁMigrationContextǁadd_log__mutmut_2': xǁMigrationContextǁadd_log__mutmut_2, 
        'xǁMigrationContextǁadd_log__mutmut_3': xǁMigrationContextǁadd_log__mutmut_3, 
        'xǁMigrationContextǁadd_log__mutmut_4': xǁMigrationContextǁadd_log__mutmut_4, 
        'xǁMigrationContextǁadd_log__mutmut_5': xǁMigrationContextǁadd_log__mutmut_5, 
        'xǁMigrationContextǁadd_log__mutmut_6': xǁMigrationContextǁadd_log__mutmut_6, 
        'xǁMigrationContextǁadd_log__mutmut_7': xǁMigrationContextǁadd_log__mutmut_7, 
        'xǁMigrationContextǁadd_log__mutmut_8': xǁMigrationContextǁadd_log__mutmut_8
    }
    xǁMigrationContextǁadd_log__mutmut_orig.__name__ = 'xǁMigrationContextǁadd_log'
    
    def add_original_file(self, file_path: str, content: str, file_type: str = "unknown"):
        args = [file_path, content, file_type]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁadd_original_file__mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁadd_original_file__mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁadd_original_file__mutmut_orig(self, file_path: str, content: str, file_type: str = "unknown"):
        """Register an original file before migration."""
        self.original_files[file_path] = content
        self.file_types[file_path] = file_type
        self.stats["total_files"] = len(self.original_files)
    
    def xǁMigrationContextǁadd_original_file__mutmut_1(self, file_path: str, content: str, file_type: str = "XXunknownXX"):
        """Register an original file before migration."""
        self.original_files[file_path] = content
        self.file_types[file_path] = file_type
        self.stats["total_files"] = len(self.original_files)
    
    def xǁMigrationContextǁadd_original_file__mutmut_2(self, file_path: str, content: str, file_type: str = "UNKNOWN"):
        """Register an original file before migration."""
        self.original_files[file_path] = content
        self.file_types[file_path] = file_type
        self.stats["total_files"] = len(self.original_files)
    
    def xǁMigrationContextǁadd_original_file__mutmut_3(self, file_path: str, content: str, file_type: str = "unknown"):
        """Register an original file before migration."""
        self.original_files[file_path] = None
        self.file_types[file_path] = file_type
        self.stats["total_files"] = len(self.original_files)
    
    def xǁMigrationContextǁadd_original_file__mutmut_4(self, file_path: str, content: str, file_type: str = "unknown"):
        """Register an original file before migration."""
        self.original_files[file_path] = content
        self.file_types[file_path] = None
        self.stats["total_files"] = len(self.original_files)
    
    def xǁMigrationContextǁadd_original_file__mutmut_5(self, file_path: str, content: str, file_type: str = "unknown"):
        """Register an original file before migration."""
        self.original_files[file_path] = content
        self.file_types[file_path] = file_type
        self.stats["total_files"] = None
    
    def xǁMigrationContextǁadd_original_file__mutmut_6(self, file_path: str, content: str, file_type: str = "unknown"):
        """Register an original file before migration."""
        self.original_files[file_path] = content
        self.file_types[file_path] = file_type
        self.stats["XXtotal_filesXX"] = len(self.original_files)
    
    def xǁMigrationContextǁadd_original_file__mutmut_7(self, file_path: str, content: str, file_type: str = "unknown"):
        """Register an original file before migration."""
        self.original_files[file_path] = content
        self.file_types[file_path] = file_type
        self.stats["TOTAL_FILES"] = len(self.original_files)
    
    xǁMigrationContextǁadd_original_file__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁadd_original_file__mutmut_1': xǁMigrationContextǁadd_original_file__mutmut_1, 
        'xǁMigrationContextǁadd_original_file__mutmut_2': xǁMigrationContextǁadd_original_file__mutmut_2, 
        'xǁMigrationContextǁadd_original_file__mutmut_3': xǁMigrationContextǁadd_original_file__mutmut_3, 
        'xǁMigrationContextǁadd_original_file__mutmut_4': xǁMigrationContextǁadd_original_file__mutmut_4, 
        'xǁMigrationContextǁadd_original_file__mutmut_5': xǁMigrationContextǁadd_original_file__mutmut_5, 
        'xǁMigrationContextǁadd_original_file__mutmut_6': xǁMigrationContextǁadd_original_file__mutmut_6, 
        'xǁMigrationContextǁadd_original_file__mutmut_7': xǁMigrationContextǁadd_original_file__mutmut_7
    }
    xǁMigrationContextǁadd_original_file__mutmut_orig.__name__ = 'xǁMigrationContextǁadd_original_file'
    
    def add_migration_result(self, file_path: str, result: Dict):
        args = [file_path, result]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁadd_migration_result__mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁadd_migration_result__mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁadd_migration_result__mutmut_orig(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_1(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = None
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_2(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") or result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_3(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get(None) and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_4(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("XXsuccessXX") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_5(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("SUCCESS") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_6(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get(None):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_7(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("XXmigrated_codeXX"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_8(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("MIGRATED_CODE"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_9(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = None
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_10(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["XXmigrated_codeXX"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_11(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["MIGRATED_CODE"]
            self.stats["migrated_count"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_12(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] = 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_13(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] -= 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_14(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["XXmigrated_countXX"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_15(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["MIGRATED_COUNT"] += 1
    
    def xǁMigrationContextǁadd_migration_result__mutmut_16(self, file_path: str, result: Dict):
        """Record the result of migrating a file."""
        self.migration_results[file_path] = result
        if result.get("success") and result.get("migrated_code"):
            self.migrated_files[file_path] = result["migrated_code"]
            self.stats["migrated_count"] += 2
    
    xǁMigrationContextǁadd_migration_result__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁadd_migration_result__mutmut_1': xǁMigrationContextǁadd_migration_result__mutmut_1, 
        'xǁMigrationContextǁadd_migration_result__mutmut_2': xǁMigrationContextǁadd_migration_result__mutmut_2, 
        'xǁMigrationContextǁadd_migration_result__mutmut_3': xǁMigrationContextǁadd_migration_result__mutmut_3, 
        'xǁMigrationContextǁadd_migration_result__mutmut_4': xǁMigrationContextǁadd_migration_result__mutmut_4, 
        'xǁMigrationContextǁadd_migration_result__mutmut_5': xǁMigrationContextǁadd_migration_result__mutmut_5, 
        'xǁMigrationContextǁadd_migration_result__mutmut_6': xǁMigrationContextǁadd_migration_result__mutmut_6, 
        'xǁMigrationContextǁadd_migration_result__mutmut_7': xǁMigrationContextǁadd_migration_result__mutmut_7, 
        'xǁMigrationContextǁadd_migration_result__mutmut_8': xǁMigrationContextǁadd_migration_result__mutmut_8, 
        'xǁMigrationContextǁadd_migration_result__mutmut_9': xǁMigrationContextǁadd_migration_result__mutmut_9, 
        'xǁMigrationContextǁadd_migration_result__mutmut_10': xǁMigrationContextǁadd_migration_result__mutmut_10, 
        'xǁMigrationContextǁadd_migration_result__mutmut_11': xǁMigrationContextǁadd_migration_result__mutmut_11, 
        'xǁMigrationContextǁadd_migration_result__mutmut_12': xǁMigrationContextǁadd_migration_result__mutmut_12, 
        'xǁMigrationContextǁadd_migration_result__mutmut_13': xǁMigrationContextǁadd_migration_result__mutmut_13, 
        'xǁMigrationContextǁadd_migration_result__mutmut_14': xǁMigrationContextǁadd_migration_result__mutmut_14, 
        'xǁMigrationContextǁadd_migration_result__mutmut_15': xǁMigrationContextǁadd_migration_result__mutmut_15, 
        'xǁMigrationContextǁadd_migration_result__mutmut_16': xǁMigrationContextǁadd_migration_result__mutmut_16
    }
    xǁMigrationContextǁadd_migration_result__mutmut_orig.__name__ = 'xǁMigrationContextǁadd_migration_result'
    
    def add_validation_result(self, file_path: str, result: Dict):
        args = [file_path, result]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁadd_validation_result__mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁadd_validation_result__mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁadd_validation_result__mutmut_orig(self, file_path: str, result: Dict):
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
    
    def xǁMigrationContextǁadd_validation_result__mutmut_1(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = None
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_2(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] = 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_3(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] -= 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_4(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["XXvalidated_countXX"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_5(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["VALIDATED_COUNT"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_6(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 2
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_7(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get(None):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_8(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("XXpassedXX"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_9(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("PASSED"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_10(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] = 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_11(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] -= 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_12(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["XXpassed_countXX"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_13(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["PASSED_COUNT"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_14(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 2
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_15(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] = 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_16(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] -= 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_17(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["XXfailed_countXX"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_18(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["FAILED_COUNT"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_19(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 2
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_20(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get(None, []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_21(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", None):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_22(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get([]):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_23(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", ):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_24(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("XXissuesXX", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_25(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("ISSUES", []):
            tier = issue.get("tier", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_26(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = None
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_27(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get(None, 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_28(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", None)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_29(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get(1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_30(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", )
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_31(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("XXtierXX", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_32(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("TIER", 1)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_33(self, file_path: str, result: Dict):
        """Record validation results for a file."""
        self.validation_results[file_path] = result
        self.stats["validated_count"] += 1
        
        if result.get("passed"):
            self.stats["passed_count"] += 1
        else:
            self.stats["failed_count"] += 1
            
        # Count issues by tier
        for issue in result.get("issues", []):
            tier = issue.get("tier", 2)
            self.stats[f"tier{tier}_issues"] += 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_34(self, file_path: str, result: Dict):
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
            self.stats[f"tier{tier}_issues"] = 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_35(self, file_path: str, result: Dict):
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
            self.stats[f"tier{tier}_issues"] -= 1
    
    def xǁMigrationContextǁadd_validation_result__mutmut_36(self, file_path: str, result: Dict):
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
            self.stats[f"tier{tier}_issues"] += 2
    
    xǁMigrationContextǁadd_validation_result__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁadd_validation_result__mutmut_1': xǁMigrationContextǁadd_validation_result__mutmut_1, 
        'xǁMigrationContextǁadd_validation_result__mutmut_2': xǁMigrationContextǁadd_validation_result__mutmut_2, 
        'xǁMigrationContextǁadd_validation_result__mutmut_3': xǁMigrationContextǁadd_validation_result__mutmut_3, 
        'xǁMigrationContextǁadd_validation_result__mutmut_4': xǁMigrationContextǁadd_validation_result__mutmut_4, 
        'xǁMigrationContextǁadd_validation_result__mutmut_5': xǁMigrationContextǁadd_validation_result__mutmut_5, 
        'xǁMigrationContextǁadd_validation_result__mutmut_6': xǁMigrationContextǁadd_validation_result__mutmut_6, 
        'xǁMigrationContextǁadd_validation_result__mutmut_7': xǁMigrationContextǁadd_validation_result__mutmut_7, 
        'xǁMigrationContextǁadd_validation_result__mutmut_8': xǁMigrationContextǁadd_validation_result__mutmut_8, 
        'xǁMigrationContextǁadd_validation_result__mutmut_9': xǁMigrationContextǁadd_validation_result__mutmut_9, 
        'xǁMigrationContextǁadd_validation_result__mutmut_10': xǁMigrationContextǁadd_validation_result__mutmut_10, 
        'xǁMigrationContextǁadd_validation_result__mutmut_11': xǁMigrationContextǁadd_validation_result__mutmut_11, 
        'xǁMigrationContextǁadd_validation_result__mutmut_12': xǁMigrationContextǁadd_validation_result__mutmut_12, 
        'xǁMigrationContextǁadd_validation_result__mutmut_13': xǁMigrationContextǁadd_validation_result__mutmut_13, 
        'xǁMigrationContextǁadd_validation_result__mutmut_14': xǁMigrationContextǁadd_validation_result__mutmut_14, 
        'xǁMigrationContextǁadd_validation_result__mutmut_15': xǁMigrationContextǁadd_validation_result__mutmut_15, 
        'xǁMigrationContextǁadd_validation_result__mutmut_16': xǁMigrationContextǁadd_validation_result__mutmut_16, 
        'xǁMigrationContextǁadd_validation_result__mutmut_17': xǁMigrationContextǁadd_validation_result__mutmut_17, 
        'xǁMigrationContextǁadd_validation_result__mutmut_18': xǁMigrationContextǁadd_validation_result__mutmut_18, 
        'xǁMigrationContextǁadd_validation_result__mutmut_19': xǁMigrationContextǁadd_validation_result__mutmut_19, 
        'xǁMigrationContextǁadd_validation_result__mutmut_20': xǁMigrationContextǁadd_validation_result__mutmut_20, 
        'xǁMigrationContextǁadd_validation_result__mutmut_21': xǁMigrationContextǁadd_validation_result__mutmut_21, 
        'xǁMigrationContextǁadd_validation_result__mutmut_22': xǁMigrationContextǁadd_validation_result__mutmut_22, 
        'xǁMigrationContextǁadd_validation_result__mutmut_23': xǁMigrationContextǁadd_validation_result__mutmut_23, 
        'xǁMigrationContextǁadd_validation_result__mutmut_24': xǁMigrationContextǁadd_validation_result__mutmut_24, 
        'xǁMigrationContextǁadd_validation_result__mutmut_25': xǁMigrationContextǁadd_validation_result__mutmut_25, 
        'xǁMigrationContextǁadd_validation_result__mutmut_26': xǁMigrationContextǁadd_validation_result__mutmut_26, 
        'xǁMigrationContextǁadd_validation_result__mutmut_27': xǁMigrationContextǁadd_validation_result__mutmut_27, 
        'xǁMigrationContextǁadd_validation_result__mutmut_28': xǁMigrationContextǁadd_validation_result__mutmut_28, 
        'xǁMigrationContextǁadd_validation_result__mutmut_29': xǁMigrationContextǁadd_validation_result__mutmut_29, 
        'xǁMigrationContextǁadd_validation_result__mutmut_30': xǁMigrationContextǁadd_validation_result__mutmut_30, 
        'xǁMigrationContextǁadd_validation_result__mutmut_31': xǁMigrationContextǁadd_validation_result__mutmut_31, 
        'xǁMigrationContextǁadd_validation_result__mutmut_32': xǁMigrationContextǁadd_validation_result__mutmut_32, 
        'xǁMigrationContextǁadd_validation_result__mutmut_33': xǁMigrationContextǁadd_validation_result__mutmut_33, 
        'xǁMigrationContextǁadd_validation_result__mutmut_34': xǁMigrationContextǁadd_validation_result__mutmut_34, 
        'xǁMigrationContextǁadd_validation_result__mutmut_35': xǁMigrationContextǁadd_validation_result__mutmut_35, 
        'xǁMigrationContextǁadd_validation_result__mutmut_36': xǁMigrationContextǁadd_validation_result__mutmut_36
    }
    xǁMigrationContextǁadd_validation_result__mutmut_orig.__name__ = 'xǁMigrationContextǁadd_validation_result'
    
    def add_repair_attempt(self, file_path: str, attempt: Dict):
        args = [file_path, attempt]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁadd_repair_attempt__mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁadd_repair_attempt__mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_orig(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_1(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_2(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = None
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_3(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(None)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_4(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] = 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_5(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] -= 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_6(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["XXtotal_repair_attemptsXX"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_7(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["TOTAL_REPAIR_ATTEMPTS"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_8(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 2
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_9(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") or attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_10(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get(None) and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_11(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("XXsuccessXX") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_12(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("SUCCESS") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_13(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get(None):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_14(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("XXrepaired_codeXX"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_15(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("REPAIRED_CODE"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_16(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = None
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_17(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["XXrepaired_codeXX"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_18(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["REPAIRED_CODE"]
            self.stats["repaired_count"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_19(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] = 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_20(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] -= 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_21(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["XXrepaired_countXX"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_22(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["REPAIRED_COUNT"] += 1
    
    def xǁMigrationContextǁadd_repair_attempt__mutmut_23(self, file_path: str, attempt: Dict):
        """Record a repair attempt for a file."""
        if file_path not in self.repair_history:
            self.repair_history[file_path] = []
        self.repair_history[file_path].append(attempt)
        self.stats["total_repair_attempts"] += 1
        
        # Update migrated code if repair succeeded
        if attempt.get("success") and attempt.get("repaired_code"):
            self.migrated_files[file_path] = attempt["repaired_code"]
            self.stats["repaired_count"] += 2
    
    xǁMigrationContextǁadd_repair_attempt__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁadd_repair_attempt__mutmut_1': xǁMigrationContextǁadd_repair_attempt__mutmut_1, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_2': xǁMigrationContextǁadd_repair_attempt__mutmut_2, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_3': xǁMigrationContextǁadd_repair_attempt__mutmut_3, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_4': xǁMigrationContextǁadd_repair_attempt__mutmut_4, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_5': xǁMigrationContextǁadd_repair_attempt__mutmut_5, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_6': xǁMigrationContextǁadd_repair_attempt__mutmut_6, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_7': xǁMigrationContextǁadd_repair_attempt__mutmut_7, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_8': xǁMigrationContextǁadd_repair_attempt__mutmut_8, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_9': xǁMigrationContextǁadd_repair_attempt__mutmut_9, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_10': xǁMigrationContextǁadd_repair_attempt__mutmut_10, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_11': xǁMigrationContextǁadd_repair_attempt__mutmut_11, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_12': xǁMigrationContextǁadd_repair_attempt__mutmut_12, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_13': xǁMigrationContextǁadd_repair_attempt__mutmut_13, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_14': xǁMigrationContextǁadd_repair_attempt__mutmut_14, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_15': xǁMigrationContextǁadd_repair_attempt__mutmut_15, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_16': xǁMigrationContextǁadd_repair_attempt__mutmut_16, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_17': xǁMigrationContextǁadd_repair_attempt__mutmut_17, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_18': xǁMigrationContextǁadd_repair_attempt__mutmut_18, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_19': xǁMigrationContextǁadd_repair_attempt__mutmut_19, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_20': xǁMigrationContextǁadd_repair_attempt__mutmut_20, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_21': xǁMigrationContextǁadd_repair_attempt__mutmut_21, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_22': xǁMigrationContextǁadd_repair_attempt__mutmut_22, 
        'xǁMigrationContextǁadd_repair_attempt__mutmut_23': xǁMigrationContextǁadd_repair_attempt__mutmut_23
    }
    xǁMigrationContextǁadd_repair_attempt__mutmut_orig.__name__ = 'xǁMigrationContextǁadd_repair_attempt'
    
    def get_repair_count(self, file_path: str) -> int:
        """Get number of repair attempts for a file."""
        return len(self.repair_history.get(file_path, []))
    
    def get_related_files(self, file_path: str) -> Dict[str, str]:
        args = [file_path]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁget_related_files__mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁget_related_files__mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁget_related_files__mutmut_orig(self, file_path: str) -> Dict[str, str]:
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
    
    def xǁMigrationContextǁget_related_files__mutmut_1(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = None
        
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
    
    def xǁMigrationContextǁget_related_files__mutmut_2(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = None
            
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
    
    def xǁMigrationContextǁget_related_files__mutmut_3(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get(None, {})
            
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
    
    def xǁMigrationContextǁget_related_files__mutmut_4(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", None)
            
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
    
    def xǁMigrationContextǁget_related_files__mutmut_5(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get({})
            
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
    
    def xǁMigrationContextǁget_related_files__mutmut_6(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", )
            
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
    
    def xǁMigrationContextǁget_related_files__mutmut_7(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("XXdjango_dependenciesXX", {})
            
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
    
    def xǁMigrationContextǁget_related_files__mutmut_8(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("DJANGO_DEPENDENCIES", {})
            
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
    
    def xǁMigrationContextǁget_related_files__mutmut_9(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get(None, []):
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
    
    def xǁMigrationContextǁget_related_files__mutmut_10(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", None):
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
    
    def xǁMigrationContextǁget_related_files__mutmut_11(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get([]):
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
    
    def xǁMigrationContextǁget_related_files__mutmut_12(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", ):
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
    
    def xǁMigrationContextǁget_related_files__mutmut_13(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("XXdependenciesXX", []):
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
    
    def xǁMigrationContextǁget_related_files__mutmut_14(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("DEPENDENCIES", []):
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
    
    def xǁMigrationContextǁget_related_files__mutmut_15(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", []):
                source = None
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
    
    def xǁMigrationContextǁget_related_files__mutmut_16(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", []):
                source = dep_info.get(None, "")
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
    
    def xǁMigrationContextǁget_related_files__mutmut_17(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", []):
                source = dep_info.get("source", None)
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
    
    def xǁMigrationContextǁget_related_files__mutmut_18(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", []):
                source = dep_info.get("")
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
    
    def xǁMigrationContextǁget_related_files__mutmut_19(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", []):
                source = dep_info.get("source", )
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
    
    def xǁMigrationContextǁget_related_files__mutmut_20(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", []):
                source = dep_info.get("XXsourceXX", "")
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
    
    def xǁMigrationContextǁget_related_files__mutmut_21(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", []):
                source = dep_info.get("SOURCE", "")
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
    
    def xǁMigrationContextǁget_related_files__mutmut_22(self, file_path: str) -> Dict[str, str]:
        """
        Get migrated content of files that are related to the given file
        via the dependency graph. Used to provide cross-file context.
        """
        related = {}
        
        # Check dependency graph relationships
        if self.dependency_graph:
            deps = self.dependency_graph.get("django_dependencies", {})
            
            for dep_info in deps.get("dependencies", []):
                source = dep_info.get("source", "XXXX")
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
    
    def xǁMigrationContextǁget_related_files__mutmut_23(self, file_path: str) -> Dict[str, str]:
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
                target = None
                
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
    
    def xǁMigrationContextǁget_related_files__mutmut_24(self, file_path: str) -> Dict[str, str]:
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
                target = dep_info.get(None, "")
                
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
    
    def xǁMigrationContextǁget_related_files__mutmut_25(self, file_path: str) -> Dict[str, str]:
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
                target = dep_info.get("target", None)
                
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
    
    def xǁMigrationContextǁget_related_files__mutmut_26(self, file_path: str) -> Dict[str, str]:
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
                target = dep_info.get("")
                
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
    
    def xǁMigrationContextǁget_related_files__mutmut_27(self, file_path: str) -> Dict[str, str]:
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
                target = dep_info.get("target", )
                
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
    
    def xǁMigrationContextǁget_related_files__mutmut_28(self, file_path: str) -> Dict[str, str]:
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
                target = dep_info.get("XXtargetXX", "")
                
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
    
    def xǁMigrationContextǁget_related_files__mutmut_29(self, file_path: str) -> Dict[str, str]:
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
                target = dep_info.get("TARGET", "")
                
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
    
    def xǁMigrationContextǁget_related_files__mutmut_30(self, file_path: str) -> Dict[str, str]:
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
                target = dep_info.get("target", "XXXX")
                
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
    
    def xǁMigrationContextǁget_related_files__mutmut_31(self, file_path: str) -> Dict[str, str]:
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
                
                if source == file_path or target in self.migrated_files:
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
    
    def xǁMigrationContextǁget_related_files__mutmut_32(self, file_path: str) -> Dict[str, str]:
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
                
                if source != file_path and target in self.migrated_files:
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
    
    def xǁMigrationContextǁget_related_files__mutmut_33(self, file_path: str) -> Dict[str, str]:
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
                
                if source == file_path and target not in self.migrated_files:
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
    
    def xǁMigrationContextǁget_related_files__mutmut_34(self, file_path: str) -> Dict[str, str]:
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
                    related[target] = None
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
    
    def xǁMigrationContextǁget_related_files__mutmut_35(self, file_path: str) -> Dict[str, str]:
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
                elif target == file_path or source in self.migrated_files:
                    related[source] = self.migrated_files[source]
        
        # Also check files_by_type for same-app relationships
        file_parts = file_path.replace("\\", "/").split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_36(self, file_path: str) -> Dict[str, str]:
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
                elif target != file_path and source in self.migrated_files:
                    related[source] = self.migrated_files[source]
        
        # Also check files_by_type for same-app relationships
        file_parts = file_path.replace("\\", "/").split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_37(self, file_path: str) -> Dict[str, str]:
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
                elif target == file_path and source not in self.migrated_files:
                    related[source] = self.migrated_files[source]
        
        # Also check files_by_type for same-app relationships
        file_parts = file_path.replace("\\", "/").split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_38(self, file_path: str) -> Dict[str, str]:
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
                    related[source] = None
        
        # Also check files_by_type for same-app relationships
        file_parts = file_path.replace("\\", "/").split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_39(self, file_path: str) -> Dict[str, str]:
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
        file_parts = None
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_40(self, file_path: str) -> Dict[str, str]:
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
        file_parts = file_path.replace("\\", "/").split(None)
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_41(self, file_path: str) -> Dict[str, str]:
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
        file_parts = file_path.replace(None, "/").split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_42(self, file_path: str) -> Dict[str, str]:
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
        file_parts = file_path.replace("\\", None).split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_43(self, file_path: str) -> Dict[str, str]:
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
        file_parts = file_path.replace("/").split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_44(self, file_path: str) -> Dict[str, str]:
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
        file_parts = file_path.replace("\\", ).split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_45(self, file_path: str) -> Dict[str, str]:
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
        file_parts = file_path.replace("XX\\XX", "/").split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_46(self, file_path: str) -> Dict[str, str]:
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
        file_parts = file_path.replace("\\", "XX/XX").split("/")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_47(self, file_path: str) -> Dict[str, str]:
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
        file_parts = file_path.replace("\\", "/").split("XX/XX")
        if len(file_parts) > 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_48(self, file_path: str) -> Dict[str, str]:
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
        if len(file_parts) >= 1:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_49(self, file_path: str) -> Dict[str, str]:
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
        if len(file_parts) > 2:
            app_prefix = "/".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_50(self, file_path: str) -> Dict[str, str]:
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
            app_prefix = None
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_51(self, file_path: str) -> Dict[str, str]:
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
            app_prefix = "/".join(None)
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_52(self, file_path: str) -> Dict[str, str]:
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
            app_prefix = "XX/XX".join(file_parts[:-1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_53(self, file_path: str) -> Dict[str, str]:
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
            app_prefix = "/".join(file_parts[:+1])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_54(self, file_path: str) -> Dict[str, str]:
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
            app_prefix = "/".join(file_parts[:-2])
            for path, content in self.migrated_files.items():
                if path != file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_55(self, file_path: str) -> Dict[str, str]:
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
                if path != file_path or path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_56(self, file_path: str) -> Dict[str, str]:
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
                if path == file_path and path.startswith(app_prefix):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_57(self, file_path: str) -> Dict[str, str]:
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
                if path != file_path and path.startswith(None):
                    related[path] = content
        
        return related
    
    def xǁMigrationContextǁget_related_files__mutmut_58(self, file_path: str) -> Dict[str, str]:
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
                    related[path] = None
        
        return related
    
    xǁMigrationContextǁget_related_files__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁget_related_files__mutmut_1': xǁMigrationContextǁget_related_files__mutmut_1, 
        'xǁMigrationContextǁget_related_files__mutmut_2': xǁMigrationContextǁget_related_files__mutmut_2, 
        'xǁMigrationContextǁget_related_files__mutmut_3': xǁMigrationContextǁget_related_files__mutmut_3, 
        'xǁMigrationContextǁget_related_files__mutmut_4': xǁMigrationContextǁget_related_files__mutmut_4, 
        'xǁMigrationContextǁget_related_files__mutmut_5': xǁMigrationContextǁget_related_files__mutmut_5, 
        'xǁMigrationContextǁget_related_files__mutmut_6': xǁMigrationContextǁget_related_files__mutmut_6, 
        'xǁMigrationContextǁget_related_files__mutmut_7': xǁMigrationContextǁget_related_files__mutmut_7, 
        'xǁMigrationContextǁget_related_files__mutmut_8': xǁMigrationContextǁget_related_files__mutmut_8, 
        'xǁMigrationContextǁget_related_files__mutmut_9': xǁMigrationContextǁget_related_files__mutmut_9, 
        'xǁMigrationContextǁget_related_files__mutmut_10': xǁMigrationContextǁget_related_files__mutmut_10, 
        'xǁMigrationContextǁget_related_files__mutmut_11': xǁMigrationContextǁget_related_files__mutmut_11, 
        'xǁMigrationContextǁget_related_files__mutmut_12': xǁMigrationContextǁget_related_files__mutmut_12, 
        'xǁMigrationContextǁget_related_files__mutmut_13': xǁMigrationContextǁget_related_files__mutmut_13, 
        'xǁMigrationContextǁget_related_files__mutmut_14': xǁMigrationContextǁget_related_files__mutmut_14, 
        'xǁMigrationContextǁget_related_files__mutmut_15': xǁMigrationContextǁget_related_files__mutmut_15, 
        'xǁMigrationContextǁget_related_files__mutmut_16': xǁMigrationContextǁget_related_files__mutmut_16, 
        'xǁMigrationContextǁget_related_files__mutmut_17': xǁMigrationContextǁget_related_files__mutmut_17, 
        'xǁMigrationContextǁget_related_files__mutmut_18': xǁMigrationContextǁget_related_files__mutmut_18, 
        'xǁMigrationContextǁget_related_files__mutmut_19': xǁMigrationContextǁget_related_files__mutmut_19, 
        'xǁMigrationContextǁget_related_files__mutmut_20': xǁMigrationContextǁget_related_files__mutmut_20, 
        'xǁMigrationContextǁget_related_files__mutmut_21': xǁMigrationContextǁget_related_files__mutmut_21, 
        'xǁMigrationContextǁget_related_files__mutmut_22': xǁMigrationContextǁget_related_files__mutmut_22, 
        'xǁMigrationContextǁget_related_files__mutmut_23': xǁMigrationContextǁget_related_files__mutmut_23, 
        'xǁMigrationContextǁget_related_files__mutmut_24': xǁMigrationContextǁget_related_files__mutmut_24, 
        'xǁMigrationContextǁget_related_files__mutmut_25': xǁMigrationContextǁget_related_files__mutmut_25, 
        'xǁMigrationContextǁget_related_files__mutmut_26': xǁMigrationContextǁget_related_files__mutmut_26, 
        'xǁMigrationContextǁget_related_files__mutmut_27': xǁMigrationContextǁget_related_files__mutmut_27, 
        'xǁMigrationContextǁget_related_files__mutmut_28': xǁMigrationContextǁget_related_files__mutmut_28, 
        'xǁMigrationContextǁget_related_files__mutmut_29': xǁMigrationContextǁget_related_files__mutmut_29, 
        'xǁMigrationContextǁget_related_files__mutmut_30': xǁMigrationContextǁget_related_files__mutmut_30, 
        'xǁMigrationContextǁget_related_files__mutmut_31': xǁMigrationContextǁget_related_files__mutmut_31, 
        'xǁMigrationContextǁget_related_files__mutmut_32': xǁMigrationContextǁget_related_files__mutmut_32, 
        'xǁMigrationContextǁget_related_files__mutmut_33': xǁMigrationContextǁget_related_files__mutmut_33, 
        'xǁMigrationContextǁget_related_files__mutmut_34': xǁMigrationContextǁget_related_files__mutmut_34, 
        'xǁMigrationContextǁget_related_files__mutmut_35': xǁMigrationContextǁget_related_files__mutmut_35, 
        'xǁMigrationContextǁget_related_files__mutmut_36': xǁMigrationContextǁget_related_files__mutmut_36, 
        'xǁMigrationContextǁget_related_files__mutmut_37': xǁMigrationContextǁget_related_files__mutmut_37, 
        'xǁMigrationContextǁget_related_files__mutmut_38': xǁMigrationContextǁget_related_files__mutmut_38, 
        'xǁMigrationContextǁget_related_files__mutmut_39': xǁMigrationContextǁget_related_files__mutmut_39, 
        'xǁMigrationContextǁget_related_files__mutmut_40': xǁMigrationContextǁget_related_files__mutmut_40, 
        'xǁMigrationContextǁget_related_files__mutmut_41': xǁMigrationContextǁget_related_files__mutmut_41, 
        'xǁMigrationContextǁget_related_files__mutmut_42': xǁMigrationContextǁget_related_files__mutmut_42, 
        'xǁMigrationContextǁget_related_files__mutmut_43': xǁMigrationContextǁget_related_files__mutmut_43, 
        'xǁMigrationContextǁget_related_files__mutmut_44': xǁMigrationContextǁget_related_files__mutmut_44, 
        'xǁMigrationContextǁget_related_files__mutmut_45': xǁMigrationContextǁget_related_files__mutmut_45, 
        'xǁMigrationContextǁget_related_files__mutmut_46': xǁMigrationContextǁget_related_files__mutmut_46, 
        'xǁMigrationContextǁget_related_files__mutmut_47': xǁMigrationContextǁget_related_files__mutmut_47, 
        'xǁMigrationContextǁget_related_files__mutmut_48': xǁMigrationContextǁget_related_files__mutmut_48, 
        'xǁMigrationContextǁget_related_files__mutmut_49': xǁMigrationContextǁget_related_files__mutmut_49, 
        'xǁMigrationContextǁget_related_files__mutmut_50': xǁMigrationContextǁget_related_files__mutmut_50, 
        'xǁMigrationContextǁget_related_files__mutmut_51': xǁMigrationContextǁget_related_files__mutmut_51, 
        'xǁMigrationContextǁget_related_files__mutmut_52': xǁMigrationContextǁget_related_files__mutmut_52, 
        'xǁMigrationContextǁget_related_files__mutmut_53': xǁMigrationContextǁget_related_files__mutmut_53, 
        'xǁMigrationContextǁget_related_files__mutmut_54': xǁMigrationContextǁget_related_files__mutmut_54, 
        'xǁMigrationContextǁget_related_files__mutmut_55': xǁMigrationContextǁget_related_files__mutmut_55, 
        'xǁMigrationContextǁget_related_files__mutmut_56': xǁMigrationContextǁget_related_files__mutmut_56, 
        'xǁMigrationContextǁget_related_files__mutmut_57': xǁMigrationContextǁget_related_files__mutmut_57, 
        'xǁMigrationContextǁget_related_files__mutmut_58': xǁMigrationContextǁget_related_files__mutmut_58
    }
    xǁMigrationContextǁget_related_files__mutmut_orig.__name__ = 'xǁMigrationContextǁget_related_files'
    
    def get_context_for_migration(self, file_path: str) -> Dict[str, Any]:
        args = [file_path]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁget_context_for_migration__mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁget_context_for_migration__mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_orig(self, file_path: str) -> Dict[str, Any]:
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
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_1(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "XXfile_pathXX": file_path,
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
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_2(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "FILE_PATH": file_path,
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
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_3(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "XXoriginal_codeXX": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_4(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "ORIGINAL_CODE": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_5(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(None, ""),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_6(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, None),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_7(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(""),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_8(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_9(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, "XXXX"),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_10(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "XXfile_typeXX": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_11(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "FILE_TYPE": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_12(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(None, "unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_13(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, None),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_14(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get("unknown"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_15(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, ),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_16(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, "XXunknownXX"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_17(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, "UNKNOWN"),
            "source_version": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_18(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, "unknown"),
            "XXsource_versionXX": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_19(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, "unknown"),
            "SOURCE_VERSION": self.source_version,
            "target_version": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_20(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "XXtarget_versionXX": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_21(self, file_path: str) -> Dict[str, Any]:
        """
        Build the full context dict that the Migration Agent needs
        when migrating a specific file.
        """
        return {
            "file_path": file_path,
            "original_code": self.original_files.get(file_path, ""),
            "file_type": self.file_types.get(file_path, "unknown"),
            "source_version": self.source_version,
            "TARGET_VERSION": self.target_version,
            "related_files": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_22(self, file_path: str) -> Dict[str, Any]:
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
            "XXrelated_filesXX": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_23(self, file_path: str) -> Dict[str, Any]:
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
            "RELATED_FILES": self.get_related_files(file_path),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_24(self, file_path: str) -> Dict[str, Any]:
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
            "related_files": self.get_related_files(None),
            "dependency_graph": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_25(self, file_path: str) -> Dict[str, Any]:
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
            "XXdependency_graphXX": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_26(self, file_path: str) -> Dict[str, Any]:
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
            "DEPENDENCY_GRAPH": self.dependency_graph,
            "previous_attempt": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_27(self, file_path: str) -> Dict[str, Any]:
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
            "XXprevious_attemptXX": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_28(self, file_path: str) -> Dict[str, Any]:
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
            "PREVIOUS_ATTEMPT": self.migration_results.get(file_path),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_29(self, file_path: str) -> Dict[str, Any]:
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
            "previous_attempt": self.migration_results.get(None),
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_30(self, file_path: str) -> Dict[str, Any]:
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
            "XXvalidation_errorsXX": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_31(self, file_path: str) -> Dict[str, Any]:
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
            "VALIDATION_ERRORS": self.validation_results.get(file_path, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_32(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get(file_path, {}).get(None, []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_33(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", None),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_34(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get(file_path, {}).get([]),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_35(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get(file_path, {}).get("issues", ),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_36(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get(None, {}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_37(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get(file_path, None).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_38(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get({}).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_39(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get(file_path, ).get("issues", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_40(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get(file_path, {}).get("XXissuesXX", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_41(self, file_path: str) -> Dict[str, Any]:
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
            "validation_errors": self.validation_results.get(file_path, {}).get("ISSUES", []),
            "repair_count": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_42(self, file_path: str) -> Dict[str, Any]:
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
            "XXrepair_countXX": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_43(self, file_path: str) -> Dict[str, Any]:
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
            "REPAIR_COUNT": self.get_repair_count(file_path),
        }
    
    def xǁMigrationContextǁget_context_for_migration__mutmut_44(self, file_path: str) -> Dict[str, Any]:
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
            "repair_count": self.get_repair_count(None),
        }
    
    xǁMigrationContextǁget_context_for_migration__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁget_context_for_migration__mutmut_1': xǁMigrationContextǁget_context_for_migration__mutmut_1, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_2': xǁMigrationContextǁget_context_for_migration__mutmut_2, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_3': xǁMigrationContextǁget_context_for_migration__mutmut_3, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_4': xǁMigrationContextǁget_context_for_migration__mutmut_4, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_5': xǁMigrationContextǁget_context_for_migration__mutmut_5, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_6': xǁMigrationContextǁget_context_for_migration__mutmut_6, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_7': xǁMigrationContextǁget_context_for_migration__mutmut_7, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_8': xǁMigrationContextǁget_context_for_migration__mutmut_8, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_9': xǁMigrationContextǁget_context_for_migration__mutmut_9, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_10': xǁMigrationContextǁget_context_for_migration__mutmut_10, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_11': xǁMigrationContextǁget_context_for_migration__mutmut_11, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_12': xǁMigrationContextǁget_context_for_migration__mutmut_12, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_13': xǁMigrationContextǁget_context_for_migration__mutmut_13, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_14': xǁMigrationContextǁget_context_for_migration__mutmut_14, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_15': xǁMigrationContextǁget_context_for_migration__mutmut_15, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_16': xǁMigrationContextǁget_context_for_migration__mutmut_16, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_17': xǁMigrationContextǁget_context_for_migration__mutmut_17, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_18': xǁMigrationContextǁget_context_for_migration__mutmut_18, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_19': xǁMigrationContextǁget_context_for_migration__mutmut_19, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_20': xǁMigrationContextǁget_context_for_migration__mutmut_20, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_21': xǁMigrationContextǁget_context_for_migration__mutmut_21, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_22': xǁMigrationContextǁget_context_for_migration__mutmut_22, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_23': xǁMigrationContextǁget_context_for_migration__mutmut_23, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_24': xǁMigrationContextǁget_context_for_migration__mutmut_24, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_25': xǁMigrationContextǁget_context_for_migration__mutmut_25, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_26': xǁMigrationContextǁget_context_for_migration__mutmut_26, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_27': xǁMigrationContextǁget_context_for_migration__mutmut_27, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_28': xǁMigrationContextǁget_context_for_migration__mutmut_28, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_29': xǁMigrationContextǁget_context_for_migration__mutmut_29, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_30': xǁMigrationContextǁget_context_for_migration__mutmut_30, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_31': xǁMigrationContextǁget_context_for_migration__mutmut_31, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_32': xǁMigrationContextǁget_context_for_migration__mutmut_32, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_33': xǁMigrationContextǁget_context_for_migration__mutmut_33, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_34': xǁMigrationContextǁget_context_for_migration__mutmut_34, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_35': xǁMigrationContextǁget_context_for_migration__mutmut_35, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_36': xǁMigrationContextǁget_context_for_migration__mutmut_36, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_37': xǁMigrationContextǁget_context_for_migration__mutmut_37, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_38': xǁMigrationContextǁget_context_for_migration__mutmut_38, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_39': xǁMigrationContextǁget_context_for_migration__mutmut_39, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_40': xǁMigrationContextǁget_context_for_migration__mutmut_40, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_41': xǁMigrationContextǁget_context_for_migration__mutmut_41, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_42': xǁMigrationContextǁget_context_for_migration__mutmut_42, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_43': xǁMigrationContextǁget_context_for_migration__mutmut_43, 
        'xǁMigrationContextǁget_context_for_migration__mutmut_44': xǁMigrationContextǁget_context_for_migration__mutmut_44
    }
    xǁMigrationContextǁget_context_for_migration__mutmut_orig.__name__ = 'xǁMigrationContextǁget_context_for_migration'
    
    def get_summary(self) -> Dict[str, Any]:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁget_summary__mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁget_summary__mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁget_summary__mutmut_orig(self) -> Dict[str, Any]:
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
    
    def xǁMigrationContextǁget_summary__mutmut_1(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "XXrepo_idXX": self.repo_id,
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
    
    def xǁMigrationContextǁget_summary__mutmut_2(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "REPO_ID": self.repo_id,
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
    
    def xǁMigrationContextǁget_summary__mutmut_3(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "XXsource_versionXX": self.source_version,
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
    
    def xǁMigrationContextǁget_summary__mutmut_4(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "SOURCE_VERSION": self.source_version,
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
    
    def xǁMigrationContextǁget_summary__mutmut_5(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "XXtarget_versionXX": self.target_version,
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
    
    def xǁMigrationContextǁget_summary__mutmut_6(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "TARGET_VERSION": self.target_version,
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
    
    def xǁMigrationContextǁget_summary__mutmut_7(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "XXpipeline_statusXX": self.pipeline_status,
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
    
    def xǁMigrationContextǁget_summary__mutmut_8(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "PIPELINE_STATUS": self.pipeline_status,
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
    
    def xǁMigrationContextǁget_summary__mutmut_9(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "XXcurrent_batchXX": self.current_batch,
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
    
    def xǁMigrationContextǁget_summary__mutmut_10(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "CURRENT_BATCH": self.current_batch,
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
    
    def xǁMigrationContextǁget_summary__mutmut_11(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "XXstarted_atXX": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "stats": copy.deepcopy(self.stats),
            "files_migrated": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_12(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "STARTED_AT": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "stats": copy.deepcopy(self.stats),
            "files_migrated": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_13(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "XXcompleted_atXX": self.completed_at.isoformat() if self.completed_at else None,
            "stats": copy.deepcopy(self.stats),
            "files_migrated": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_14(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "COMPLETED_AT": self.completed_at.isoformat() if self.completed_at else None,
            "stats": copy.deepcopy(self.stats),
            "files_migrated": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_15(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "XXstatsXX": copy.deepcopy(self.stats),
            "files_migrated": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_16(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "STATS": copy.deepcopy(self.stats),
            "files_migrated": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_17(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "stats": copy.deepcopy(None),
            "files_migrated": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_18(self) -> Dict[str, Any]:
        """Get a summary of the migration context state."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "stats": copy.copy(self.stats),
            "files_migrated": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_19(self) -> Dict[str, Any]:
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
            "XXfiles_migratedXX": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_20(self) -> Dict[str, Any]:
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
            "FILES_MIGRATED": list(self.migrated_files.keys()),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_21(self) -> Dict[str, Any]:
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
            "files_migrated": list(None),
            "files_validated": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_22(self) -> Dict[str, Any]:
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
            "XXfiles_validatedXX": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_23(self) -> Dict[str, Any]:
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
            "FILES_VALIDATED": list(self.validation_results.keys()),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_24(self) -> Dict[str, Any]:
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
            "files_validated": list(None),
            "files_with_issues": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_25(self) -> Dict[str, Any]:
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
            "XXfiles_with_issuesXX": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_26(self) -> Dict[str, Any]:
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
            "FILES_WITH_ISSUES": [
                path for path, result in self.validation_results.items()
                if not result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_27(self) -> Dict[str, Any]:
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
                if result.get("passed")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_28(self) -> Dict[str, Any]:
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
                if not result.get(None)
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_29(self) -> Dict[str, Any]:
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
                if not result.get("XXpassedXX")
            ],
        }
    
    def xǁMigrationContextǁget_summary__mutmut_30(self) -> Dict[str, Any]:
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
                if not result.get("PASSED")
            ],
        }
    
    xǁMigrationContextǁget_summary__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁget_summary__mutmut_1': xǁMigrationContextǁget_summary__mutmut_1, 
        'xǁMigrationContextǁget_summary__mutmut_2': xǁMigrationContextǁget_summary__mutmut_2, 
        'xǁMigrationContextǁget_summary__mutmut_3': xǁMigrationContextǁget_summary__mutmut_3, 
        'xǁMigrationContextǁget_summary__mutmut_4': xǁMigrationContextǁget_summary__mutmut_4, 
        'xǁMigrationContextǁget_summary__mutmut_5': xǁMigrationContextǁget_summary__mutmut_5, 
        'xǁMigrationContextǁget_summary__mutmut_6': xǁMigrationContextǁget_summary__mutmut_6, 
        'xǁMigrationContextǁget_summary__mutmut_7': xǁMigrationContextǁget_summary__mutmut_7, 
        'xǁMigrationContextǁget_summary__mutmut_8': xǁMigrationContextǁget_summary__mutmut_8, 
        'xǁMigrationContextǁget_summary__mutmut_9': xǁMigrationContextǁget_summary__mutmut_9, 
        'xǁMigrationContextǁget_summary__mutmut_10': xǁMigrationContextǁget_summary__mutmut_10, 
        'xǁMigrationContextǁget_summary__mutmut_11': xǁMigrationContextǁget_summary__mutmut_11, 
        'xǁMigrationContextǁget_summary__mutmut_12': xǁMigrationContextǁget_summary__mutmut_12, 
        'xǁMigrationContextǁget_summary__mutmut_13': xǁMigrationContextǁget_summary__mutmut_13, 
        'xǁMigrationContextǁget_summary__mutmut_14': xǁMigrationContextǁget_summary__mutmut_14, 
        'xǁMigrationContextǁget_summary__mutmut_15': xǁMigrationContextǁget_summary__mutmut_15, 
        'xǁMigrationContextǁget_summary__mutmut_16': xǁMigrationContextǁget_summary__mutmut_16, 
        'xǁMigrationContextǁget_summary__mutmut_17': xǁMigrationContextǁget_summary__mutmut_17, 
        'xǁMigrationContextǁget_summary__mutmut_18': xǁMigrationContextǁget_summary__mutmut_18, 
        'xǁMigrationContextǁget_summary__mutmut_19': xǁMigrationContextǁget_summary__mutmut_19, 
        'xǁMigrationContextǁget_summary__mutmut_20': xǁMigrationContextǁget_summary__mutmut_20, 
        'xǁMigrationContextǁget_summary__mutmut_21': xǁMigrationContextǁget_summary__mutmut_21, 
        'xǁMigrationContextǁget_summary__mutmut_22': xǁMigrationContextǁget_summary__mutmut_22, 
        'xǁMigrationContextǁget_summary__mutmut_23': xǁMigrationContextǁget_summary__mutmut_23, 
        'xǁMigrationContextǁget_summary__mutmut_24': xǁMigrationContextǁget_summary__mutmut_24, 
        'xǁMigrationContextǁget_summary__mutmut_25': xǁMigrationContextǁget_summary__mutmut_25, 
        'xǁMigrationContextǁget_summary__mutmut_26': xǁMigrationContextǁget_summary__mutmut_26, 
        'xǁMigrationContextǁget_summary__mutmut_27': xǁMigrationContextǁget_summary__mutmut_27, 
        'xǁMigrationContextǁget_summary__mutmut_28': xǁMigrationContextǁget_summary__mutmut_28, 
        'xǁMigrationContextǁget_summary__mutmut_29': xǁMigrationContextǁget_summary__mutmut_29, 
        'xǁMigrationContextǁget_summary__mutmut_30': xǁMigrationContextǁget_summary__mutmut_30
    }
    xǁMigrationContextǁget_summary__mutmut_orig.__name__ = 'xǁMigrationContextǁget_summary'
    
    def to_dict(self) -> Dict[str, Any]:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁMigrationContextǁto_dict__mutmut_orig'), object.__getattribute__(self, 'xǁMigrationContextǁto_dict__mutmut_mutants'), args, kwargs, self)
    
    def xǁMigrationContextǁto_dict__mutmut_orig(self) -> Dict[str, Any]:
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
    
    def xǁMigrationContextǁto_dict__mutmut_1(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "XXrepo_idXX": self.repo_id,
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
    
    def xǁMigrationContextǁto_dict__mutmut_2(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "REPO_ID": self.repo_id,
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
    
    def xǁMigrationContextǁto_dict__mutmut_3(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "XXsource_versionXX": self.source_version,
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
    
    def xǁMigrationContextǁto_dict__mutmut_4(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "SOURCE_VERSION": self.source_version,
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
    
    def xǁMigrationContextǁto_dict__mutmut_5(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "XXtarget_versionXX": self.target_version,
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
    
    def xǁMigrationContextǁto_dict__mutmut_6(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "TARGET_VERSION": self.target_version,
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
    
    def xǁMigrationContextǁto_dict__mutmut_7(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "XXpipeline_statusXX": self.pipeline_status,
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
    
    def xǁMigrationContextǁto_dict__mutmut_8(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "PIPELINE_STATUS": self.pipeline_status,
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
    
    def xǁMigrationContextǁto_dict__mutmut_9(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "XXcurrent_batchXX": self.current_batch,
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
    
    def xǁMigrationContextǁto_dict__mutmut_10(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "CURRENT_BATCH": self.current_batch,
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
    
    def xǁMigrationContextǁto_dict__mutmut_11(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "XXstarted_atXX": self.started_at,
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
    
    def xǁMigrationContextǁto_dict__mutmut_12(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "STARTED_AT": self.started_at,
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
    
    def xǁMigrationContextǁto_dict__mutmut_13(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at,
            "XXcompleted_atXX": self.completed_at,
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
    
    def xǁMigrationContextǁto_dict__mutmut_14(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at,
            "COMPLETED_AT": self.completed_at,
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
    
    def xǁMigrationContextǁto_dict__mutmut_15(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "XXstatsXX": self.stats,
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
    
    def xǁMigrationContextǁto_dict__mutmut_16(self) -> Dict[str, Any]:
        """Serialize context to dict for storage in MongoDB."""
        return {
            "repo_id": self.repo_id,
            "source_version": self.source_version,
            "target_version": self.target_version,
            "pipeline_status": self.pipeline_status,
            "current_batch": self.current_batch,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "STATS": self.stats,
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
    
    def xǁMigrationContextǁto_dict__mutmut_17(self) -> Dict[str, Any]:
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
            "XXmigration_resultsXX": {
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
    
    def xǁMigrationContextǁto_dict__mutmut_18(self) -> Dict[str, Any]:
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
            "MIGRATION_RESULTS": {
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
    
    def xǁMigrationContextǁto_dict__mutmut_19(self) -> Dict[str, Any]:
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
                    "XXsuccessXX": r.get("success"),
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
    
    def xǁMigrationContextǁto_dict__mutmut_20(self) -> Dict[str, Any]:
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
                    "SUCCESS": r.get("success"),
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
    
    def xǁMigrationContextǁto_dict__mutmut_21(self) -> Dict[str, Any]:
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
                    "success": r.get(None),
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
    
    def xǁMigrationContextǁto_dict__mutmut_22(self) -> Dict[str, Any]:
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
                    "success": r.get("XXsuccessXX"),
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
    
    def xǁMigrationContextǁto_dict__mutmut_23(self) -> Dict[str, Any]:
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
                    "success": r.get("SUCCESS"),
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
    
    def xǁMigrationContextǁto_dict__mutmut_24(self) -> Dict[str, Any]:
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
                    "XXchanges_madeXX": r.get("changes_made", []),
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
    
    def xǁMigrationContextǁto_dict__mutmut_25(self) -> Dict[str, Any]:
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
                    "CHANGES_MADE": r.get("changes_made", []),
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
    
    def xǁMigrationContextǁto_dict__mutmut_26(self) -> Dict[str, Any]:
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
                    "changes_made": r.get(None, []),
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
    
    def xǁMigrationContextǁto_dict__mutmut_27(self) -> Dict[str, Any]:
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
                    "changes_made": r.get("changes_made", None),
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
    
    def xǁMigrationContextǁto_dict__mutmut_28(self) -> Dict[str, Any]:
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
                    "changes_made": r.get([]),
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
    
    def xǁMigrationContextǁto_dict__mutmut_29(self) -> Dict[str, Any]:
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
                    "changes_made": r.get("changes_made", ),
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
    
    def xǁMigrationContextǁto_dict__mutmut_30(self) -> Dict[str, Any]:
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
                    "changes_made": r.get("XXchanges_madeXX", []),
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
    
    def xǁMigrationContextǁto_dict__mutmut_31(self) -> Dict[str, Any]:
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
                    "changes_made": r.get("CHANGES_MADE", []),
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
    
    def xǁMigrationContextǁto_dict__mutmut_32(self) -> Dict[str, Any]:
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
                    "XXfile_typeXX": r.get("file_type"),
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
    
    def xǁMigrationContextǁto_dict__mutmut_33(self) -> Dict[str, Any]:
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
                    "FILE_TYPE": r.get("file_type"),
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
    
    def xǁMigrationContextǁto_dict__mutmut_34(self) -> Dict[str, Any]:
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
                    "file_type": r.get(None),
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
    
    def xǁMigrationContextǁto_dict__mutmut_35(self) -> Dict[str, Any]:
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
                    "file_type": r.get("XXfile_typeXX"),
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
    
    def xǁMigrationContextǁto_dict__mutmut_36(self) -> Dict[str, Any]:
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
                    "file_type": r.get("FILE_TYPE"),
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
    
    def xǁMigrationContextǁto_dict__mutmut_37(self) -> Dict[str, Any]:
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
            "XXvalidation_resultsXX": self.validation_results,
            "repair_history": {
                path: [
                    {"success": a.get("success"), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_38(self) -> Dict[str, Any]:
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
            "VALIDATION_RESULTS": self.validation_results,
            "repair_history": {
                path: [
                    {"success": a.get("success"), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_39(self) -> Dict[str, Any]:
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
            "XXrepair_historyXX": {
                path: [
                    {"success": a.get("success"), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_40(self) -> Dict[str, Any]:
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
            "REPAIR_HISTORY": {
                path: [
                    {"success": a.get("success"), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_41(self) -> Dict[str, Any]:
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
                    {"XXsuccessXX": a.get("success"), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_42(self) -> Dict[str, Any]:
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
                    {"SUCCESS": a.get("success"), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_43(self) -> Dict[str, Any]:
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
                    {"success": a.get(None), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_44(self) -> Dict[str, Any]:
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
                    {"success": a.get("XXsuccessXX"), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_45(self) -> Dict[str, Any]:
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
                    {"success": a.get("SUCCESS"), "issues_fixed": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_46(self) -> Dict[str, Any]:
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
                    {"success": a.get("success"), "XXissues_fixedXX": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_47(self) -> Dict[str, Any]:
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
                    {"success": a.get("success"), "ISSUES_FIXED": a.get("issues_fixed", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_48(self) -> Dict[str, Any]:
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
                    {"success": a.get("success"), "issues_fixed": a.get(None, [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_49(self) -> Dict[str, Any]:
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
                    {"success": a.get("success"), "issues_fixed": a.get("issues_fixed", None)}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_50(self) -> Dict[str, Any]:
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
                    {"success": a.get("success"), "issues_fixed": a.get([])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_51(self) -> Dict[str, Any]:
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
                    {"success": a.get("success"), "issues_fixed": a.get("issues_fixed", )}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_52(self) -> Dict[str, Any]:
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
                    {"success": a.get("success"), "issues_fixed": a.get("XXissues_fixedXX", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    def xǁMigrationContextǁto_dict__mutmut_53(self) -> Dict[str, Any]:
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
                    {"success": a.get("success"), "issues_fixed": a.get("ISSUES_FIXED", [])}
                    for a in attempts
                ]
                for path, attempts in self.repair_history.items()
            },
        }
    
    xǁMigrationContextǁto_dict__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁMigrationContextǁto_dict__mutmut_1': xǁMigrationContextǁto_dict__mutmut_1, 
        'xǁMigrationContextǁto_dict__mutmut_2': xǁMigrationContextǁto_dict__mutmut_2, 
        'xǁMigrationContextǁto_dict__mutmut_3': xǁMigrationContextǁto_dict__mutmut_3, 
        'xǁMigrationContextǁto_dict__mutmut_4': xǁMigrationContextǁto_dict__mutmut_4, 
        'xǁMigrationContextǁto_dict__mutmut_5': xǁMigrationContextǁto_dict__mutmut_5, 
        'xǁMigrationContextǁto_dict__mutmut_6': xǁMigrationContextǁto_dict__mutmut_6, 
        'xǁMigrationContextǁto_dict__mutmut_7': xǁMigrationContextǁto_dict__mutmut_7, 
        'xǁMigrationContextǁto_dict__mutmut_8': xǁMigrationContextǁto_dict__mutmut_8, 
        'xǁMigrationContextǁto_dict__mutmut_9': xǁMigrationContextǁto_dict__mutmut_9, 
        'xǁMigrationContextǁto_dict__mutmut_10': xǁMigrationContextǁto_dict__mutmut_10, 
        'xǁMigrationContextǁto_dict__mutmut_11': xǁMigrationContextǁto_dict__mutmut_11, 
        'xǁMigrationContextǁto_dict__mutmut_12': xǁMigrationContextǁto_dict__mutmut_12, 
        'xǁMigrationContextǁto_dict__mutmut_13': xǁMigrationContextǁto_dict__mutmut_13, 
        'xǁMigrationContextǁto_dict__mutmut_14': xǁMigrationContextǁto_dict__mutmut_14, 
        'xǁMigrationContextǁto_dict__mutmut_15': xǁMigrationContextǁto_dict__mutmut_15, 
        'xǁMigrationContextǁto_dict__mutmut_16': xǁMigrationContextǁto_dict__mutmut_16, 
        'xǁMigrationContextǁto_dict__mutmut_17': xǁMigrationContextǁto_dict__mutmut_17, 
        'xǁMigrationContextǁto_dict__mutmut_18': xǁMigrationContextǁto_dict__mutmut_18, 
        'xǁMigrationContextǁto_dict__mutmut_19': xǁMigrationContextǁto_dict__mutmut_19, 
        'xǁMigrationContextǁto_dict__mutmut_20': xǁMigrationContextǁto_dict__mutmut_20, 
        'xǁMigrationContextǁto_dict__mutmut_21': xǁMigrationContextǁto_dict__mutmut_21, 
        'xǁMigrationContextǁto_dict__mutmut_22': xǁMigrationContextǁto_dict__mutmut_22, 
        'xǁMigrationContextǁto_dict__mutmut_23': xǁMigrationContextǁto_dict__mutmut_23, 
        'xǁMigrationContextǁto_dict__mutmut_24': xǁMigrationContextǁto_dict__mutmut_24, 
        'xǁMigrationContextǁto_dict__mutmut_25': xǁMigrationContextǁto_dict__mutmut_25, 
        'xǁMigrationContextǁto_dict__mutmut_26': xǁMigrationContextǁto_dict__mutmut_26, 
        'xǁMigrationContextǁto_dict__mutmut_27': xǁMigrationContextǁto_dict__mutmut_27, 
        'xǁMigrationContextǁto_dict__mutmut_28': xǁMigrationContextǁto_dict__mutmut_28, 
        'xǁMigrationContextǁto_dict__mutmut_29': xǁMigrationContextǁto_dict__mutmut_29, 
        'xǁMigrationContextǁto_dict__mutmut_30': xǁMigrationContextǁto_dict__mutmut_30, 
        'xǁMigrationContextǁto_dict__mutmut_31': xǁMigrationContextǁto_dict__mutmut_31, 
        'xǁMigrationContextǁto_dict__mutmut_32': xǁMigrationContextǁto_dict__mutmut_32, 
        'xǁMigrationContextǁto_dict__mutmut_33': xǁMigrationContextǁto_dict__mutmut_33, 
        'xǁMigrationContextǁto_dict__mutmut_34': xǁMigrationContextǁto_dict__mutmut_34, 
        'xǁMigrationContextǁto_dict__mutmut_35': xǁMigrationContextǁto_dict__mutmut_35, 
        'xǁMigrationContextǁto_dict__mutmut_36': xǁMigrationContextǁto_dict__mutmut_36, 
        'xǁMigrationContextǁto_dict__mutmut_37': xǁMigrationContextǁto_dict__mutmut_37, 
        'xǁMigrationContextǁto_dict__mutmut_38': xǁMigrationContextǁto_dict__mutmut_38, 
        'xǁMigrationContextǁto_dict__mutmut_39': xǁMigrationContextǁto_dict__mutmut_39, 
        'xǁMigrationContextǁto_dict__mutmut_40': xǁMigrationContextǁto_dict__mutmut_40, 
        'xǁMigrationContextǁto_dict__mutmut_41': xǁMigrationContextǁto_dict__mutmut_41, 
        'xǁMigrationContextǁto_dict__mutmut_42': xǁMigrationContextǁto_dict__mutmut_42, 
        'xǁMigrationContextǁto_dict__mutmut_43': xǁMigrationContextǁto_dict__mutmut_43, 
        'xǁMigrationContextǁto_dict__mutmut_44': xǁMigrationContextǁto_dict__mutmut_44, 
        'xǁMigrationContextǁto_dict__mutmut_45': xǁMigrationContextǁto_dict__mutmut_45, 
        'xǁMigrationContextǁto_dict__mutmut_46': xǁMigrationContextǁto_dict__mutmut_46, 
        'xǁMigrationContextǁto_dict__mutmut_47': xǁMigrationContextǁto_dict__mutmut_47, 
        'xǁMigrationContextǁto_dict__mutmut_48': xǁMigrationContextǁto_dict__mutmut_48, 
        'xǁMigrationContextǁto_dict__mutmut_49': xǁMigrationContextǁto_dict__mutmut_49, 
        'xǁMigrationContextǁto_dict__mutmut_50': xǁMigrationContextǁto_dict__mutmut_50, 
        'xǁMigrationContextǁto_dict__mutmut_51': xǁMigrationContextǁto_dict__mutmut_51, 
        'xǁMigrationContextǁto_dict__mutmut_52': xǁMigrationContextǁto_dict__mutmut_52, 
        'xǁMigrationContextǁto_dict__mutmut_53': xǁMigrationContextǁto_dict__mutmut_53
    }
    xǁMigrationContextǁto_dict__mutmut_orig.__name__ = 'xǁMigrationContextǁto_dict'
