import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import axios from 'axios';

import UsersList from './components/UsersList';
import About from './components/About';
import NavBar from './components/NavBar';
import Form from './components/forms/Form';
import Logout from './components/Logout';
import UserStatus from './components/UserStatus';
import Message from './components/Message';
import Footer from './components/Footer';
import Exercises from './components/Exercises';

class App extends Component {
  constructor() {
    super();
    this.state = {
      users: [],
      title: 'TestDriven.io',
      isAuthenticated: false,
      messageName: null,
      messageType: null,
    };
    this.logoutUser = this.logoutUser.bind(this);
    this.loginUser = this.loginUser.bind(this);
    this.createMessage = this.createMessage.bind(this);
    this.removeMessage = this.removeMessage.bind(this);
    this.getUsers = this.getUsers.bind(this);
  }
  componentWillMount() {
    if (window.localStorage.getItem('authToken')) {
      this.setState({ isAuthenticated: true });
    };
  };
  componentDidMount() {
    this.getUsers();
  };
  getUsers() {
    return axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => {
      const users = res.data.data.users;
      const updatedUsers = users.map((user) => {
        user.scores = [];
        return user;
      });
      this.setState({ users: updatedUsers });
      return axios.get(`${process.env.REACT_APP_SCORES_SERVICE_URL}/scores`)
    })
    .then((res) => {
      const scores = res.data.data.scores;
      const users = [...this.state.users]
      const updatedUsers = users.map((user) => {
        for (let score of scores) {
          if (score.user_id === user.id) {
            if (score.correct === null) score.correct = 'N/A';
            user.scores.push(score);
          }
        }
        return user;
      });
      this.setState({ users: updatedUsers });
    })
    .catch((err) => { });
  };
  logoutUser() {
    window.localStorage.clear();
    this.setState({ isAuthenticated: false });
  };
  loginUser(token) {
    window.localStorage.setItem('authToken', token);
    this.setState({ isAuthenticated: true });
    this.getUsers();
    this.createMessage('Welcome!', 'success');
  };
  createMessage(name='Sanity Check', type='success') {
    this.setState({
      messageName: name,
      messageType: type
    });
    setTimeout(() => {
      this.removeMessage();
    }, 3000);
  };
  removeMessage() {
    this.setState({
      messageName: null,
      messageType: null
    });
  };
  render() {
    return (
      <div>
        <NavBar
          title={this.state.title}
          isAuthenticated={this.state.isAuthenticated}
        />
        <div className="container">
          {this.state.messageName && this.state.messageType &&
            <Message
              messageName={this.state.messageName}
              messageType={this.state.messageType}
              removeMessage={this.removeMessage}
            />
          }
          <div className="row">
            <div className="col-md-6">
              <br/>
              <Switch>
                <Route exact path='/' render={() => (
                  <Exercises
                    isAuthenticated={this.state.isAuthenticated}
                    getUsers={this.getUsers}
                  />
                )} />
                <Route exact path='/about' component={About}/>
                <Route exact path='/register' render={() => (
                  <Form
                    formType={'register'}
                    isAuthenticated={this.state.isAuthenticated}
                    loginUser={this.loginUser}
                    createMessage={this.createMessage}
                    getUsers={this.getUsers}
                  />
                )} />
                <Route exact path='/login' render={() => (
                  <Form
                    formType={'login'}
                    isAuthenticated={this.state.isAuthenticated}
                    loginUser={this.loginUser}
                    createMessage={this.createMessage}
                    getUsers={this.getUsers}
                  />
                )} />
                <Route exact path='/all-users' render={() => (
                  <UsersList
                    users={this.state.users}
                  />
                )} />
                <Route exact path='/logout' render={() => (
                  <Logout
                    logoutUser={this.logoutUser}
                    isAuthenticated={this.state.isAuthenticated}
                  />
                )} />
                <Route exact path='/status' render={() => (
                  <UserStatus
                    isAuthenticated={this.state.isAuthenticated}
                  />
                )} />
              </Switch>
            </div>
          </div>
        </div>
        <Footer/>
      </div>
    )
  };
};

export default App;
