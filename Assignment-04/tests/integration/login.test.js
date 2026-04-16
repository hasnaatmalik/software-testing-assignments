// tests/integration/login.test.js
require('chromedriver'); // <-- ADD THIS LINE
const { Builder } = require('selenium-webdriver');
const expect = require('chai').expect;
const LoginPage = require('../pages/LoginPage');


describe('Login UI Integration Tests', function () {
    let driver;
    let loginPage;

    before(async function () {
        // Setup Chrome driver
        driver = await new Builder().forBrowser('chrome').build();
        loginPage = new LoginPage(driver);
    });

    after(async function () {
        await driver.quit();
    });

    it('should display error for invalid email format', async function () {
        await loginPage.navigate();
        await loginPage.enterEmail('invalid-email');
        await loginPage.enterPassword('password123');
        await loginPage.submit();

        const error = await loginPage.getErrorMessage();
        expect(error).to.include('Invalid email');
    });

    it('should display error for non-existing user', async function () {
        await loginPage.navigate();
        await loginPage.enterEmail('nonexistent@example.com');
        await loginPage.enterPassword('password123');
        await loginPage.submit();

        const error = await loginPage.getErrorMessage();
        expect(error).to.include('User not found');
    });

    it('should display error for empty form submission', async function () {
        await loginPage.navigate();
        await loginPage.submit();

        const error = await loginPage.getErrorMessage();
        expect(error).to.include('Invalid email format'); // The first validation that fails
    });

    // To test valid login, we first need to register a user.
    // We'll test this flow sequentially.
    describe('Valid User Flow', function() {
        it('should successfully register a test user for login testing', async function() {
            await driver.get('http://localhost:3000/signup');
            await driver.findElement(require('selenium-webdriver').By.id('username')).sendKeys('logintest');
            await driver.findElement(require('selenium-webdriver').By.id('email')).sendKeys('login@test.com');
            await driver.findElement(require('selenium-webdriver').By.id('password')).sendKeys('password123');
            await driver.findElement(require('selenium-webdriver').By.id('signupBtn')).click();
            
            const successMsg = await driver.findElement(require('selenium-webdriver').By.id('success-msg')).getText();
            expect(successMsg).to.include('Registration successful');
        });

        it('should display error for wrong password', async function () {
            await loginPage.navigate();
            await loginPage.enterEmail('login@test.com');
            await loginPage.enterPassword('wrongpassword');
            await loginPage.submit();

            const error = await loginPage.getErrorMessage();
            expect(error).to.include('Incorrect password');
        });

        it('should login successfully with valid credentials', async function () {
            await loginPage.navigate();
            await loginPage.enterEmail('login@test.com');
            await loginPage.enterPassword('password123');
            await loginPage.submit();

            // Wait until navigating to dashboard and welcome message is present
            const welcomeElement = await driver.wait(require('selenium-webdriver').until.elementLocated(require('selenium-webdriver').By.id('welcome-msg')), 5000);
            const welcomeMsg = await welcomeElement.getText();
            expect(welcomeMsg).to.include('Welcome, logintest!');
        });
    });
});