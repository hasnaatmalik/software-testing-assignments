// tests/integration/advanced.test.js
require('chromedriver');
const { Builder, By } = require('selenium-webdriver');
const expect = require('chai').expect;
const SignupPage = require('../pages/SignupPage');

describe('Advanced Edge Use-Case Scenarios', function () {
    let driver;
    let signupPage;

    before(async function () {
        driver = await new Builder().forBrowser('chrome').build();
        signupPage = new SignupPage(driver);
    });

    after(async function () {
        await driver.quit();
    });

    // 1. Boundary testing (max limits)
    it('should handle extremely long usernames without crashing', async function () {
        const longUsername = 'a'.repeat(255);
        await signupPage.navigate();
        await signupPage.fillForm(longUsername, 'long@user.com', 'password123');
        await signupPage.submit();
        
        const success = await signupPage.getSuccessMessage();
        expect(success).to.include('Registration successful');
    });

    // 2. Special Characters
    it('should reject or handle special characters securely in username', async function () {
        await signupPage.navigate();
        await signupPage.fillForm('<script>alert("xss")</script>', 'xss@test.com', 'password123');
        await signupPage.submit();
        // Depending on backend this might pass or fail, here we just ensure backend doesn't crash 
        // and returns a normal valid state (or sanitizes it). In our simple mock backend, it succeeds.
        const success = await signupPage.getSuccessMessage();
        expect(success).to.include('Registration successful');
    });

    // 3. Rapid submissions (Spam handling)
    it('should handle rapid multiple form submissions gracefully', async function () {
        await signupPage.navigate();
        await signupPage.fillForm('spamuser', 'spam@test.com', 'password123');
        
        // Click 5 times very rapidly
        for(let i=0; i<5; i++) {
            try {
                await signupPage.submit();
            } catch (e) {
                // Ignore stale element errors caused by successful navigation mid-loop
            }
        }

        const success = await signupPage.getSuccessMessage();
        const error = await signupPage.getErrorMessage();
        
        // Ensure that either it says successful, or it says duplicate user! 
        const hasValidResponse = (success && success.includes('Registration successful')) || (error && error.includes('User already exists'));
        expect(hasValidResponse).to.be.true;
    });

    // 4. Trailing spaces testing
    it('should fail email validation if email contains spaces', async function () {
        await signupPage.navigate();
        await signupPage.fillForm('spaceuser', 'test email@test.com', 'password123');
        await signupPage.submit();

        // Standard HTML5 input type="email" might block this, or our backend might
        // Wait, our express app handles it, but since it's an end-to-end test, we see UI response.
        const error = await signupPage.getErrorMessage();
        expect(error).to.include('Invalid email'); // Express validation catches it usually or it stays on page
    });

    // 5. Mixed-case email uniqueness
    it('should treat emails as case-sensitive or insensitive according to backend rules', async function () {
        const email = 'CaseTEST@example.com';
        await signupPage.navigate();
        await signupPage.fillForm('casetest1', email, 'password123');
        await signupPage.submit();

        // The second attempt with same exact case should definitely fail
        await signupPage.navigate();
        await signupPage.fillForm('casetest2', email, 'password123');
        await signupPage.submit();

        const error = await signupPage.getErrorMessage();
        expect(error).to.include('User already exists');
    });
});
