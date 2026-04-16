# Environment Setup Note

**Task 1 Deliverable**

The environment for this testing assignment was engineered on macOS using the following local stack configuration:

- **JDK Version:** Java 17 (Eclipse Temurin)
- **Build Tool:** Apache Maven 3.9+
- **IDE:** IntelliJ IDEA Community Edition
- **Testing Core:** JUnit Jupiter (JUnit 5)

## Actions Taken
1. Initialized a custom E-commerce Java project (SUT) with interacting classes (`UserService`, `DiscountCalculator`, `ProductService`, etc.) to isolate logic and avoid external dependency noise.
2. Formatted the `pom.xml` strictly to define dependencies for JUnit 5, Apache POI (for CSV/Excel testing), and JaCoCo.
3. Successfully executed the initial build using `mvn clean install` to automatically download the Maven dependencies.
4. Executed the initial suite using `mvn test` to ensure the surefire plugin intercepted the `*Test.java` files correctly without environment mismatch errors.

Please refer to the `Media/Task-01_Setup_and_Initial_Build.mov` video for a real-time demonstration of the repo acquisition and testing pipeline.
