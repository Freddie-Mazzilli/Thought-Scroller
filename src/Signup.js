import React, { useState } from "react";

function Signup({attemptSignup}) {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleChangeUsername = event => setUsername(event.target.value)
    const handleChangePassword = event => setPassword(event.target.value)

    function handleSubmit(event){
        event.preventDefault()
        attemptSignup({username, password})
    }    


    return (
        <div>
            <div>
                <h2 className="text-white">ThoughtScroller</h2>
            </div>
                <h6 className="text-white">Signup Here</h6>
                <form onSubmit={handleSubmit}>
                    <div className="bg-blue-500">
                        <label className="text-white">Username</label>
                        <input className="text-black" type="text" onChange={handleChangeUsername} value={username} placeholder="Username"/>
                        <label className="text-white">Password</label>
                        <input className="text-black" type="password" onChange={handleChangePassword} value={password} placeholder="Password"/>
                        <button type="submit">Signup</button>
                    </div>
                </form>
        </div>
    );
}

export default Signup;