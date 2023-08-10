import React from "react";
import { NavLink } from "react-router-dom";

function Nav({currentUser, logout}) {
    
    return (
        <ul>
            { !currentUser ? <NavLink to="/login"> Login </NavLink> : null }
            { !currentUser ? <NavLink to="/signup"> Signup </NavLink> : null}
            { currentUser ? <button onClick={logout}> Log Out </button> : null }
        </ul>
    );
}

export default Nav;