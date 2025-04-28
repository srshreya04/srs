// frontend/src/app/student.service.ts

import { Injectable } from '@angular/core';
import axios from 'axios';

@Injectable({
  providedIn: 'root'
})
export class StudentService {
  baseUrl = 'http://localhost:3000/api/students';

  getStudents() {
    return axios.get(this.baseUrl);
  }

  createStudent(student: any) {
    return axios.post(this.baseUrl, student);
  }

  updateStudent(id: string, student: any) {
    return axios.put(`${this.baseUrl}/${id}`, student);
  }

  deleteStudent(id: string) {
    return axios.delete(`${this.baseUrl}/${id}`);
  }
}
