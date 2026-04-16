package ecommerce;

import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.CsvFileSource;
import org.junit.jupiter.params.provider.MethodSource;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Tag;

@Tag("slow")
public class DataDrivenTests {

    // ==========================================
    // 1. CSV Data-Driven Test (UserService)
    // ==========================================
    @ParameterizedTest(name = "[{index}] Email: {0} -> Expected: {1}")
    @CsvFileSource(resources = "/email_data.csv", numLinesToSkip = 1)
    void should_validateEmail_usingCsvData(String email, boolean expectedResult) {
        UserService service = new UserService();
        assertEquals(expectedResult, service.isValidEmail(email));
    }

    // ==========================================
    // 2. Excel Data-Driven Test (DiscountCalculator)
    // ==========================================
    @ParameterizedTest(name = "[{index}] {0} - Price: {1}, Discount: {2}")
    @MethodSource("excelDataProvider")
    void should_calculateDiscount_usingExcelData(String category, double price, double discount, double expected, boolean expectException) {
        DiscountCalculator calc = new DiscountCalculator();

        if (expectException) {
            // Invalid data should trigger our IllegalArgumentException
            assertThrows(IllegalArgumentException.class, () -> calc.calculateFinalPrice(price, discount));
        } else {
            // Valid, Edge, and Stress data should calculate correctly
            // Delta of 0.01 is used to handle floating-point math precision
            assertEquals(expected, calc.calculateFinalPrice(price, discount), 0.01);
        }
    }

    // ==========================================
    // Helper Method: Parse Excel and Feed to JUnit
    // ==========================================
    public static Stream<Arguments> excelDataProvider() throws Exception {
        List<Arguments> arguments = new ArrayList<>();

        // Load the Excel file from src/test/resources
        try (InputStream is = DataDrivenTests.class.getResourceAsStream("/discount_data.xlsx");
             Workbook workbook = new XSSFWorkbook(is)) {

            Sheet sheet = workbook.getSheetAt(0);

            // Start at index 1 to skip the header row
            for (int i = 1; i <= sheet.getLastRowNum(); i++) {
                Row row = sheet.getRow(i);
                if (row == null) continue;

                // Read cells based on column layout
                String category = row.getCell(0).getStringCellValue();
                double price = row.getCell(1).getNumericCellValue();
                double discount = row.getCell(2).getNumericCellValue();
                double expected = row.getCell(3).getNumericCellValue();
                boolean expectException = row.getCell(4).getBooleanCellValue();

                arguments.add(Arguments.of(category, price, discount, expected, expectException));
            }
        }
        return arguments.stream();
    }
}