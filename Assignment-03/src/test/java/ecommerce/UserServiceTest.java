package ecommerce;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Tag;
@Tag("fast")
public class UserServiceTest {

    @Test
    void should_returnTrue_when_emailIsValid() {
        // Arrange
        UserService service = new UserService();
        // Act
        boolean result = service.isValidEmail("test@domain.com");
        // Assert
        assertTrue(result);
    }

    @Test
    void should_returnFalse_when_emailIsNull() {
        // Arrange
        UserService service = new UserService();
        // Act
        boolean result = service.isValidEmail(null);
        // Assert
        assertFalse(result);
    }

    @Test
    void should_returnFalse_when_emailIsEmpty() {
        // Arrange
        UserService service = new UserService();
        // Act
        boolean result = service.isValidEmail("");
        // Assert
        assertFalse(result);
    }

    @Test
    void should_returnFalse_when_emailLacksAtSymbol() {
        // Arrange
        UserService service = new UserService();
        // Act
        boolean result = service.isValidEmail("testdomain.com");
        // Assert
        assertFalse(result);
    }

    @Test
    void should_formatCorrectly_when_validNamesProvided() {
        // Arrange
        UserService service = new UserService();
        // Act
        String result = service.formatUsername("John", "Doe");
        // Assert
        assertEquals("john_doe", result);
    }

    @Test
    void should_throwException_when_firstNameIsNull() {
        // Arrange
        UserService service = new UserService();
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            service.formatUsername(null, "Doe");
        });
    }

    @Test
    void should_formatCorrectly_when_namesHaveTrailingSpaces() {
        // Arrange
        UserService service = new UserService();
        // Act
        String result = service.formatUsername(" Alice ", " Smith  ");
        // Assert
        assertEquals("alice_smith", result);
    }

    @Test
    void should_throwException_when_lastNameIsNull() {
        // Arrange
        UserService service = new UserService();
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            service.formatUsername("John", null);
        });
    }
}