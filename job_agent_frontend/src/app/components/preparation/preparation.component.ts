import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';


@Component({
  selector: 'app-preparation',
  standalone: false,
  
  templateUrl: './preparation.component.html',
  styleUrl: './preparation.component.css'
})
export class PreparationComponent {
  role = '';
  topic = '';
  response: any;

  constructor(private apiService: ApiService) {}

  onSubmit() {
    const payload = { role: this.role, user_input: this.topic };
    this.apiService.generateQuestion(payload).subscribe(
      (data) => {
        this.response = data;
      },
      (error) => {
        console.error('Error fetching data', error);
      }
    );
  }

}
