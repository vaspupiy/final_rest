import React from "react";
import logo from './logo.svg'
import './App.css'
import UserList from "./components/User";
import ProjectList from "./components/Projects";
import ProjectListItem from "./components/Project";
import ToDoList from "./components/ToDo";
import axios from 'axios'
import Footer from "./components/Footer";
import Navb from "./components/Navb";
import { HashRouter, Route, Switch, BrowserRouter, Redirect, Link } from 'react-router-dom';
import LoginForm from './components/Auth.js';
import Cookies from 'universal-cookie';
import ProjectForm from "./components/ProjectForm"
import ToDoForm from "./components/ToDoForm"


const NotFound404 = ({ location }) => {
  return (
    <div>
      <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}


class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todos': [],
      'token': '',
      'username': ''
    }
  }

  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({ 'token': token }, () => this.load_data())
  }

  set_username(username) {
    const cookies = new Cookies()
    cookies.set('username', username)
    this.setState({ 'username': username })
  }

  is_authenticated() {
    return this.state.token != ''
  }

  logout() {
    this.set_token('')
    this.set_username('')
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({ 'token': token }, () => this.load_data())
  }

  get_username_from_storage() {
    const cookies = new Cookies()
    const username = cookies.get('username')
    this.setState({ 'username': username })
  }


  get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {
      username: username,
      password: password,
    }).then(response => {
      this.set_token(response.data['token'], this.set_username(username))
    }).catch(error => alert('Неверный логин или пароль'))
  }

  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }
    if (this.is_authenticated()) {
      headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
  }

  deleteProject(uid) {
    const headers = this.get_headers()
    axios.delete(`http://127.0.0.1:8000/api/projects/${uid}/`, { headers, headers })
      .then(response => {
        this.setState({
          projects: this.state.projects.filter((item) => item.uid !== uid)
        })
      }).catch(error => console.log(error))
  }

  createProject(name, link, worker) {
    const headers = this.get_headers()
    const data = { name: name, link: link, worker: worker }
    console.log(data)
    axios.post(`http://127.0.0.1:8000/api/projects/`, data, { headers, headers })
      .then(response => {
        let new_project = response.data
        const project = this.state.projects.filter((item) => item.uid === new_project.project)[0]
        new_project.project = project
        this.setState({ projects: [...this.state.projects, new_project] })
      }).catch(error => console.log(error))
  }

  deleteToDo(uid) {
    const headers = this.get_headers()
    axios.delete(`http://127.0.0.1:8000/api/todo/${uid}/`, { headers, headers })
      .then(response => {
        this.setState({
          todos: this.state.todos.filter((item) => item.uid !== uid)
        })
      }).catch(error => console.log(error))
  }

  createToDo(author, project, title, text) {
    const headers = this.get_headers()
    const data = { author: author, project: project, title: title, text: text }
    console.log(data)
    axios.post(`http://127.0.0.1:8000/api/todo/`, data, { headers, headers })
      .then(response => {
        let new_todo = response.data
        const todo = this.state.todos.filter((item) => item.uid === new_todo.todo)[0]
        new_todo.todo = todo
        this.setState({ todos: [...this.state.todos, new_todo] })
      }).catch(error => console.log(error))
  }

  load_data() {
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/users', { headers })
      .then(response => {
        this.setState(
          {
            users: response.data
          }
        )
      }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/api/projects', { headers })
      .then(response => {
        this.setState(
          {
            projects: response.data
          }
        )
      }).catch(error => console.log(error), this.setState({ projects: [] }))
    axios.get('http://127.0.0.1:8000/api/todo', { headers })
      .then(response => {
        this.setState(
          {
            todos: response.data
          }
        )
      }).catch(error => console.log(error))
  }

  componentDidMount() {
    this.get_token_from_storage()
    this.get_username_from_storage()
  }

  render() {
    return (
      <div className="App">
        <Navb />

        {/* <HashRouter> */}
        <BrowserRouter>
          <nav>
            {this.is_authenticated() ? 'пользователь: ' + this.state.username + ' ' : ''}
            {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
          </nav>
          <Switch>
            <Route exact path='/' component={() => <UserList users={this.state.users} />} />
            <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} deleteProject={(uid) => this.deleteProject(uid)} />} />
            <Route path='/project/:id' component={() => <ProjectListItem projects={this.state.projects} />} />
            <Route path='/projects/create' component={() => <ProjectForm worker={this.state.users} createProject={(name, link, worker) => this.createProject(name, link, worker)} />} />
            <Route path='/todo/create' component={() => <ToDoForm author={this.state.users} project={this.state.projects} createToDo={(author, project, title, text) => this.createToDo(author, project, title, text)} />} />
            <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos} deleteToDo={(uid) => this.deleteToDo(uid)} />} />
            <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
            <Route component={NotFound404} />
          </Switch>
        </BrowserRouter>
        {/* </HashRouter> */}
        <Footer />
      </div >

    )
  }
}

export default App;