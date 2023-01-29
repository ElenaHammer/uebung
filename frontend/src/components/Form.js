//  Importiert die Component Klasse aus dem 'react'-Modul
import React, { Component } from 'react';

class Form extends Component {
    // Die Form Klasse definiert einen state-Objekt mit der Eigenschaft: name
    // Die Eigenschaft speichert den Wert, der vom Benutzer in das Formularfeld eingegeben wird.
    state = {
        name: '',
    };

    // Die Methode handleChange wird aufgerufen, wenn ein Eingabefeld im Formular geändert wird. 
    // Sie aktualisiert den Zustand des Formulars, indem sie den Wert des Formularfelds, 
    // das geändert wurde, in den Zustand überträgt.
    handleChange = event => {
        this.setState({ [event.target.name]: event.target.value });
    }

    // Die Methode handleSubmit wird aufgerufen, wenn das Formular gesendet wird. 
    // Sie verhindert das Standardverhalten des Formulars, 
    // indem sie das event-Objekt über event.preventDefault() unterbindet.
    handleSubmit = event => {
        event.preventDefault();
    }

    // Die render-Methode gibt die HTML-Struktur des Formulars zurück.
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <div>
                    <label>Name:</label>
                    <input
                        type="text"
                        name="name"
                        value={this.state.name}
                        onChange={this.handleChange}
                    />
                </div>
                <button type="submit">Submit</button>
            </form>
        );
    }
}

// Die Klasse "Form" wird exportiert, um sie in anderen Teilen der Anwendung verwenden zu können.
export default Form;
