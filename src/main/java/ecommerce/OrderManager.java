package ecommerce;

public class OrderManager {
    private InventoryManager inventoryManager;
    private PaymentProcessor paymentProcessor;

    public OrderManager(InventoryManager inventoryManager, PaymentProcessor paymentProcessor) {
        this.inventoryManager = inventoryManager;
        this.paymentProcessor = paymentProcessor;
    }

    public boolean placeOrder(String item, int quantity, double price, String paymentMethod) {
        if (!inventoryManager.hasSufficientStock(item, quantity)) {
            return false;
        }

        boolean paymentSuccess = paymentProcessor.processPayment(price * quantity, paymentMethod);
        if (paymentSuccess) {
            inventoryManager.reduceStock(item, quantity);
            return true;
        }

        return false;
    }
}