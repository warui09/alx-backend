import { createClient, print } from 'redis';

const client = createClient();
const schoolName = 'HolbertonSchools';

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

client.hset(schoolName, 'Portland', '50', print);
client.hset(schoolName, 'Seattle', '80', print);
client.hset(schoolName, 'New York', '20', print);
client.hset(schoolName, 'Bogota', '20', print);
client.hset(schoolName, 'Cali', '40', print);
client.hset(schoolName, 'Paris', '2', print);

client.hgetall(schoolName, (err, schools) => {
  if (err) {
    console.log(`Error getting schools: ${err}`);
  } else {
    console.log(schools);
  };
});
