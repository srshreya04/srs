// backend/server.js

const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

// Create App
const app = express();
app.use(cors());
app.use(express.json());

// MongoDB Connection
mongoose.connect('YOUR_MONGODB_CLOUD_URI_HERE', {
    dbName: 'db22510007',
}).then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

// Student Schema
const StudentSchema = new mongoose.Schema({
    name: String,
    email: String,
    course: String,
});

const Student = mongoose.model('Student', StudentSchema);

// CRUD APIs

// CREATE
app.post('/api/students', async (req, res) => {
    const student = new Student(req.body);
    await student.save();
    res.send(student);
});

// READ
app.get('/api/students', async (req, res) => {
    const students = await Student.find();
    res.send(students);
});

// UPDATE
app.put('/api/students/:id', async (req, res) => {
    const student = await Student.findByIdAndUpdate(req.params.id, req.body, { new: true });
    res.send(student);
});

// DELETE
app.delete('/api/students/:id', async (req, res) => {
    await Student.findByIdAndDelete(req.params.id);
    res.send({ message: 'Student Deleted' });
});

// Start Server
app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});
