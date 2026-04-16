// tests/pages/LoginPage.js
const { By, until } = require('selenium-webdriver');

class LoginPage {
    constructor(driver) {
        this.driver = driver;
        this.emailInput = By.id('email');
        this.passwordInput = By.id('password');
        this.submitButton = By.id('loginBtn');
        this.errorMessage = By.id('error-msg');
    }

    async navigate() {
        await this.driver.get('http://localhost:3000/login');
    }

    async enterEmail(email) {
        await this.driver.findElement(this.emailInput).sendKeys(email);
    }

    async enterPassword(password) {
        await this.driver.findElement(this.passwordInput).sendKeys(password);
    }

    async submit() {
        await this.driver.findElement(this.submitButton).click();
    }

    async getErrorMessage() {
        let errorElement = await this.driver.wait(until.elementLocated(this.errorMessage), 5000);
        return await errorElement.getText();
    }
}
module.exports = LoginPage;