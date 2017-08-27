import React, { Component } from 'react';
import bear from './bear.gif';
import 'typeface-roboto';
import './App.css';
import SearchBar from './components/SearchBar';

class Home extends Component {
  render() {
    return (
      <div className="Home">
        <div className="Home-header">
          <img src={bear} className="Home-logo" alt="logo" />
          <h2>bear.ai</h2>
        </div>
        <div className="Home-search">
          <SearchBar></SearchBar>
        </div>
      </div>
    );
  }
}

export default Home;
