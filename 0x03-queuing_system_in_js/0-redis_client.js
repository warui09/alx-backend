import { createClient } from 'redis';

void async function () {    
  const client = createClient();

  client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
  client.on('connect', () => console.log('Redis client connected to the server'));
}();
