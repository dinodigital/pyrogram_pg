from apscheduler.schedulers.background import BackgroundScheduler

from jobs.sample_job import job

# Jobs
scheduler = BackgroundScheduler()
scheduler.add_job(job, "interval", seconds=3)
