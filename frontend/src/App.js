import './App.css';
import React from "react";

import {Layout, Menu} from 'antd';
import {
    DesktopOutlined,
    PieChartOutlined,
    FileOutlined,
    UserOutlined,
} from '@ant-design/icons';
import {BrowserRouter, Link, Route, Routes} from "react-router-dom";

import axios from 'axios'
import Cookies from 'universal-cookie'


import AuthorList from "./components/Author";
import BookList from "./components/Book"
import AuthorBookList from "./components/AuthorBook";
import ProjectList from "./components/Project";
import ToDoList from "./components/ToDo";
import ProjectToDoList from "./components/ProjectToDo";
import LoginForm from "./components/Auth";
import ProjectForm from "./components/ProjectForm"
import ToDoForm from "./components/ToDoForm";


const {Header, Content, Footer, Sider} = Layout;
const {SubMenu} = Menu;

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
            'user_name': '',
            collapsed: false,
        }
    }

    onCollapse = collapsed => {
        console.log(collapsed);
        this.setState({collapsed});
    };

    set_token(token) {
        let cookies = new Cookies();
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }


    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        let cookies = new Cookies()
        let token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api/api-token-auth/', {username: username, password: password})
            .then(response => {
                let token = response.data['token']
                console.log(response.data.json)
                this.set_token(token)
                this.set_user_name(username)
            }).catch(error => alert('Неверный логин или пароль'))
    }

    set_user_name(username) {
        this.state.username = username
    }

    get_user_name() {
        return this.state.username
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


    load_data() {

        let headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/api/authors/', {headers})
            .then(response => {
                const items = response.data.results
                this.setState(
                    {
                        'authors': items
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/book/', {headers})
            .then(response => {
                const items = response.data.results
                this.setState(
                    {
                        'books': items
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project/', {headers})
            .then(response => {
                const items = response.data.results
                this.setState(
                    {
                        'projects': items
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const items = response.data.results
                this.setState(
                    {
                        'todos': items
                    }
                )
            }).catch(error => console.log(error))
    }

    deleteProject(uid, url_prj) {
        const headers = this.get_headers()
        axios.delete(url_prj, {headers})
            .then(response => {
                this.setState({projects: this.state.projects.filter((item) => item.uid !== uid)})
            }).catch(error => {
            console.log(error)
        })
    }

    createProject(name, author, link) {
        const headers = this.get_headers()
        const data = {name: name, authors: [author,], link: link}
        axios.post(`http://127.0.0.1:8000/api/project/`, data, {headers})
            .then(response => {
                let newProject = response.data
                const author = this.state.authors.filter((item) => item.uid === newProject.author)
                newProject.author = author
                this.state.projects.push(newProject)
            }).catch(error => {
            console.log(error)
        })
    }

    deleteToDo(uid, url_todo) {
        const headers = this.get_headers()
        axios.delete(url_todo, {headers})
            .then(response => {
                this.setState({todos: this.state.todos.filter((item) => item.uid !== uid)})
            }).catch(error => {
            console.log(error)
        })
    }

    createToDo(project, author, content) {
        const headers = this.get_headers()
        const obj = this.state.projects.filter((item) => item.uid === project)
        console.log(obj)
        const data = {project: project, author: author, content: content}
        axios.post(`http://127.0.0.1:8000/api/todo/`, data, {headers})
            .then(response => {
                let newToDo = response.data
                const author = this.state.authors.filter((item) => item.uid === newToDo.author)
                newToDo.author = author
                const project = this.state.projects.filter((item) => item.uid === newToDo.project)
                newToDo.project = project
                this.state.todos.push(newToDo)
            }).catch(error => {
            console.log(error)
        })
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {

        const {collapsed} = this.state;
        return (

            <BrowserRouter>
                <Layout style={{minHeight: '100vh'}}>

                    <Sider collapsible collapsed={collapsed} onCollapse={this.onCollapse}>
                        <div className="logo"/>
                        <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline">

                            <Menu.Item key="1" icon={<PieChartOutlined/>}>
                                <Link to={'/'}>Authors</Link>
                            </Menu.Item>

                            <Menu.Item key="2" icon={<DesktopOutlined/>}>
                                <Link to={'/projects'}>Projects</Link>

                            </Menu.Item>

                            <Menu.Item key="9" icon={<FileOutlined/>}>
                                <Link to={'/todos'}>ToDo</Link>
                            </Menu.Item>
                            <Menu.Item key="10" icon={<UserOutlined/>}>
                                {
                                    this.is_authenticated() ?
                                        <Link to={'/'} onClick={() => this.logout()}>
                                            Logout {this.get_user_name()}</Link> :
                                        <Link to={'/login'}>Login</Link>
                                }
                            </Menu.Item>
                        </Menu>
                    </Sider>

                    <Layout className="site-layout">
                        <Header className="site-layout-background" style={{padding: 0}}/>
                        <Content>

                            <div className="App">
                                <Routes>
                                    <Route path='*' element={<NotFound404/>}/>

                                    <Route path='/' element={<AuthorList authors={this.state.authors}/>}/>
                                    <Route path='/books' element={<BookList books={this.state.books}/>}/>
                                    <Route path='/projects' element={<ProjectList projects={this.state.projects}
                                                                                  deleteProject={(uid, url_prj) => this.deleteProject(uid, url_prj)}/>}/>
                                    <Route path='/todos' element={<ToDoList todos={this.state.todos}
                                                                            deleteToDo={(uid, url_todo) => this.deleteToDo(uid, url_todo)}/>}/>

                                    <Route path='/author/:username'
                                           element={<AuthorBookList items={this.state.books}/>}/>

                                    <Route path="/project/:name" element={<ProjectToDoList items={this.state.todos}
                                                                                           projects_list={this.state.projects}/>}/>

                                    <Route path='/login' element={<LoginForm
                                        get_token={(username, password) => this.get_token(username, password)}/>}/>

                                    <Route path='/projects/create' element={<ProjectForm authors={this.state.authors}
                                                                                         createProject={(name, author, link) => this.createProject(name, author, link)}/>}/>
                                    <Route path='/todos/create' element={<ToDoForm projects={this.state.projects}
                                                                                   authors={this.state.authors}
                                                                                   createToDo={(project, author, content) => this.createToDo(project, author, content)}/>}/>
                                </Routes>
                            </div>

                        </Content>
                        <Footer style={{textAlign: 'center'}}>Ant Design ©2018 Created by Ant UED</Footer>
                    </Layout>
                </Layout>

            </BrowserRouter>

        )
    }
}


export default App;
