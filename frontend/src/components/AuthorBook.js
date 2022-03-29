import React from 'react'
import {useParams} from 'react-router-dom'

const BookItem = ({item}) => {
    return (
        <tr>
            {/*<td>{item.id}</td>*/}
            <td>{item.name}</td>
            <td>{item.authors.join(' & ')}</td>
        </tr>
    )
}
const AuthorBookList = ({items}) => {
    let {username} = useParams();
    // когда авторов больше чем один
    let filtered_items = items.filter((item) => {for (let index = 0; index < item.authors.length; ++index)
    { if (item.authors[index] === username) return 1}
    })

    return (
        <table>
            <tr>
                {/*<th>ID</th>*/}
                <th>NAME</th>
                <th>AUTHOR</th>
            </tr>
            {filtered_items.map((item) => <BookItem item={item}/>)}
        </table>
    )
}
export default AuthorBookList