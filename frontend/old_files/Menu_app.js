import React from "react";
import {Layout, Menu} from 'antd';
import {
    DesktopOutlined,
    PieChartOutlined,
    FileOutlined,
    TeamOutlined,
    UserOutlined,
} from '@ant-design/icons';


import {BrowserRouter, Link, Route, Router, Routes} from "react-router-dom";
import AuthorList from "../src/components/Author";
import App from "../src/App";
// import is_authenticated from "./App"
// import logout from "./App"


const {Header, Content, Footer, Sider} = Layout;
const {SubMenu} = Menu;

class Menu_app extends React.Component {
    state = {
        collapsed: false,
    };



    onCollapse = collapsed => {
        console.log(collapsed);
        this.setState({collapsed});
    };

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

                            {/*<SubMenu key="sub1" icon={<UserOutlined/>} title="User">*/}
                            {/*    <Menu.Item key="3">Tom</Menu.Item>*/}
                            {/*    <Menu.Item key="4">Bill</Menu.Item>*/}
                            {/*    <Menu.Item key="5">Alex</Menu.Item>*/}
                            {/*</SubMenu>*/}
                            {/*<SubMenu key="sub2" icon={<TeamOutlined/>} title="Team">*/}
                            {/*    <Menu.Item key="6">Team 1</Menu.Item>*/}
                            {/*    <Menu.Item key="8">Team 2</Menu.Item>*/}
                            {/*</SubMenu>*/}
                            <Menu.Item key="9" icon={<FileOutlined/>}>
                                <Link to={'/todos'}>ToDo</Link>
                            </Menu.Item>
                            <Menu.Item key="10" icon={<UserOutlined/>}>
                                {
                                    // is_authenticated() ? <Link to={'/'} onClick={() => logout()}>Logout</Link> :
                                        <Link to={'/login'}>Login</Link>
                                }
                            </Menu.Item>
                        </Menu>
                    </Sider>

                    <Layout className="site-layout">
                        <Header className="site-layout-background" style={{padding: 0}}/>
                        <Content>
                            <App/>

                        </Content>
                        <Footer style={{textAlign: 'center'}}>Ant Design ©2018 Created by Ant UED</Footer>
                    </Layout>
                </Layout>

            </BrowserRouter>

        );
    }
}

export default Menu_app;