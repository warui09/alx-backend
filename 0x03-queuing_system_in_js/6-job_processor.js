const kue = require('kue');
const queue = kue.createQueue();

function sendNotification (phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('notification', (job, done) => {
  const { phoneNumber, message } = job.data;

  try {
    sendNotification(phoneNumber, message);
    done();
  } catch (err) {
    done(err);
  }
});
