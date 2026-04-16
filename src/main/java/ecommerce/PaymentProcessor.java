package ecommerce;

public class PaymentProcessor {
    public boolean processPayment(double amount, String method) {
        if (amount <= 0) {
            return false; // Payment failed
        }
        // Pretend we do external API calls here
        return method.equalsIgnoreCase("CREDIT_CARD") || method.equalsIgnoreCase("PAYPAL");
    }
}