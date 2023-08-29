import React from "react";
import { NavLink } from "react-router-dom";

function Footer({currentUser}) {

    return (
        <ul className="text-white justify-evenly flex">
             <NavLink to="/">Thought Scroll</NavLink>
             { currentUser ? <NavLink to="/create_post">Create</NavLink> : null }
             <NavLink to="/communities">Communities</NavLink>             
        </ul>
    )
}

export default Footer;