import React from 'react';
import './App.css';

function App() {

  const handleButtonClick = () => {
    fetch('http://localhost:8000/test_connection')
      .then(response => response.json())
      .then(data => alert(data.message))
      .catch(error => console.error('Error:', error));
  };

  return (
    <div className="App">
      <header className="App-header">
        <div>
          <button onClick={handleButtonClick}>
            Click Me
          </button>
        </div>
      </header>
    </div>
  );
}

export default App;
