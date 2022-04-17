import React from "react";
import Table from 'react-bootstrap/Table'
import { useParams } from 'react-router-dom'


const ProjectItem = ({ project }) => {
    return (
        <tbody>
            <tr>
                <td>
                    {project.name}
                </td>
                <td>
                    {project.link}
                </td>
                <td>
                    {/* {project.worker} */}
                    {JSON.stringify(project.worker)}
                </td>
            </tr>
        </tbody>
    )
}


const ProjectListItem = ({ projects }) => {
    let { id } = useParams();
    let filtered_items = projects.filter((item) => item.uid == id)
    return (
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
                        Workers
                    </th>
                </tr>
            </thead>
            {filtered_items.map((project) => <ProjectItem project={project} />)}
        </Table>
    )
}

export default ProjectListItem