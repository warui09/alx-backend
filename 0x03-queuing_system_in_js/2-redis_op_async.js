import { createClient, print } from 'redis';
const { promisify } = require('util');

const client = createClient();
const get = promisify(client.get).bind(client);

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try{
    const name = await get(schoolName);
    console.log(name);
  } catch (err) {
    console.log(`Error getting value for ${schoolName}: ${err}`);
  }
};

setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
