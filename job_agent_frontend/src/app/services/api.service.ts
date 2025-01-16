import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {

  private apiUrl = 'http://localhost:8000/generate/'; // URL of the FastAPI backend

  constructor(private http: HttpClient) {}

  generateQuestion(data: { role: string, user_input: string }): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }
}
