from django.db import models
from django.contrib.auth.models import User


class ProjectManager(models.Manager):
    def get_queryset(self):
        return super(ProjectManager, self).get_queryset().filter(
            is_active=True)


class Project(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = ProjectManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.name


class WorkDone(models.Model):
    user = models.ForeignKey(User)
    minutes = models.IntegerField()
    description = models.CharField(max_length=255)
    project = models.ForeignKey(Project)

    def __str__(self):
        return "{user} worked {minutes} minutes on {project}".format(
            user=self.user.username,
            minutes=self.minutes,
            project=self.project.name
        )
