// tests/unit/validation.test.js
const { expect } = require('chai');
const { validateEmail, validatePassword, validateUsername } = require('../../src/utils/validation');

describe('Validation Unit Tests', function() {

    describe('Email Validation', function() {
        it('should return true for valid email formats', function() {
            expect(validateEmail('test@example.com')).to.be.true;
            expect(validateEmail('user.name@domain.co')).to.be.true;
        });

        it('should return false if missing @ symbol', function() {
            expect(validateEmail('testexample.com')).to.be.false;
        });

        it('should return false if missing domain', function() {
            expect(validateEmail('test@.com')).to.be.false;
            expect(validateEmail('test@')).to.be.false;
        });

        it('should return false for empty email', function() {
            expect(validateEmail('')).to.be.false;
            expect(validateEmail(null)).to.be.false;
            expect(validateEmail(undefined)).to.be.false;
        });
    });

    describe('Password Validation', function() {
        it('should return true for valid password (>= 6 characters)', function() {
            expect(validatePassword('123456')).to.be.true;
            expect(validatePassword('password123')).to.be.true;
        });

        it('should return false for short password (< 6 characters)', function() {
            expect(validatePassword('12345')).to.be.false;
            expect(validatePassword('abc')).to.be.false;
        });

        it('should return false for empty password', function() {
            expect(validatePassword('')).to.be.false;
        });
    });

    describe('Username Validation', function() {
        it('should return true for valid username (>= 3 characters)', function() {
            expect(validateUsername('abc')).to.be.true;
            expect(validateUsername('johndoe')).to.be.true;
        });

        it('should return false for short username (< 3 characters)', function() {
            expect(validateUsername('ab')).to.be.false;
            expect(validateUsername('a')).to.be.false;
        });

        it('should return false for empty username', function() {
            expect(validateUsername('')).to.be.false;
        });
    });

});
