import React from 'react'
class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = { author: props.author[0]?.uid, project: props.project[0]?.uid, title: '', text: '' }
    }
    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value,
            }
        );
    }
    handleSubmit(event) {
        this.props.createToDo(this.state.author, this.state.project, this.state.title, this.state.text)
        event.preventDefault()
    }
    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="author">author</label>
                    <select name="author"
                        className='form-control'
                        onChange={(event) => this.handleChange(event)}>
                        {this.props.author.map((item) => <option
                            value={item.uid}>{item.username}</option>)}
                    </select>
                </div>
                <div className="form-group">
                    <label for="project">project</label>
                    <select name="project"
                        className='form-control'
                        onChange={(event) => this.handleChange(event)}>
                        {this.props.project.map((item) => <option
                            value={item.uid}>{item.name}</option>)}
                    </select>
                </div>
                <div className="form-group">
                    <label for="title">title</label>
                    <input type="text" className="form-control" name="title"
                        value={this.state.title} onChange={(event) => this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="text">text</label>
                    <input type="text" className="form-control" name="text"
                        value={this.state.text} onChange={(event) => this.handleChange(event)} />
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}
export default ToDoForm