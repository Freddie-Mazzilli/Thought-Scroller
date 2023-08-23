import React, { useState } from "react";

function Login({attemptLogin}) {
    
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleChangeUsername = event => setUsername(event.target.value)
    const handleChangePassword = event => setPassword(event.target.value)

    function handleSubmit(event){
        event.preventDefault()
        attemptLogin({username, password})
    }

    return (
        <div>
            <div>
                <h2 className="text-white">Thought-Scroller</h2>
            </div>
                <h1 className="text-white">Login Here</h1>
                <form onSubmit={handleSubmit}>
                    <div className="bg-blue-500">
                        <label className="text-white"> Username </label>
                        <input className="text-black" type="text" onChange={handleChangeUsername} value={username} placeholder="Username"/>
                        <label className="text-white"> Password </label>
                        <input className="text-black" type="password" onChange={handleChangePassword} value={password} placeholder="Password"/> 
                        <button className="text-white" type="submit"> Login </button>
                    </div>
                </form>
        </div>
    );
}

export default Login;
