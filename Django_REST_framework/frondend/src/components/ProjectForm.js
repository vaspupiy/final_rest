import React from 'react'
class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = { name: '', link: '', worker: [props.worker[0]?.uid] }
    }
    handleChange(event) {
        if (event.target.name === 'worker') {
            this.setState(
                {
                    [event.target.name]: [...event.target.selectedOptions].map(o => o.value),
                }
            );
        } else {
            this.setState(
                {
                    [event.target.name]: event.target.value,
                }
            );
        }

    }
    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.link, this.state.worker)
        event.preventDefault()
    }
    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">name</label>
                    <input type="text" className="form-control" name="name"
                        value={this.state.name} onChange={(event) => this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="link">link</label>
                    <input type="text" className="form-control" name="link"
                        value={this.state.link} onChange={(event) => this.handleChange(event)} />
                </div>
                <div className="form-group">
                    <label for="worker">worker</label>
                    {/* <input type="text" className="form-control" name="worker"
                        value={this.state.worker} onChange={(event) => this.handleChange(event)} /> */}
                    <select name="worker" className='form-control' multiple={true}
                        onChange={(event) => this.handleChange(event)}>
                        {this.props.worker.map((item) => <option
                            value={item.uid}>{item.username}</option>)}
                    </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}
export default ProjectForm