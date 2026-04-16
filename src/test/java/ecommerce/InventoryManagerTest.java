package ecommerce;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class InventoryManagerTest {

    @Test
    void should_increaseStock_when_validQuantityAdded() {
        // Arrange
        InventoryManager manager = new InventoryManager();
        // Act
        manager.addStock("Laptop", 10);
        // Assert
        assertTrue(manager.hasSufficientStock("Laptop", 5));
    }

    @Test
    void should_throwException_when_addingNegativeQuantity() {
        // Arrange
        InventoryManager manager = new InventoryManager();
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            manager.addStock("Mouse", -5);
        });
    }

    @Test
    void should_throwException_when_addingZeroQuantity() {
        // Arrange
        InventoryManager manager = new InventoryManager();
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            manager.addStock("Keyboard", 0);
        });
    }

    @Test
    void should_returnTrue_when_stockIsExactMatch() {
        // Arrange
        InventoryManager manager = new InventoryManager();
        manager.addStock("Monitor", 2);
        // Act
        boolean result = manager.hasSufficientStock("Monitor", 2);
        // Assert
        assertTrue(result);
    }

    @Test
    void should_returnFalse_when_stockIsInsufficient() {
        // Arrange
        InventoryManager manager = new InventoryManager();
        manager.addStock("Desk", 1);
        // Act
        boolean result = manager.hasSufficientStock("Desk", 5);
        // Assert
        assertFalse(result);
    }

    @Test
    void should_reduceStock_when_quantityIsValid() {
        // Arrange
        InventoryManager manager = new InventoryManager();
        manager.addStock("Chair", 10);
        // Act
        manager.reduceStock("Chair", 3);
        // Assert
        assertTrue(manager.hasSufficientStock("Chair", 7));
        assertFalse(manager.hasSufficientStock("Chair", 8));
    }

    @Test
    void should_throwException_when_reducingMoreThanAvailable() {
        // Arrange
        InventoryManager manager = new InventoryManager();
        manager.addStock("Cable", 5);
        // Act & Assert
        assertThrows(IllegalStateException.class, () -> {
            manager.reduceStock("Cable", 10);
        });
    }

    @Test
    void should_handleMultipleItems_when_addingDifferentProducts() {
        // Arrange
        InventoryManager manager = new InventoryManager();
        // Act
        manager.addStock("ItemA", 5);
        manager.addStock("ItemB", 10);
        // Assert
        assertTrue(manager.hasSufficientStock("ItemA", 5));
        assertTrue(manager.hasSufficientStock("ItemB", 10));
    }
}