import React from "react";
import {Link} from "react-router-dom";

const AuthorItem = ({author}) => {
    return (<tr>
        <td>
            <Link to={`author/${author.username}`}> {author.username} </Link>
        </td>
        <td>
            {author.uid}
        </td>
    </tr>)
}
const AuthorList = ({authors}) => {
    return (<table>
        <th>
            Username
        </th>
        <th>
            UID
        </th>
        {authors.map((author) => <AuthorItem author={author}/>)}
    </table>)
}
export default AuthorList