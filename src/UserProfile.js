import React from "react";

function UserProfile({currentUser}) {

    return (
        <div className="bg-gray-300">
            <span> Welcome {currentUser.username}! </span>
            <h6>This Is Where The Details Of A User Would Go</h6>
        </div>
    )
}

export default UserProfile;