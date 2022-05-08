import React from "react";


class ToDoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {projects: props.authors.uid, authors: props.authors.uid, content: '',};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({
                [event.target.name]: event.target.value
            }
        )
    }

    handleSubmit(event) {
        this.props.createToDo(this.state.project, this.state.author, this.state.content);
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <div className="form-group">
                    <label htmlFor="project">project</label>
                    <select name="project" className='form-control'
                            onChange={(event) => this.handleChange(event)}>
                        {this.props.projects.map((item) => <option
                            value={item.uid}>{item.name}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label for="author">author</label>
                    <select name="author" className='form-control'
                            onChange={(event) => this.handleChange(event)}>
                        {this.props.authors.map((item) => <option
                            value={item.uid}>{item.username}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="content">content</label>
                    <input type="text" className="form-control" name="content"
                           value={this.state.content}
                           onChange={(event) => this.handleChange(event)}
                    />
                </div>

                <input type="submit" className="btn btn-primary" value="Save"/>

            </form>
        );
    }
}

export default ToDoForm
