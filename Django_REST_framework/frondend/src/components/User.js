import React from "react";
import Table from 'react-bootstrap/Table'

const UserItem = ({ user }) => {
    return (
        <tbody>
            <tr>
                <td>
                    {user.username}
                </td>
                <td>
                    {user.email}
                </td>
                <td>
                    {user.first_name}
                </td>
                <td>
                    {user.last_name}
                </td>
            </tr>
        </tbody>
    )
}


const UserList = ({ users }) => {
    return (
        <Table striped bordered hover variant="dark">
            <thead>
                <tr>
                    <th>
                        Username
                    </th>
                    <th>
                        E-mail
                    </th>
                    <th>
                        First Name
                    </th>
                    <th>
                        Laste Name
                    </th>
                </tr>
            </thead>
            {users.map((user) => <UserItem user={user} />)}
        </Table>
    )
}

export default UserList