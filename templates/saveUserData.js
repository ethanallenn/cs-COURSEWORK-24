const express = require('express');
const bodyParser = require('body-parser');
const saveUserData = require('./templates/saveUserData');

const app = express();
const port = 3000;

// Middleware to parse form data
app.use(bodyParser.urlencoded({ extended: true }));

// Serve the add_user_form.html file
app.get('/', (req, res) => {
    res.sendFile('/Users/ethanallen/Documents/A2_CourseworkProject/templates/add_user_form.html');
});

// Handle form submission
app.post('/submit', (req, res) => {
    const userData = {
        name: req.body.name,
        email: req.body.email,
        age: parseInt(req.body.age, 10)
    };

    saveUserData(userData);

    res.send(`
        <html>
            <body>
                <h1>User data saved successfully!</h1>
                <p>Name: ${userData.name}</p>
                <p>Email: ${userData.email}</p>
                <p>Age: ${userData.age}</p>
                <button onclick="window.location.href='/login_view.html'">Return to Login</button>
            </body>
        </html>
    `);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
