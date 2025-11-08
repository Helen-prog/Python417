import './App.css';
import Users from './components/users/Users';
import { useState, useEffect } from 'react';

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://reqres.in/api/users')
      .then(res => res.json())
      .then(json => {
        setUsers(json.data);
      })
      .catch(err => {
        alert("Ошибка при получении пользователей" + err);
      })
  }, []);

  return (
    <div className="main">
      {/* <Users /> */}
    </div>
  );
}

export default App;
