import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient({ host: 'localhost', port: 6379 });

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// client.quit();

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const res = await promisify(client.get).bind(client)(schoolName)
    console.log(`${res}`);
  } catch (e) {
    console.error(`${e}`);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
