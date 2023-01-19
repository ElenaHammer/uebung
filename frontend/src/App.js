import './App.css';
import React, {Component} from 'react';
import { BrowserRouter as Router, Route, Navigate, Routes, useLocation } from 'react-router-dom';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import UebungApi from './api/UebungApi';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name : '',
      vornamen : '',
      currentUser: null,

    }
  }

  getPerson = () => {
    UebungApi.getAPI().getPersonByID(id)
    .then(personBO => this.setState({
      currentUser: personBO
    }))
  }

  render() {


  return (
    <div className="App">
      
        <p>
          Mein name ist {currentUser.getVorname()} {currentUser.getName()}
        </p>

        
    
      <TextField id="outlined-basic" label="Outlined" variant="outlined" />

    </div>
  );
}
}

export default App;

