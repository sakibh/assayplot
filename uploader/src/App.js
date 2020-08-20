import React from 'react';
import FileUpload from './components/FileUpload'
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1><i className="fas fa-chart-line"></i> Assay Plot</h1>
        <FileUpload />
      </header>
    </div>
  );
}

export default App;
