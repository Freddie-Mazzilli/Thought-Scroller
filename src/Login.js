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
            <div>
                <h2 className="text-white">Thought-Scroller</h2>
            </div>
                <h6 className="text-white">Login Here</h6>
                {loginSuccessful ? <h1 className="text-white">Invalid Username or Password</h1> :
                <form onSubmit={(event => {handleSubmit(event)
                setLoginSuccessful(loginSuccessful => !loginSuccessful)
                })}>
                    <div className="bg-blue-500">
                        <label className="text-white"> Username </label>
                        <input className="text-white" type="text" onChange={handleChangeUsername} value={username} placeholder="Username"/>
                        <label className="text-white"> Password </label>
                        <input className="text-white" type="text" onChange={handleChangePassword} value={password} placeholder="Password"/> 
                        <button className="text-white" type="submit"> Login </button>
                    </div>
                </form>}
        </div>
    );
}

export default Login;
