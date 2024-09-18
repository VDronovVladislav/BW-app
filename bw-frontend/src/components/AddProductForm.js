import React, { useState } from 'react';

const AddProductForm = ({ onAdd }) => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name || !description || price === '') {
      alert('Пожалуйста, заполните все поля.');
      return;
    }

    const productData = { name, description, price: parseFloat(price) };
    try {
      const response = await fetch('http://127.0.0.1:8000/api/products/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(productData),
      });

      if (response.ok) {
        setName('');
        setDescription('');
        setPrice('');
        onAdd();
      } else {
        alert('Ошибка при добавлении продукта.');
      }
    } catch (error) {
      console.error('Ошибка:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <input
        type="text"
        placeholder="Название"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="text"
        placeholder="Описание"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <input
        type="number"
        placeholder="Цена"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />
      <button type="submit">Отправить</button>
    </form>
  );
};

export default AddProductForm;