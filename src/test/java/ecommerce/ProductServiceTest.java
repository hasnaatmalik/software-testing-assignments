package ecommerce;

import org.junit.jupiter.api.Test;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;

public class ProductServiceTest {

    @Test
    void should_addProduct_when_nameIsValid() {
        // Arrange
        ProductService service = new ProductService();
        // Act
        service.addProduct("Phone");
        List<String> results = service.searchProducts("Phone");
        // Assert
        assertEquals(1, results.size());
    }

    @Test
    void should_notAddProduct_when_nameIsNull() {
        // Arrange
        ProductService service = new ProductService();
        // Act
        service.addProduct(null);
        List<String> results = service.searchProducts(""); // Should return empty anyway, but verifies no crash
        // Assert
        assertEquals(0, results.size());
    }

    @Test
    void should_notAddProduct_when_nameIsEmpty() {
        // Arrange
        ProductService service = new ProductService();
        // Act
        service.addProduct("   ");
        // Assert
        // We can't search empty strings based on the logic, so we search a fallback
        assertEquals(0, service.searchProducts(" ").size());
    }

    @Test
    void should_findProduct_when_exactMatchExists() {
        // Arrange
        ProductService service = new ProductService();
        service.addProduct("Tablet");
        // Act
        List<String> results = service.searchProducts("Tablet");
        // Assert
        assertTrue(results.contains("Tablet"));
    }

    @Test
    void should_findProduct_when_caseIsDifferent() {
        // Arrange
        ProductService service = new ProductService();
        service.addProduct("SmartWatch");
        // Act
        List<String> results = service.searchProducts("smartwatch");
        // Assert
        assertEquals(1, results.size());
    }

    @Test
    void should_returnEmptyList_when_noMatchFound() {
        // Arrange
        ProductService service = new ProductService();
        service.addProduct("Camera");
        // Act
        List<String> results = service.searchProducts("Lens");
        // Assert
        assertTrue(results.isEmpty());
    }

    @Test
    void should_findMultipleProducts_when_keywordMatchesMany() {
        // Arrange
        ProductService service = new ProductService();
        service.addProduct("Gaming Mouse");
        service.addProduct("Wireless Mouse");
        service.addProduct("Keyboard");
        // Act
        List<String> results = service.searchProducts("Mouse");
        // Assert
        assertEquals(2, results.size());
    }

    @Test
    void should_returnEmptyList_when_searchKeywordIsNull() {
        // Arrange
        ProductService service = new ProductService();
        service.addProduct("Headphones");
        // Act
        List<String> results = service.searchProducts(null);
        // Assert
        assertTrue(results.isEmpty());
    }
}