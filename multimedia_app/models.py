



from django.db import models

class MultimediaFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media_files/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
