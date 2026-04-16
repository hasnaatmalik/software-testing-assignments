# Final Summary Report

## 1. Toolchain & Environment
- **Platform**: macOS
- **JDK**: Java 17
- **Runner**: Apache Maven
- **Test Framework**: JUnit 5 (Jupiter)
- **External Dependencies**: Apache POI (Excel/CSV manipulation), JaCoCo (Coverage Analysis)

## 2. Test Strategy Overview
The architecture was strictly modularized. The primary focus was asserting the Arrange-Act-Assert (AAA) syntax to prevent brittle test structures.
- **Positive & Negative Scenarios:** Verified valid constraints and explicitly handled invalid structures via `assertThrows`.
- **Edge Conditions:** Validated extreme boundaries, especially in numeric processors (`DiscountCalculator`) and null-safety collections (`ProductService`).

## 3. Coverage Analysis
JaCoCo was utilized entirely from the command line interface without IDE crutches. The build pipeline outputs HTML traces into `target/site/jacoco`.
- **Target Coverage:** > 70%
- **Actual Coverage:** *(Fill in final coverage numbers here after analyzing the final JaCoCo report)*

## 4. Challenges Faced
- Configuring the Maven Surefire plugin to run specific JUnit suites concurrently and correctly map `junit-platform.properties`.
- Injecting raw arguments via `@MethodSource` correctly matching method signatures for parameterized tests.

## 5. Contribution Breakdown
- **Muhammad Hasnaat Raza:** Sole Contributor (Custom Application Development, Infrastructure Setup, Data-Driven Tests, JaCoCo pipelines).
