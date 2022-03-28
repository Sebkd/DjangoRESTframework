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
    // когда авторов больше чем один
    let filtered_items = items.filter((item) => item.project.replace(/\s/g, '') === name)



    return (
        <table>
            <tr>
                {/*<th>ID</th>*/}
                <th>PROJECT</th>
                <th>AUTHOR</th>
                <th>CONTENT</th>
            </tr>
            {filtered_items.map((item) => <TodoItem item={item}/>)}
        </table>
    )
}
export default ProjectToDoList;