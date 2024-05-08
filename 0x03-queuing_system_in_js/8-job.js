function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (let i = 0; i < jobs.length; i++) {
    const jobData = jobs[i];

    queue
      .create('push_notification_code_3', jobData)
      .save((job, err) => {
        if (!err) {
	  console.log(`Notification job created: ${job.id}`);
        }
      })
      .on('progress', (job, progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      })
      .on('complete', (job) => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (job, err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      });
  }
}
