// import logo from './logo.svg';
import './App.css';
import React from "react";

import AuthorList from "./components/Author";
import BookList from "./components/Book"

import axios from 'axios'

import SiderDemo from "./components/Menu_app";



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books' : [],
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
                {/*<AuthorList authors={this.state.authors}/>*/}
                <AuthorList authors={this.state.authors}/>
                <BookList books={this.state.books}/>
            </div>
        )
    }
}


export default App;
