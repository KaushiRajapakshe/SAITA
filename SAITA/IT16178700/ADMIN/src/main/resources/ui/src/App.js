// Application related admin view main react ui
import React from 'react';
import './App.css';
import { BrowserRouter as Router } from 'react-router-dom';

import Header from './Header.js';
import Footer from "./Footer.js";

// React App function
function App() {

  // returning react ui view with user feedback table data
  return (
    <Router>
      <div className="main">
        <div className="App">
          <Header />
          <section className="line"></section>
          <Footer />
        </div>
      </div>
    </Router>
  );
}

export default App;