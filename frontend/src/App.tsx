import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <a
          className="App-link"
          href={`http://${process.env.REACT_APP_BACKEND_URL}/heartbeatfile`}
        >
          Download heartbeat
        </a>
      </header>
    </div>
  );
}

export default App;
