import React from "react";
import {Form, Input, Button, Checkbox} from 'antd';

class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {username: "", password: ""}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value, // в этот таргет будут попадать либо login, либо password
            }
        );
    }

    handleSubmit(event) {
        console.log(this.state.username + ' ' + this.state.password)
        this.props.get_token(this.state.username, this.state.password)
        console.log(this.state.username + ' ' + this.state.password) // чтобы при Submit форма не отправлялась
        event.preventDefault() // чтобы при Submit форма не отправлялась

    }

    render() {
        return (

            <Form
                name="basic"
                labelCol={{span: 8}}
                wrapperCol={{span: 16}}
                initialValues={{remember: true}}
                onFinish={(event) => this.handleSubmit(event)}
                autoComplete="off"
            >
                <Form.Item
                    label="Username"
                    name="username"
                    rules={[{required: true, message: 'Please input your username!'}]}
                >
                    <Input
                        type="text" name="username" placeholder="username"
                        value={this.state.username}
                        onChange={(event) => this.handleChange(event)}
                    />
                </Form.Item>

                <Form.Item
                    label="Password"
                    name="password"
                    rules={[{required: true, message: 'Please input your password!'}]}
                >
                    <Input.Password
                        type="password" name="password" placeholder="password"
                        value={this.state.password}
                        onChange={(event) => this.handleChange(event)}
                    />
                </Form.Item>

                <Form.Item wrapperCol={{offset: 8, span: 16}}>
                    <Button type="primary" htmlType="submit">
                        Login
                    </Button>
                </Form.Item>
            </Form>
        )
            ;
    }
}

export default LoginForm