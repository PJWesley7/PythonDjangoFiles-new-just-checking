from django.db import models

class JobsInfo(models.Model):
    recruiter_name = models.CharField(max_length=255)
    job_id = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.recruiter_name} - {self.job_id}'