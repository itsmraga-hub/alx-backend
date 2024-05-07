import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient({ host: 'localhost', port: 6379 });

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

var key = "HolbertonSchools";

client
  .MULTI()
  .HSET(key, 'Portland', 50, redis.print)
  .HSET(key, 'Seattle', 80, redis.print)
  .HSET(key, 'New York', 20, redis.print)
  .HSET(key, 'Bogota', 20, redis.print)
  .HSET(key, 'Cali', 40, redis.print)
  .HSET(key, 'Paris', 2, redis.print)
  .EXEC();

client.HGETALL('HolbertonSchools', (err, hashset) => {
  console.log(hashset);
});
