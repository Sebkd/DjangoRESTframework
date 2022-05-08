import React from 'react'
import {useParams} from 'react-router-dom'

const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.author}</td>
            <td>{todo.content}</td>
        </tr>
    )
}
const ProjectToDoList = ({items, projects_list}) => {
    let name = useParams();

    let project_uid = projects_list.filter((item) => item.name.replace(/\s/g, '') === name.name)[0]

    let filtered_items = items.filter((item) => item.project === project_uid.uid)

    return (
        <table>
            <tr>
                <th>PROJECT</th>
                <th>AUTHOR</th>
                <th>CONTENT</th>
            </tr>
            {filtered_items.map((item) => <TodoItem todo={item}/>)}
        </table>
    )
}
export default ProjectToDoList;