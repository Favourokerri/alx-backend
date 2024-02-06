import { createClient, print } from 'redis';
import util from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const printAsync = util.promisify(print);

async function setNewSchool(schoolName, value) {
  try {
    await client.set(schoolName, value, printAsync);
  } catch (error) {
    console.log(error);
  }
}

async function displaySchoolValue(schoolName) {
  await client.get(schoolName, printAsync);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
