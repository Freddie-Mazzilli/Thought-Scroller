import React from "react";

function CreatePost({updateNewPost, addNewPost}) {

    return (
        <div className="bg-gray-300">
            <form onSubmit={(event => addNewPost(event))}>
                <div>
                    <label>Title</label><br></br>
                    <input onChange={updateNewPost} type="text" id="title" name="title"></input><br></br>
                    <label>Body Text</label><br></br>
                    <input onChange={updateNewPost} type="text" id="content" name="content"></input><br></br>
                    <button type="submit">Create Post</button>
                </div>
            </form>
        </div>       
    )
}

export default CreatePost;