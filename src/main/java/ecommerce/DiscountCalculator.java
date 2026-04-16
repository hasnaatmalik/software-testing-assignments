package ecommerce;

public class DiscountCalculator {
    public double calculateFinalPrice(double originalPrice, double discountPercentage) {
        if (originalPrice < 0 || discountPercentage < 0 || discountPercentage > 100) {
            throw new IllegalArgumentException("Invalid price or discount");
        }
        double discountAmount = originalPrice * (discountPercentage / 100);
        return originalPrice - discountAmount;
    }
}