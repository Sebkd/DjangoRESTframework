import React, {useEffect, useState} from 'react'
import {Link} from "react-router-dom";
import {Space} from 'antd';
import {SearchOutlined} from '@ant-design/icons';

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <Link to={`/project/${project.name.replace(/\s/g, '')}`}> {project.name} </Link>
            <td>{project.link}</td>
            <td>{project.authors.join(' & ')}
            </td>
            <td>
                <button onClick={() => deleteProject(project.uid, project.url)}
                        type='button'>Delete
                </button>
            </td>
        </tr>
    )
}
const ProjectList = ({projects, deleteProject}) => {

    const [searchTerm, setSearchTerm] = useState("");
    const handleChange = event => {
        setSearchTerm(event.target.value);
    };
    const results = !searchTerm
        ? projects
        : projects.filter(project =>
            project.name.toLowerCase().includes(searchTerm.toLocaleLowerCase())
        );


    return (
        <div>
            <table>
                <tr>
                    <th>NAME</th>
                    <th>LINK</th>
                    <th>AUTHORS</th>
                    <th></th>
                </tr>
                {results.map((project) => <ProjectItem project={project}
                                                       deleteProject={deleteProject}/>)}
            </table>
            <Link to="/projects/create"> Create </Link>
            <div>
                <Space>
                    <SearchOutlined/>
                </Space>

                <input
                    type="text"
                    placeholder="Search"
                    value={searchTerm}
                    onChange={handleChange}
                />
            </div>

            <ul>
            </ul>
        </div>
    )
}
export default ProjectList