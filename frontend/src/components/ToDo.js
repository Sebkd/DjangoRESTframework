import React from 'react'

const ToDoItem = ({todo}) => {
    return (
        <tr>
            {/*<td>{project.url}</td>*/}
            {/*<td>{todo.url}</td>*/}
            {/*<td>{todo.is_active}</td>*/}
            {/*<td>{todo.is_created}</td>*/}
            {/*<td>{todo.is_change}</td>*/}
            <td>{todo.project}</td>
            <td>{todo.author}</td>
            <td>{todo.content}</td>
        </tr>
    )
}
const ToDoList = ({todos}) => {
    return (
        <table>
            <tr>
                {/*<th>URL</th>*/}
                {/*<th>ACTIVE</th>*/}
                {/*<th>CREATED</th>*/}
                {/*<th>CHANGE</th>*/}
                <th>PROJECT</th>
                <th>AUTHOR</th>
                <th>CONTENT</th>
            </tr>
            {/*{todos.map((todo) => <ToDotodo todo={todo}/>)}*/}
            {todos.map((todo) => <ToDoItem todo={todo}/>)}
        </table>
    )
}
export default ToDoList