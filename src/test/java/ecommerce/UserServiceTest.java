package ecommerce;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class UserServiceTest {

    @Test
    void should_returnTrue_when_emailIsValid() {
        // Arrange
        UserService userService = new UserService();
        String validEmail = "student@fast.com";

        // Act
        boolean result = userService.isValidEmail(validEmail);

        // Assert
        assertTrue(result, "The email should be considered valid.");
    }
}