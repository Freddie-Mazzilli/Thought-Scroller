import React, { useState } from "react";

function Login({attemptLogin}) {
    
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [loginSuccessful, setLoginSuccessful] = useState(false)

    const handleChangeUsername = event => setUsername(event.target.value)
    const handleChangePassword = event => setPassword(event.target.value)

    function handleSubmit(event){
        event.preventDefault()
        attemptLogin({username, password})
    }

    return (
        <div>
            SHEESH!
        </div>
    );
}

export default Login;
