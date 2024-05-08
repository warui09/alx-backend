const kue = require('kue');
const queue = kue.createQueue();
const push_notification_code_2 = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

for (let i = 0; i < jobs.length; i++) {
  push_notification_code_2
    .create('notification', jobs[i])
    .save((job, err) => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    })
    .on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    })
    .on('complete', (job) => {
      console.log(`Notification job ${job.id} completed`);
    })
    .on('failed', (job, err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });
}
