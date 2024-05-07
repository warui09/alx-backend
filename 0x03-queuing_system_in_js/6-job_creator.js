const kue = require('kue');
const queue = kue.createQueue();

const jobDataFormat = { phoneNumber: String, message: String };
const jobObject = { phoneNumber: '1234567890', message: 'Hello, world!' };

const pushNotificationQueue = kue.createQueue();

const job = pushNotificationQueue.create('notification', jobObject);
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
