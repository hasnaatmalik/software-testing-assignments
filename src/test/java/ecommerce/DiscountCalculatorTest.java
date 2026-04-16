package ecommerce;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.TestMethodOrder;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class DiscountCalculatorTest {

    @Test
    @Order(1)
    void should_calculateCorrectPrice_when_validInputsProvided() {
        // Arrange
        DiscountCalculator calc = new DiscountCalculator();
        // Act
        double result = calc.calculateFinalPrice(100.0, 20.0);
        // Assert
        assertEquals(80.0, result);
    }

    @Test
    @Order(2)
    void should_returnOriginalPrice_when_discountIsZero() {
        // Arrange
        DiscountCalculator calc = new DiscountCalculator();
        // Act
        double result = calc.calculateFinalPrice(50.0, 0.0);
        // Assert
        assertEquals(50.0, result);
    }

    @Test
    @Order(3)
    void should_returnZero_when_discountIsOneHundred() {
        // Arrange
        DiscountCalculator calc = new DiscountCalculator();
        // Act
        double result = calc.calculateFinalPrice(75.0, 100.0);
        // Assert
        assertEquals(0.0, result);
    }

    @Test
    void should_throwException_when_priceIsNegative() {
        // Arrange
        DiscountCalculator calc = new DiscountCalculator();
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            calc.calculateFinalPrice(-10.0, 10.0);
        });
    }

    @Test
    void should_throwException_when_discountIsNegative() {
        // Arrange
        DiscountCalculator calc = new DiscountCalculator();
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            calc.calculateFinalPrice(100.0, -5.0);
        });
    }

    @Test
    void should_throwException_when_discountIsGreaterThanOneHundred() {
        // Arrange
        DiscountCalculator calc = new DiscountCalculator();
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            calc.calculateFinalPrice(100.0, 105.0);
        });
    }

    @Test
    void should_returnZero_when_originalPriceIsZero() {
        // Arrange
        DiscountCalculator calc = new DiscountCalculator();
        // Act
        double result = calc.calculateFinalPrice(0.0, 20.0);
        // Assert
        assertEquals(0.0, result);
    }

    @Test
    void should_calculateCorrectly_when_priceHasDecimals() {
        // Arrange
        DiscountCalculator calc = new DiscountCalculator();
        // Act
        double result = calc.calculateFinalPrice(10.50, 50.0);
        // Assert
        assertEquals(5.25, result);
    }
}