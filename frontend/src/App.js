import React, { Component } from 'react';
import bear from './bear.gif';
import './App.css';
import $ from 'jquery';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={bear} className="App-logo" alt="logo" />
          <h2>bear.ai</h2>
        </div>
        <CourseList url="/search/berkeley-classes/?ordering=-id" pollInterval={1000} />
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
        var courseNodes = this.state.data.results.map(function(course) {
          return <li key={course.id}>{course.title}</li>
        });
      }
    }
    return (
      <div>
        <p><u>Live Course List</u></p>
        {courseNodes}
      </div>
    )
  }
}

export default App;
