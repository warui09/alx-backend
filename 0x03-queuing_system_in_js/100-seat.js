const express = require('express');
import { createClient } from 'redis';
const { promisify } = require('util');
const queue = require('kue').createQueue;
const app = express();
const PORT = 1245;
const client = createClient();
const available_seats = 50;
const reservationEnabled = true;

const reserveSeat = (number) => {
  return new Promise((resolve, reject) => {
    client.get('available_seats', (err, availableSeats) => {
      if (err) {
        console.error(`Error retrieving available seats: ${err}`);
        reject(err);
        return;
      }

      const newAvailableSeats = parseInt(availableSeats) - number;
      if (newAvailableSeats < 0) {
        console.error('Not enough seats available');
        reject(new Error('Not enough seats available'));
        return;
      }

      client.set('available_seats', newAvailableSeats.toString(), (err) => {
        if (err) {
          console.error(`Error reserving ${number} seats`);
          reject(err);
        } else {
          console.log(`Reserved ${number} seats`);
          resolve();
        }
      });
    });
  });
};

const getCurrentAvailableSeats = async () => {
  const getAsync = promisify(client.get).bind(client);
  return await getAsync('available_seats');
};

app.get('/available_seats', (req, res) => {
  res.json({"numberOfAvailableSeats": `${available_seats}`});
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ "status": "Reservation are blocked" });
  }

  queue
    .create('reserve_seat', { seatNumber: 1, availableSeats: available_seats })
    .save((err) => {
      if (!err) {
        res.json({ "status": "Reservation in process" });
      } else {
        res.json({ "status": "Reservation failed" });
      }
    })
    .on('complete', (job) => console.log(`Seat reservation job ${job.id} completed`))
    .on('failed', (job, err) => console.log(`Seat reservation job ${job.id} failed: ${err}`));
});

app.get('/process', (req, res) => {
  res.json({ "status": "Queue processing" });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      reserveSeat(1, availableSeats - 1);
      done();
    }
  });
});

app.listen(PORT, () => {
  console.log(`Express app listening on port ${PORT}`);
});
