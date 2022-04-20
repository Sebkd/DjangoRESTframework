import React, {useEffect, useState} from 'react'
import {Link} from "react-router-dom";
import SearchBar from "./Search";
import Fuse from "fuse.js";
import {Space} from 'antd';
import {SearchOutlined} from '@ant-design/icons';

const ProjectItem = ({project, author, deleteProject}) => {
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
    // const [searchResults, setSearchResults] = useState([]);
    const handleChange = event => {
        setSearchTerm(event.target.value);
    };
    const results = !searchTerm
    ? projects
    : projects.filter(project =>
        project.name.toLowerCase().includes(searchTerm.toLocaleLowerCase())
      );


    // useEffect(() => {
    //     const results = projects.filter(project =>
    //         project.name.toLowerCase().includes(searchTerm.toLowerCase())
    //     );
    //     setSearchResults(results);
    // }, [searchTerm]);



    return (
        <div>
            <table>
                <tr>
                    {/*<th>UID</th>*/}
                    <th>NAME</th>
                    <th>LINK</th>
                    <th>AUTHORS</th>
                    <th></th>
                </tr>
                {projects.map((project) => <ProjectItem project={project}
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
                {/*{ searchResults.map(item => (*/}
                {/*    <ol>*/}
                {/*        <Link to={`/project/${item.name.replace(/\s/g, '')}`}> {item.name} </Link>*/}
                {/*    </ol>*/}
                                { results.map(item => (
                    <ol>
                        <Link to={`/project/${item.name.replace(/\s/g, '')}`}> {item.name} </Link>
                    </ol>
                    // <li>{item.name}</li>
                ))}
            </ul>
        </div>
    )
}
export default ProjectList