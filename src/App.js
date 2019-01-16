import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <html>
        <head>
          <title>강아지 가이드</title>
        </head>
        <body className="line">
          <div className="head">
            <div className="headlinelogo headline">
              <img className="headicon headline"
              src="https://image.flaticon.com/icons/svg/1196/1196308.svg"
              alt="dog icon"
              title="강아지 가이드"
              width="90"
              height="60"/>
            </div>
            <div className="headlineexplanation headline">
              <div className="header">강아지 가이드</div>
              <div>dog guide</div>
            </div>
            <div className="headlinesearch headline">
              <p>search</p>
            </div>
            <div className="headlinelogin headline">
              <p>login</p>
            </div>
            <div className="headlinejoin headline">
              <p>join</p>
            </div>
          </div>
          <div className="bodyline">   
            <img
            src="https://images.unsplash.com/photo-1546421845-6471bdcf3edf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60"
            alt="human and dog"
            width="100%"
            title="강아지 가이드"/>
          </div> 
        </body>
      </html>
    );
  }
}

export default App;
