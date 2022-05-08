import React from 'react'
import {Link} from "react-router-dom";

const TodoItem = ({todo, deleteToDo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.author}</td>
            <td>{todo.content}</td>
            <td>
                <button onClick={() => deleteToDo(todo.uid, todo.url)}
                        type='button'>Delete
                </button>
            </td>
        </tr>
    )
}
const TodoList = ({todos, deleteToDo}) => {
    return (
        <div>
            <table>
                <tr>
                    <th>PROJECT</th>
                    <th>AUTHOR</th>
                    <th>CONTENT</th>
                    <th></th>
                </tr>
                {todos.map((todo) => <TodoItem todo={todo} deleteToDo={deleteToDo}/>)}
            </table>
            <Link to="/todos/create"> Create </Link>
        </div>
    )
}
export default TodoList