import React from 'react'

const BookItem = ({book}) => {
    return (
        <tr>
            <td>{book.name}</td>
            <td>{book.authors}</td>
        </tr>
    )
}
const BookList = ({books}) => {
    return (
        <table>
            <tr>
                <th>NAME</th>
                <th>AUHTOR</th>
            </tr>
            {books.map((book) => <BookItem book={book}/>)}
        </table>
    )
}
export default BookList