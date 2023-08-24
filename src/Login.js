import React, { useState } from "react";
import MisterBrain from "./assets/MisterBrain.png"

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
        <div className="grid grid-cols-2 items-center">
            <div>
                <img className="ml-40 md:border-2 border-white" src={MisterBrain} alt="Brainy One"/>
            </div>
            <div className="w-3/4">
                <h1 className="text-white text-center text-3xl font-extralight">Login Here</h1>
                <br></br>
                <form onSubmit={handleSubmit}>
                    <div className="grid grid-rows-5">
                        <label className="text-white"> Username </label>
                        <input className="text-black" type="text" onChange={handleChangeUsername} value={username} placeholder="Username"/>
                        <br></br>
                        <label className="text-white"> Password </label>
                        <input className="text-black" type="password" onChange={handleChangePassword} value={password} placeholder="Password"/> 
                        <br></br>
                        <br></br>
                        <button className="text-white md:border-4 border-white mx-60 py-2" type="submit"> Login </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default Login;
