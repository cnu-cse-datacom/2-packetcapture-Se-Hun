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
          <div className="headline">
            <div className="headlinelogo headfactor">
              <img className="headicon headfactor"
              src="https://image.flaticon.com/icons/svg/1196/1196308.svg"
              alt="dog icon"
              title="강아지 가이드"/>
            </div>
            <div className="headlineexplanation headfactor">
              <p className="header">강아지 가이드</p>
              <p>dog guide</p>
            </div>
            <div className="headlinesearch headfactor">
              <p className="height5">search</p>
            </div>
            <div className="headlinelogin headfactor">
              <p className="height5">login</p>
            </div>
            <div className="headlinejoin headfactor">
              <p className="height5">join</p>
            </div>
            <div className="headlineetc headfactor">
              <p className="height5">etc</p>
            </div>
          </div>
          <div className="bodyline">   
            <div className="maindisplay">
              <h1>강아지 가이드</h1>
              <p>강아지에 대한 정보를 알아보세요!<br />다양한 종류의 강아지들을 알려드립니다!</p>
              <p>search</p>
            </div>
          </div> 
        </body>
      </html>
    );
  }
}

export default App;
