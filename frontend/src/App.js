import './App.css';
import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Navigate, Routes, useLocation } from 'react-router-dom';

function App() {

  const name = "Elena";

  return (
    <div className="App">
      
      <header className="App-header">
        <p>
          Mein name ist {name}
        </p>
      </header>
    </div>
  );
}

export default App;
