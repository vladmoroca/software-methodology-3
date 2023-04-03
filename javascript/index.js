const express = require('express');
const app = express();

app.get('/', (req, res) => res.json('Hello World!'))

app.listen(3033, () => {
    console.log('server started on port 3033!');
})