// Die index.js in React ist der Haupteinstiegspunkt in die Anwendung. Die Datei importiert die
// notwendigen Bibliotheken und Komponenten, wie React, ReactDOM und die Hauptkomponente (App) aus anderen Dateien.
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

// Die createRoot Methode von ReactDOM wird verwendet, um eine Root-Komponente für die Anwendung zu erstellen.
// Die Methode erwartet ein Element, das im HTML-Dokument existiert (in diesem Fall das Element mit der ID root)
// und rendert die Hauptkomponente (<App />) innerhalb einer Strict-Modus-Umgebung.
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

