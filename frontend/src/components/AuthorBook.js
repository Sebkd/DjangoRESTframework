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
    // let filtered_items = items.filter((item) => item.authors.username === username)
    // let filtered_items = items.forEach(function (item) {
    //     item.authors.filter((elem) => elem == username)
    // })
    // let filtered_items = items.filter((item) => item.authors == username)
    let filtered_items = items.filter((item) => {for (let index = 0; index < item.authors.length; ++index)
    { return item.authors[index] == username; }
    })
    // let filtered_items = items.filter((item) => item.authors.forEach(function (elem)
    // { return elem == username; }))
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