import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-landing-page',
  standalone: false,
  
  templateUrl: './landing-page.component.html',
  styleUrl: './landing-page.component.css'
})
export class LandingPageComponent {
  backgroundImage = 'url(assets/landing_page_background.jpeg)';
  
  constructor(private router: Router) {}

  onGetStarted() {
    this.router.navigate(['/prep']);  // Navigate to the 'prep' path
  }

}
