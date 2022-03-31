import React from 'react'
import {useParams} from 'react-router-dom'

const TodoItem = ({todo}) => {
    return (
        <tr>
            {/*<td>{todo.url}</td>*/}
            <td>{todo.project}</td>
            <td>{todo.author}</td>
            <td>{todo.content}</td>
        </tr>
    )
}
const ProjectToDoList = ({items}) => {
    let {name} = useParams();
    console.log(name)

    let filtered_items = items.filter((item) => item.project.replace(/\s/g, '') === name)
    // let filtered_items = items.filter(function (item) {
    //     let projectname = item.project.replace(/\s/g, '')
    //     console.log(name)
    //     console.log(item.project)
    //     console.log(projectname)
    //     console.log(projectname == name)
    //     if (projectname == name) return 1
    // })



    return (
        <table>
            <tr>
                {/*<th>ID</th>*/}
                <th>PROJECT</th>
                <th>AUTHOR</th>
                <th>CONTENT</th>
            </tr>
            {filtered_items.map((item) => <TodoItem todo={item}/>)}
        </table>
    )
}
export default ProjectToDoList;