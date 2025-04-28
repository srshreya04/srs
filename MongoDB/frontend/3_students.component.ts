// frontend/src/app/students/students.component.ts

import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { StudentService } from '../student.service';

@Component({
  selector: 'app-students',
  standalone: true, // <<< Important
  imports: [CommonModule, FormsModule], // <<< Important
  templateUrl: './students.component.html',
  styleUrls: ['./students.component.css']
})
export class StudentsComponent implements OnInit {
  students: any[] = [];
  student = { name: '', email: '', course: '' };
  editingId: string | null = null;

  constructor(private studentService: StudentService) { }

  ngOnInit() {
    this.loadStudents();
  }

  loadStudents() {
    this.studentService.getStudents().then(response => {
      this.students = response.data;
    });
  }

  saveStudent() {
    if (this.editingId) {
      this.studentService.updateStudent(this.editingId, this.student).then(() => {
        this.loadStudents();
        this.cancelEdit();
      });
    } else {
      this.studentService.createStudent(this.student).then(() => {
        this.loadStudents();
        this.student = { name: '', email: '', course: '' };
      });
    }
  }

  editStudent(student: any) {
    this.student = { ...student };
    this.editingId = student._id;
  }

  cancelEdit() {
    this.editingId = null;
    this.student = { name: '', email: '', course: '' };
  }

  deleteStudent(id: string) {
    this.studentService.deleteStudent(id).then(() => {
      this.loadStudents();
    });
  }
}
