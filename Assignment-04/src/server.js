const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// In-memory array acting as our "database" for testing purposes
const users = [];

// Configure Express to use EJS for rendering HTML
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '../views'));
app.use(bodyParser.urlencoded({ extended: true }));

const { validateEmail, validatePassword, validateUsername } = require('./utils/validation');

// --- ROUTES ---

// Redirect root to login
app.get('/', (req, res) => res.redirect('/login'));

app.get('/login', (req, res) => {
    res.render('login', { error: null });
});

app.get('/signup', (req, res) => {
    res.render('signup', { error: null, success: null });
});

// Signup Logic & Validation
app.post('/signup', (req, res) => {
    const { username, email, password } = req.body;

    if (!validateUsername(username)) {
        return res.render('signup', { error: 'Username must be at least 3 characters.', success: null });
    }
    if (!validateEmail(email)) {
        return res.render('signup', { error: 'Invalid email format.', success: null });
    }
    if (!validatePassword(password)) {
        return res.render('signup', { error: 'Password must be at least 6 characters.', success: null });
    }
    if (users.find(u => u.email === email)) {
        return res.render('signup', { error: 'User already exists with this email.', success: null });
    }

    // Save user and redirect with success message
    users.push({ username, email, password });
    res.render('signup', { error: null, success: 'Registration successful! You can now login.' });
});

// Login Logic & Validation
app.post('/login', (req, res) => {
    const { email, password } = req.body;

    if (!validateEmail(email)) {
        return res.render('login', { error: 'Invalid email format.' });
    }

    const user = users.find(u => u.email === email);
    if (!user) {
        return res.render('login', { error: 'User not found.' });
    }
    if (user.password !== password) {
        return res.render('login', { error: 'Incorrect password.' });
    }

    // Successful login
    res.render('dashboard', { username: user.username });
});

app.listen(PORT, () => {
    console.log(`Server running successfully on http://localhost:${PORT}`);
});