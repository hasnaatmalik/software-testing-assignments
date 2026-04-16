# Assignment 3: Advanced JUnit 5 Automation Framework

This project contains the deliverables for **Assignment #03** of the Software Testing course. It demonstrates an industrial-grade testing framework engineered in Java 17 using JUnit 5, complete with parallel execution, data-driven testing, and JaCoCo coverage analysis.

## 🎯 Objectives Achieved
- **Environment Engineering:** Automated build tools configured with successful execution of core project tests.
- **Test Architecture:** Implementation of AAA (Arrange, Act, Assert) architecture across multiple custom E-commerce components.
- **Data-Driven Testing:** Integration of parameters via multiple dynamic sources (CSV and Excel formats via Apache POI).
- **Orchestration:** Parallel and deterministic test execution via suite groupings (`@Tag`) and Maven Surefire profiles.
- **Coverage:** Robust line and branch coverage analysis hitting >70% minimums across modules via JaCoCo.

---

## 📂 Project Structure

```text
Assignment-03/
├── Docs/
│   ├── TEST_STRATEGY.md      # Methodologies and edge cases identified
│   ├── Setup_Note.md         # Environment Setup & Maven specifics
│   └── Summary_Report.md     # Final assignment summary and evaluation report
├── Media/
│   └── Task-01_Setup_and_Initial_Build.mov # 3-5m Video recording demonstrating build and execution
├── src/
│   ├── main/                 # Core E-commerce logic (SUT)
│   └── test/                 # Test suites, DDT classes, and test data resources (CSV/Excel)
└── pom.xml                   # Maven project dependencies and plugin configurations
```

---

## ⚙️ Running the Project

Ensure you have **Java 17+** and **Maven** installed and configured on your system path.

### 1. Build and Run All Tests
```bash
mvn clean test
```

### 2. Generate Code Coverage Report
After executing the tests, JaCoCo will automatically output the HTML coverage reports here:
```bash
target/site/jacoco/index.html
```

### 3. Run Specific Suite (e.g., Fast Tests)
```bash
mvn test -Dgroups="fast"
```

---

## 📋 Task Checklist
- [x] **Task 1:** Project Acquisition, Setup, and Demonstration Video
- [x] **Task 2:** Test Design & Strategy (8-12 tests per class)
- [x] **Task 3:** Data-Driven Testing implementation (CSV + Excel)
- [x] **Task 4:** Test Configuration (Parallel + Groupings)
- [x] **Task 5:** Code Coverage Reporting (JaCoCo)

> Note: All code logic contained in `/src/main` is custom-built exclusively for this assignment to represent practical, interacting logic streams.
