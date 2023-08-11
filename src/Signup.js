import React, { useState } from "react";

function Signup({attemptSignup}) {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleChangeUsername = event => setUsername(event.target.value)
    const handleChangePassword = event => setPassword(event.target.value)

    


    return (
        <div>
        </div>
    );
}

export default Login;