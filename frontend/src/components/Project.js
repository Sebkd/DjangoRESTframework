import React from 'react'

const ProjectItem = ({project}) => {
    return (
        <tr>
            {/*<td>{project.url}</td>*/}
            <td>{project.name}</td>
            <td>{project.link}</td>
            <td>{project.authors.join(' & ')}</td>
        </tr>
    )
}
const ProjectList = ({projects}) => {
    return (
        <table>
            <tr>
                <th>UID</th>
                <th>NAME</th>
                <th>LINK</th>
                <th>AUHTORS</th>
            </tr>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    )
}
export default ProjectList