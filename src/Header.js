import React from "react";
import { NavLink } from "react-router-dom";

function Header({currentUser, logout}) {
    
    return (    
        <ul className="text-white justify-evenly flex">
            { !currentUser ? <NavLink to="/login"> Login </NavLink> : null }
            { !currentUser ? <NavLink to="/signup"> Signup </NavLink> : null}
            { currentUser ? <NavLink to={`/${currentUser.username}`}> Profile </NavLink> : null }
            { currentUser ? <button onClick={logout}> Log Out </button> : null }
        </ul>
    );
}

export default Header;