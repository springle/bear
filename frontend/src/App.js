import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import $ from 'jquery';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>welcome to bear</h2>
        </div>
        <CourseList url="/search/courses/" pollInterval={10000} />
      </div>
    );
  }
}

class CourseList extends Component {
  constructor(props) {
    super(props);
    this.state = {data: []}
    this.loadCoursesFromServer = this.loadCoursesFromServer.bind(this);
  }

  loadCoursesFromServer() {
    $.ajax({
      url: this.props.url,
      datatype: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this)
    })
  }

  componentDidMount() {
    this.loadCoursesFromServer();
    this.timer = setInterval(this.loadCoursesFromServer,
                            this.props.pollInterval);
  }

  componentWillUnmount() {
    clearInterval(this.timer);
  }

  render() {
    if (this.state.data) {
      if (this.state.data.results) {
        var courseNodes = this.state.data.results.map(function(course, index) {
          return <li key={index}>{course.title}</li>
        });
      }
    }
    return (
      <div>
        <p><u>Courses</u></p>
        {courseNodes}
      </div>
    )
  }
}

export default App;
