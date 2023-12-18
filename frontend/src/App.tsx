import React from 'react';
import logo from './logo.svg';
import './App.css';
import Downloads from './Downloads';

function App() {
  console.log("ClientSide:" + process.env.REACT_APP_URL);
  return (
    <div className="App">
      <header className="App-header">
        <Downloads/>
      </header>
    </div>
  );
}

export default App;
