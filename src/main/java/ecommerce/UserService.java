package ecommerce;

public class UserService {
    public boolean isValidEmail(String email) {
        if (email == null || email.isEmpty()) {
            return false;
        }
        // Added checks for spaces and prefix existence
        return email.contains("@") &&
                email.endsWith(".com") &&
                !email.contains(" ") &&
                !email.startsWith("@");
    }

    public String formatUsername(String firstName, String lastName) {
        if (firstName == null || lastName == null) {
            throw new IllegalArgumentException("Names cannot be null");
        }
        return firstName.trim().toLowerCase() + "_" + lastName.trim().toLowerCase();
    }
}