from django.db import models

# Create your models here.
class courses(models.Model):
    title = models.CharField(max_length=50)
    course_video =  models.FileField(upload_to="courses/videos",max_length=100,default=" ")
    course_pdf = models.FileField(upload_to="courses/pdf",max_length=100)

    def __str__(self):
        return self.title

    def delete(self,*args, **kwargs):
        self.course_video.delete()
        self.course_pdf.delete()
        super().delete(*args, **kwargs)
    