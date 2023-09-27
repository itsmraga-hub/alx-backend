import redis from 'redis';

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

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (error, value) => {
    if (error) {
      console.error(`Error getting value for key ${schoolName}: ${error}`);
    } else {
      console.log(`${value}`);
    }
  });
};
/* setTimeout(() => {
  client.quit();
}, 5000);
*/

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

// client.quit();
