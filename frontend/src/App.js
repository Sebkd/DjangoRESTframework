// import logo from './logo.svg';
import './App.css';
import React from "react";

import axios from 'axios'
import Cookies from 'universal-cookie'
import {HashRouter, Route, Link, Routes, useLocation, Redirect, BrowserRouter} from 'react-router-dom'

import AuthorList from "./components/Author";
import BookList from "./components/Book"
import AuthorBookList from "./components/AuthorBook";
import ProjectList from "./components/Project";
import ToDoList from "./components/ToDo";
import ProjectToDoList from "./components/ProjectToDo";
import LoginForm from "./components/Auth";


const NotFound404 = () => {

    return (
        <div>
            <h1>
                Page Not Found
                {/*из location.pathname можно взять глобальный путь урла*/}
            </h1>
        </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
            'projects': [],
            'todos': [],
            'token': '',
        }
    }

    set_token(token) {
        let cookies = new Cookies();
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated(){
        return this.state.token !== ''
    }

    logout(){
        this.set_token('')
    }

    get_token_from_storage(){
        let cookies = new Cookies()
        let token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password)


    load_data() {


        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const items = response.data.results
                this.setState(
                    {
                        'authors': items
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/book/')
            .then(response => {
                const items = response.data.results
                this.setState(
                    {
                        'books': items
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project/')
            .then(response => {
                const items = response.data.results
                this.setState(
                    {
                        'projects': items
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const items = response.data.results
                this.setState(
                    {
                        'todos': items
                    }
                )
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.load_data()
    }

    render() {
        return (
            <div className="App">
                <Routes>
                    <Route path='*' element={<NotFound404/>}/>

                    <Route path='/' element={<AuthorList authors={this.state.authors}/>}/>
                    {/* в старом варианте выглядело так  */}
                    {/*<Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>*/}
                    {/*и не оборачивали в Routes*/}
                    {/*в новом оборачиваем в Routes маршруты Route и вместо component () => пишем просто element*/}
                    <Route path='/books' element={<BookList books={this.state.books}/>}/>
                    <Route path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                    <Route path='/todos' element={<ToDoList todos={this.state.todos}/>}/>

                    <Route path='/author/:username' element={<AuthorBookList items={this.state.books}/>}/>

                    <Route path="/project/:name" element={<ProjectToDoList items={this.state.todos}/>}/>

                    <Route path='/login' element={<LoginForm
                        get_token={(username, password) => this.get_token(username, password)}/>}/>

                </Routes>
            </div>
        )
    }
}


export default App;
