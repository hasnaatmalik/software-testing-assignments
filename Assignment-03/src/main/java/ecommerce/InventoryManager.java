package ecommerce;
import java.util.HashMap;
import java.util.Map;

public class InventoryManager {
    private Map<String, Integer> stock = new HashMap<>();

    public void addStock(String item, int quantity) {
        if (quantity <= 0) throw new IllegalArgumentException("Quantity must be positive");
        stock.put(item, stock.getOrDefault(item, 0) + quantity);
    }

    public boolean hasSufficientStock(String item, int requestedQuantity) {
        return stock.getOrDefault(item, 0) >= requestedQuantity;
    }

    public void reduceStock(String item, int quantity) {
        if (!hasSufficientStock(item, quantity)) {
            throw new IllegalStateException("Not enough stock");
        }
        stock.put(item, stock.get(item) - quantity);
    }
}