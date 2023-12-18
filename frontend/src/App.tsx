import React from 'react';
import './App.css';
import Downloads from './Downloads';

console.log("BEFOREAPP ClientSide:" + process.env.REACT_APP_URL);

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
