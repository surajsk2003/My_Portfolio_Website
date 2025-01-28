from django.db import models

class AboutMe(models.Model):
    title = models.CharField(max_length=100, default="About Me")
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)  # Optional project link (e.g., GitHub)

    def __str__(self):
        return self.title
