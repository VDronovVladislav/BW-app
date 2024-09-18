import React from 'react';
import AddProductForm from './components/AddProductForm';
import ProductList from './components/ProductList';
import './App.css';

const App = () => {
  return (
    <div>
      <header>
        <h1>Список продуктов</h1>
      </header>
      <main className="container">
        <AddProductForm onAdd={() => window.location.reload()} />
        <ProductList />
      </main>
      <footer>© vdronovvladislav</footer>
    </div>
  );
};

export default App;