import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            {/*<td>{project.url}</td>*/}
            <Link to={`/project/${project.name.replace(/\s/g, '')}`}> {project.name} </Link>

            {/*<td>{project.name}</td>*/}
            <td>{project.link}</td>
            <td>{project.authors.join(' & ')}</td>
            <td>
                <button onClick={() => deleteProject(project.uid, project.url)}
                        type='button'>Delete
                </button>
            </td>
        </tr>
    )
}
const ProjectList = ({projects, deleteProject}) => {
    return (
        <table>
            <tr>
                {/*<th>UID</th>*/}
                <th>NAME</th>
                <th>LINK</th>
                <th>AUTHORS</th>
                <th></th>
            </tr>
            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
        </table>
    )
}
export default ProjectList