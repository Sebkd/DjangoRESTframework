import React from "react";
import LoginForm from "./Auth";


class ProjectForm extends React.Component {
    //name, authors, link
    constructor(props) {
        super(props);
        this.state = {name: '', authors: props.authors.uid, link: '',};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({
                [event.target.name]: event.target.value
            }
        )
        console.log(this.state.name)
        console.log(this.state.author)
        console.log(this.state.link)
    }

    handleSubmit(event) {
        console.log(this.state.name)
        console.log(this.state.author)
        console.log(this.state.link)
        this.props.createProject(this.state.name, this.state.author, this.state.link);
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="name">name</label>
                    <input type="text" className="form-control" name="name"
                           value={this.state.name}
                           onChange={(event) => this.handleChange(event)}
                    />
                </div>


                <div className="form-group">
                    <label for="author">author</label>
                    <select name="author" className='form-control'
                            onChange={(event) => this.handleChange(event)}>
                        {this.props.authors.map((item) => <option
                            value={item.uid}>{item.username}</option>)}
                    </select>
                    {/*<input type="number" className="form-control" name="author"*/}
                    {/*       value={this.state.author} onChange={(event) => this.handleChange(event)}/>*/}
                </div>

                <div className="form-group">
                    <label htmlFor="link">link</label>
                    <input type="text" className="form-control" name="link"
                           value={this.state.link}
                           onChange={(event) => this.handleChange(event)}
                    />
                </div>

                <input type="submit" className="btn btn-primary" value="Save"/>

            </form>
        );
    }
}

export default ProjectForm