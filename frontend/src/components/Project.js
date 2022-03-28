import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            {/*<td>{project.url}</td>*/}
            <Link to={`/project/${project.name.replace(/\s/g, '')}`}> {project.name} </Link>

            {/*<td>{project.name}</td>*/}
            <td>{project.link}</td>
            <td>{project.authors.join(' & ')}</td>
        </tr>
    )
}
const ProjectList = ({projects}) => {
    return (
        <table>
            <tr>
                {/*<th>UID</th>*/}
                <th>NAME</th>
                <th>LINK</th>
                <th>AUTHORS</th>
            </tr>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}
export default ProjectList