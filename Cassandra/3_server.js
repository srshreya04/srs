const express = require('express');
const cassandra = require('cassandra-driver');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

const app = express();
app.use(cors());
app.use(express.json());

// Cassandra Connection
const client = new cassandra.Client({
    contactPoints: ['127.0.0.1'],
    localDataCenter: 'datacenter1',
    keyspace: 'student',
});

// CRUD APIs

// CREATE
app.post('/api/students', async (req, res) => {
    const { name, email, course } = req.body;
    const id = uuidv4();
    const query = 'INSERT INTO students (id, name, email, course) VALUES (?, ?, ?, ?)';
    try {
        await client.execute(query, [id, name, email, course], { prepare: true });
        res.send({ id, name, email, course });
    } catch (err) {
        console.error(err);
        res.status(500).send('Error inserting student');
    }
});

// READ
app.get('/api/students', async (req, res) => {
    const query = 'SELECT * FROM students';
    try {
        const result = await client.execute(query);
        res.send(result.rows);
    } catch (err) {
        console.error(err);
        res.status(500).send('Error fetching students');
    }
});

// UPDATE
app.put('/api/students/:id', async (req, res) => {
    const { name, email, course } = req.body;
    const { id } = req.params;
    const query = 'UPDATE students SET name = ?, email = ?, course = ? WHERE id = ?';
    try {
        await client.execute(query, [name, email, course, id], { prepare: true });
        res.send({ id, name, email, course });
    } catch (err) {
        console.error(err);
        res.status(500).send('Error updating student');
    }
});

// DELETE
app.delete('/api/students/:id', async (req, res) => {
    const { id } = req.params;
    const query = 'DELETE FROM students WHERE id = ?';
    try {
        await client.execute(query, [id], { prepare: true });
        res.send({ message: 'Student Deleted' });
    } catch (err) {
        console.error(err);
        res.status(500).send('Error deleting student');
    }
});

// Start Server
app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
