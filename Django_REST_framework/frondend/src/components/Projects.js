import React from "react";
import Table from 'react-bootstrap/Table'
import { Link } from 'react-router-dom'


const ProjectItem = ({ project, deleteProject }) => {
    return (
        <tbody>
            <tr>
                <td>
                    <Link to={`project/${project.uid}`}>{project.name}</Link>
                </td>
                <td>
                    {project.link}
                </td>
                <td>
                    {/* {project.worker} */}
                    {JSON.stringify(project.worker)}
                </td>
                <td><button onClick={() => deleteProject(project.uid)} type='button'>Delete</button></td>
            </tr>
        </tbody>
    )
}


const ProjectList = ({ projects, deleteProject }) => {
    return (
        <div>
            <Table striped bordered hover variant="dark">
                <thead>
                    <tr>
                        <th>
                            ProjectName
                        </th>
                        <th>
                            Link
                        </th>
                        <th>
                            Worker
                        </th>
                        <th></th>
                    </tr>
                </thead>
                {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject} />)}
            </Table>
            <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectList