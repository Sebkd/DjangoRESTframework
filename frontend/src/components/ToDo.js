import React from 'react'

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
const TodoList = ({todos}) => {
    return (
        <table>
            <tr>
                {/*<th>UID</th>*/}
                <th>PROJECT</th>
                <th>AUTHOR</th>
                <th>CONTENT</th>
            </tr>
            {todos.map((todo) => <TodoItem todo={todo}/>)}
        </table>
    )
}
export default TodoList