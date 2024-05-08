const queue = require('kue').createQueue();

//const { createPushNotificationsJobs } = require('./8-job.js');
import createPushNotificationsJobs from './8-job.js';

before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});

it('Tests creation of a job', function() {
  createPushNotificationsJobs(list, queue);
  expect(queue.testMode.jobs.length).to.equal(1);
  expect(queue.testMode.jobs[0].data).to.eql(
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });
});
