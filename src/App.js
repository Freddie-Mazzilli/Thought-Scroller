import './index.css';
import {useState, useEffect} from 'react';
import {Route, Routes, useNavigate} from "react-router-dom";

import Nav from './Nav';
import ExplorerNav from './ExplorerNav';
import Login from './Login';
import Signup from './Signup';
import Home from './Home';
import UserProfile from './UserProfile';
import CreatePost from './CreatePost';

function App() {

  const navigate = useNavigate()

  const [currentUser, setCurrentUser] = useState(null)
  const [posts, setPosts] = useState([])
  const [comments, setComments] = useState([])
  const [replies, setReplies] = useState([])

  const [newPost, setNewPost] = useState({})


  useEffect(() => {
    fetch('http://127.0.0.1:7000/posts')
      .then(response => response.json())
      .then(postsData => setPosts(postsData))
  }, [])
  
  useEffect(() => {
    fetch('/current_session')
    .then(response => {
      if (response.ok) {
        response.json()
        .then(user => setCurrentUser(user))
      }
    })
  }, [])

  function updateNewPost(event){
    setNewPost({...newPost, [event.target.name]: event.target.value})
  }

  function addNewPost(event){
    event.preventDefault()

    fetch("http://127.0.0.1:7000/posts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(newPost)
    })
    .then(response => response.json())
    .then(newPost => setPosts([...posts, newPost]))
  }

  function attemptLogin(userInfo) {
    fetch('/login',  {
      method: "POST",
      headers: {
        'Content-Type': "application/json",
        "Accepts": "application/json"
      },
      body: JSON.stringify(userInfo)
    })
  }

  function attemptSignup(userInfo) {
    fetch('/users', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accepts": "application/json"
      },
      body: JSON.stringify(userInfo)
    })
  }
  
  function logout() {
    setCurrentUser(null)
    fetch('/logout', { method:"DELETE"})
    navigate('/')
  }

    return (
    <div className="bg-black flex flex-col h-screen justify-evenly">
      <div className="md:border-4 border-blue-700 w-full bg-black fixed top-0">
        <Nav currentUser={currentUser} logout={logout}/>
      </div>
        <Routes>
          <Route path="/" element={<Home/>}/>
          { !currentUser ? <Route path="/login" element={<Login attemptLogin={attemptLogin}/>} /> : null }
          { !currentUser ? <Route path="/signup" element={<Signup attemptSignup={attemptSignup}/>} /> : null }
          { currentUser ? <Route path={`/${currentUser.username}`} element={<UserProfile currentUser={currentUser}/>} /> : null }
          { currentUser ? <Route path="/create_post" element={<CreatePost addNewPost={addNewPost} updateNewPost={updateNewPost}/>} /> : null} 
        </Routes>
        <div className='md:border-4 border-blue-700 w-full bg-black fixed bottom-0'>
          <ExplorerNav currentUser={currentUser}/>
        </div>
    </div>
      );
    }
  
  export default App;