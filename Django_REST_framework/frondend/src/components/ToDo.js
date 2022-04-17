import React from "react";
import Table from 'react-bootstrap/Table'
import { Link } from 'react-router-dom'

const ToDoItem = ({ todo, deleteToDo }) => {
    return (
        <tbody>
            <tr>
                <td>
                    {todo.author}
                </td>
                <td>
                    {todo.project}
                </td>
                <td>
                    {todo.title}
                </td>
                <td>
                    {todo.text}
                </td>
                <td>
                    {todo.created_add}
                </td>
                <td>
                    {todo.updated_add}
                </td>
                <td><button onClick={() => deleteToDo(todo.uid)} type='button'>Delete</button></td>
                {/* <td><button onClick={() => console.log(todo.uid)} type='button'>Delete</button></td> */}
            </tr>
        </tbody>
    )
}


const ToDoList = ({ todos, deleteToDo }) => {
    return (
        <div>
            <Table striped bordered hover variant="dark">
                <thead>
                    <tr>
                        <th>
                            Author
                        </th>
                        <th>
                            Project
                        </th>
                        <th>
                            Title
                        </th>
                        <th>
                            Text
                        </th>
                        <th>
                            Created_add
                        </th>
                        <th>
                            Updated_add
                        </th>
                        <th>
                        </th>
                    </tr>
                </thead>
                {todos.map((todo) => <ToDoItem todo={todo} deleteToDo={deleteToDo} />)}
            </Table>
            <Link to='/todo/create'>Create</Link>
        </div>
    )
}

export default ToDoList