import './index.css';
import {useState, useEffect} from 'react';

function App() {

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
        history.push('/user_page')
      }
    })
  }
  
    return (
    <div className="container mx-auto bg-gray-200 rounded-xl shadow border p-8 m-10">
    <p className="text-3xl text-gray-700 font-bold mb-5">
    Welcome!
    </p>
    <p className="text-gray-500 text-lg">
    React and Tailwind CSS in action
    </p>
    </div>
    );
    }
  
  export default App;