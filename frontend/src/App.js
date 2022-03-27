// import logo from './logo.svg';
import './App.css';
import React from "react";

import AuthorList from "./components/Author";
import BookList from "./components/Book"
import AuthorBookList from "./components/AuthorBook";

import axios from 'axios'

import {HashRouter, Route, Link, Routes, useLocation, Redirect} from 'react-router-dom'


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
        }
    }

    componentDidMount() {
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
    }

    render() {
        return (
            <div className="App">
                <HashRouter>
                    <Routes>
                        <Route path='*' element={<NotFound404/>}/>

                        <Route path='/' element={<AuthorList authors={this.state.authors}/>}/>
                        {/* в старом варианте выглядело так  */}
                        {/*<Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>*/}
                        {/*и не оборачивали в Routes*/}
                        {/*в новом оборачиваем в Routes маршруты Route и вместо component () => пишем просто element*/}
                        <Route path='/books' element={<BookList books={this.state.books}/>}/>

                        <Route path='/author/:username' element={<AuthorBookList items={this.state.books}/>}/>

                    </Routes>
                </HashRouter>
            </div>
        )
    }
}


export default App;
