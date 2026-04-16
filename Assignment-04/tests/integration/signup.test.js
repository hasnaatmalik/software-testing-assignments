// tests/integration/signup.test.js
require('chromedriver');
const { Builder } = require('selenium-webdriver');
const expect = require('chai').expect;
const SignupPage = require('../pages/SignupPage');

describe('Signup UI Integration Tests', function () {
    let driver;
    let signupPage;

    before(async function () {
        driver = await new Builder().forBrowser('chrome').build();
        signupPage = new SignupPage(driver);
    });

    after(async function () {
        await driver.quit();
    });

    it('should display error for missing fields', async function () {
        await signupPage.navigate();
        await signupPage.submit(); // submit empty form
        
        const error = await signupPage.getErrorMessage();
        // The first validation check in our backend is Username
        expect(error).to.include('Username must be at least 3 characters');
    });

    it('should display error for short username', async function () {
        await signupPage.navigate();
        await signupPage.fillForm('ab', 'test@test.com', 'password123');
        await signupPage.submit();
        
        const error = await signupPage.getErrorMessage();
        expect(error).to.include('Username must be at least 3 characters');
    });

    it('should display error for invalid email', async function () {
        await signupPage.navigate();
        await signupPage.fillForm('validuser', 'invalidemail', 'password123');
        await signupPage.submit();
        
        const error = await signupPage.getErrorMessage();
        expect(error).to.include('Invalid email format');
    });

    it('should display error for short password', async function () {
        await signupPage.navigate();
        await signupPage.fillForm('validuser', 'test@example.com', '123');
        await signupPage.submit();
        
        const error = await signupPage.getErrorMessage();
        expect(error).to.include('Password must be at least 6 characters');
    });

    it('should successfully register a valid user', async function () {
        const uniqueEmail = `newuser${Date.now()}@example.com`;
        await signupPage.navigate();
        await signupPage.fillForm('newvaliduser', uniqueEmail, 'password1234');
        await signupPage.submit();
        
        const success = await signupPage.getSuccessMessage();
        expect(success).to.include('Registration successful');
    });

    it('should display error for duplicate email', async function () {
        const duplicateEmail = `dupuser${Date.now()}@example.com`;
        
        // Register first time
        await signupPage.navigate();
        await signupPage.fillForm('user1', duplicateEmail, 'password1234');
        await signupPage.submit();
        await signupPage.getSuccessMessage(); // Wait for server to process it
        
        // Try to register again with same email
        await signupPage.navigate();
        await signupPage.fillForm('user2', duplicateEmail, 'password1234');
        await signupPage.submit();

        const error = await signupPage.getErrorMessage();
        expect(error).to.include('User already exists with this email');
    });
});
