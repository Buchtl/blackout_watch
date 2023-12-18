import React from 'react';

const Downloads: React.FC = () => {
    // Some component logic
  
    console.log(process.env.REACT_APP_URL);
    return (
        <div className="App">
        <header className="App-header">
          <a
            className="App-link"
            href={`http://${process.env.REACT_APP_URL}/heartbeatfile`}
          >
            Download heartbeat
          </a>
        </header>
      </div>
    );
  };
  
  export default Downloads;