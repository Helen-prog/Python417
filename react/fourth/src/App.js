import './App.css';
import data from './data.json';
import ImageGallery from "react-image-gallery";
import { useState, useEffect } from 'react';


function App() {
  const collections = data.collections;
  const cats = data.categories;
  const [searchValue, setSearchValue] = useState('');
  const [categoryId, setCategoryId] = useState(0);

  useEffect(() => {
    console.log("Hello: ", categoryId);  
    return () => console.log("Goodbue");
      
  }, [categoryId]);

  return (
    <div className="App">
  
      
      <h1>Моя коллекция фотографий</h1>

      <div className="top">
        <div className="tags">
          {
            cats.map((obj, index) => (
              <li key={index}
                className={categoryId === index ? 'active' : ''}
                onClick={() => setCategoryId(index)}
              >
                {obj.name}
              </li>
            ))
          }
        </div>
      </div>

      <div className="search">
        <input 
          type="search" 
          className='search-input' 
          placeholder='Поиск по названию'
          value={searchValue} 
          onChange={e => setSearchValue(e.target.value)}
          />
      </div>

      <div className="image-gallery-wrapper">
        {
          collections
          .filter(obj => obj.name.toLowerCase().includes(searchValue.toLowerCase()) && (categoryId === obj.category || categoryId === 0))
          .map((obj, index) => (
            <div className="collection" key={index}>
              <h2>{obj.name}</h2>
              <ImageGallery items={obj.photos} />
            </div>
          ))
        }
      </div>
          {console.log("Return")}
    </div>
  );
}

export default App;
