import './App.css';
import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Navigate, Routes, useLocation } from 'react-router-dom';

class App extends Component {

// Zeile: state ist ein Objekt, das den aktuellen Zustand der Komponente speichert.
// Hier werden die Daten, die später vom Server geholt werden, gespeichert.
  state = {
    data: [{}]
  };

// Zeile: Die componentDidMount-Methode wird automatisch aufgerufen, sobald die Komponente vollständig gerendert wurde.
// Hier wird eine HTTP-Anfrage an die URL /person gestartet.
// Zeile: Die then-Methode wird aufgerufen, wenn die HTTP-Anfrage erfolgreich war.
// Hier wird die Antwort des Servers von JSON in ein JavaScript-Objekt umgewandelt.
  componentDidMount() {
    fetch('/person')
      .then(res => res.json())
      .then(data => {
      // Die empfangenen Daten werden in den Zustand der Komponente gespeichert (this.setState({ data });)
      // und im Debugging-Kontext ausgegeben.
        this.setState({ data });
        console.log(data);
      });
  }

// Die render-Methode wird automatisch aufgerufen, wenn sich der Zustand der Komponente ändert.
// Hier wird eine bedingte Anweisung verwendet, um zu prüfen, ob die Daten bereits vom Server geholt wurden:
  render() {
    const { data } = this.state;
    return (
      <div>
        {typeof data.personen === 'undefined' ? (
        // Wenn die Daten noch nicht geladen wurden, wird eine Meldung "Loading..." ausgegeben.
          <p>Loading...</p>
        ) : (
        // Zeile: Wenn die Daten bereits geladen wurden, wird für jedes Element in data.personen eine p-Tag-Komponente
        //erstellt und angezeigt. Jede Komponente bekommt eine eindeutige key-Prop,
        // um eine eindeutige Identifikation sicherzustellen.
          data.personen.map((person, i) => <p key={i}>{person}</p>)
        )}
      </div>
    );
  }
}

// Zuletzt wird die App-Klasse exportiert, um sie in anderen Teilen der Anwendung verwenden zu können.
export default App;
