package ecommerce;
import java.util.ArrayList;
import java.util.List;

public class ProductService {
    private List<String> products = new ArrayList<>();

    public void addProduct(String productName) {
        if (productName != null && !productName.trim().isEmpty()) {
            products.add(productName);
        }
    }

    public List<String> searchProducts(String keyword) {
        List<String> results = new ArrayList<>();
        if (keyword == null || keyword.isEmpty()) return results;

        for (String product : products) {
            if (product.toLowerCase().contains(keyword.toLowerCase())) {
                results.add(product);
            }
        }
        return results;
    }
}