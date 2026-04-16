# Test Strategy Document

## 1. UserService
* **Functional Area:** Validates user inputs (emails) and formats profile data (usernames).
* **Risk Zones:** Null pointer exceptions from uninitialized strings; malformed email bypasses.
* **Edge Cases:** Empty strings, strings with only spaces, emails missing domains, uppercase names.

## 2. DiscountCalculator
* **Functional Area:** Processes financial calculations for shopping cart totals.
* **Risk Zones:** Negative price outputs, divide-by-zero errors, precision loss with floating-point math.
* **Edge Cases:** 0% discount, 100% discount, original price of $0.00.

## 3. InventoryManager
* **Functional Area:** Manages warehouse stock states using in-memory data structures.
* **Risk Zones:** Over-drafting stock (negative inventory), concurrent modification issues, null item keys.
* **Edge Cases:** Reducing exactly the amount of stock available (boundary), adding 0 quantity.

## 4. ProductService
* **Functional Area:** Maintains product catalogs and handles text-based search filtering.
* **Risk Zones:** Case-sensitive search failures, null keyword crashes, adding blank products.
* **Edge Cases:** Searching with a keyword that matches all products, searching with a completely empty string or null.