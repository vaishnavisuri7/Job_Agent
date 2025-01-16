import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration, withEventReplay } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { LandingPageComponent } from './components/landing-page/landing-page.component';
import { PreparationComponent } from './components/preparation/preparation.component';

@NgModule({
  declarations: [
    AppComponent,
    LandingPageComponent,
    PreparationComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [
    provideClientHydration(withEventReplay()),
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
