// src/utils/validation.js

function validateEmail(email) {
    if (!email) return false;
    if (!email.includes('@')) return false;
    if (!email.includes('.')) return false;
    
    if (email.includes(' ')) return false;

    // Basic domain check to ensure characters exist after '.'
    const parts = email.split('@');
    if (parts.length !== 2) return false;
    
    const domainParts = parts[1].split('.');
    // Ensure there is a domain name (before '.') and a TLD (after '.')
    if (domainParts.length < 2 || domainParts[0].length === 0 || domainParts[1].length === 0) return false;

    return true;
}

function validatePassword(password) {
    if (!password) return false;
    if (password.length < 6) return false;
    return true;
}

function validateUsername(username) {
    if (!username) return false;
    if (username.length < 3) return false;
    return true;
}

module.exports = {
    validateEmail,
    validatePassword,
    validateUsername
};
