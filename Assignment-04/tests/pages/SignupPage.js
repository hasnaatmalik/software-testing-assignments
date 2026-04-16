// tests/pages/SignupPage.js
const { By, until } = require('selenium-webdriver');

class SignupPage {
    constructor(driver) {
        this.driver = driver;
        this.usernameInput = By.id('username');
        this.emailInput = By.id('email');
        this.passwordInput = By.id('password');
        this.submitButton = By.id('signupBtn');
        this.errorMessage = By.id('error-msg');
        this.successMessage = By.id('success-msg');
    }

    async navigate() {
        await this.driver.get('http://localhost:3000/signup');
    }

    async enterUsername(username) {
        if (username !== undefined) {
            await this.driver.findElement(this.usernameInput).sendKeys(username);
        }
    }

    async enterEmail(email) {
        if (email !== undefined) {
            await this.driver.findElement(this.emailInput).sendKeys(email);
        }
    }

    async enterPassword(password) {
        if (password !== undefined) {
            await this.driver.findElement(this.passwordInput).sendKeys(password);
        }
    }

    async fillForm(username, email, password) {
        await this.enterUsername(username);
        await this.enterEmail(email);
        await this.enterPassword(password);
    }

    async submit() {
        await this.driver.findElement(this.submitButton).click();
    }

    async getErrorMessage() {
        try {
            let errorElement = await this.driver.wait(until.elementLocated(this.errorMessage), 3000);
            return await errorElement.getText();
        } catch (error) {
            return null; // Return null if element is not found within timeout
        }
    }

    async getSuccessMessage() {
        try {
            let successElement = await this.driver.wait(until.elementLocated(this.successMessage), 3000);
            return await successElement.getText();
        } catch (error) {
            return null;
        }
    }
}
module.exports = SignupPage;
