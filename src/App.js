import './index.css';
import {useState, useEffect} from 'react';
import {Route, BrowserRouter, Routes, useNavigate} from "react-router-dom";

import Nav from './Nav';
import Login from './Login';

function App() {

  const navigate = useNavigate()

  const [currentUser, setCurrentUser] = useState(null)
  const [posts, setPosts] = useState([])
  const [comments, setComments] = useState([])
  const [replies, setReplies] = useState([])

  useEffect(() => {
    fetch('/current_session')
    .then(response => {
      if (response.ok) {
        response.json()
        .then(user => setCurrentUser(user))
      }
    })
  }, [])

  function attemptLogin(userInfo) {
    fetch('/login',  {
      method: "POST",
      headers: {
        'Content-Type': "application/json",
        "Accepts": "application/json"
      },
      body: JSON.stringify(userInfo)
    })
    .then(response => {
      if (response.ok) {
        response.json()
        .then(user => setCurrentUser(user))
        navigate('/user_profile')
      }
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
    .then(response => {
      if (response.ok) {
        response.json()
        .then(user => setCurrentUser(user))
        navigate('/user_profile')
      }
    })
  }
  
  function logout() {
    setCurrentUser(null)
    fetch('/logout', { method:"DELETE"})
    navigate('/')
  }

    return (
    <div className="bg-black h-full w-full">
      <div className="md:border-4 border-blue-700 w-full bg-black">
        <Nav currentUser={currentUser} logout={logout}/>
      </div>
        <Routes>
        </Routes>
    </div>
      );
    }
  
  export default App;