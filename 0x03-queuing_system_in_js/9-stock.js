const express = require('express');
import { createClient } from 'redis';

const app = express();
const PORT = 1245;
const client = createClient();

const listProducts = [
  { 'Id': 1, 'name': 'Suitcase 250', 'price': 50, 'stock': 4 },
  { 'Id': 2, 'name': 'Suitcase 450', 'price': 100, 'stock': 10 },
  { 'Id': 3, 'name': 'Suitcase 650', 'price': 350, 'stock': 2 },
  { 'Id': 4, 'name': 'Suitcase 1050', 'price': 550, 'stock': 5 }
];

const getItemById = (id) => {
  return listProducts[id - 1];
};

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock, (err) => {
    if (err) {
      console.error(`Error reserving stock for item ${itemId}: ${err}`);
    } else {
      console.log(`Stock reserved for item ${itemId}`);
    }
  });
};

const getCurrentReservedStockById = async (itemId) => {
  return await new Promise((resolve, reject) => {
    client.get(itemId, (err, item) => {
      if (err) {
        reject(err);
      } else {
        resolve(item);
      }
    });
  });
};

app.get('/list_products', (req, res) => {
  const data = [];
  for (let i = 1; i <= listProducts.length; i++) {
    data.push(getItemById(i));
  }
  res.json(data);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;

  try{
    const reservedStock = await getCurrentReservedStockById(itemId);
    const item = getItemById(itemId);
    const itemResponse = {
      'itemId': item.Id,
      'itemName': item.name,
      'price': item.price,
      'initialAvailableQuantity': item.stock,
      'currentQuantity': reservedStock
    };
    res.json(itemResponse);
  } catch (err) {
    res.json({"status":"Product not found"});
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);
  if (!item) {
    res.json({"status":"Product not found"});
  }

  if (!item.stock >= 1) {
    res.json({"status":"Not enough stock available","itemId":1});
  }

  reserveStockById(item.Id, item.stock);
  res.json({"status":"Reservation confirmed","itemId": item.Id});
});

app.listen(PORT, () => {
  console.log(`Express app listening on port ${PORT}`);
});
