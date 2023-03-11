from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="",null=False,unique=True,db_index=True,editable=True)
    def __str__(self):
            return f"{self.name}"
    
# def save(self, *args, **kwargs):
#     self.slug = slugify(self.name)
#     super(Course, self).save(*args, **kwargs)


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="",null=False,unique=True,db_index=True,editable=True)
    category = models.ForeignKey(Category,default=5,on_delete=models.CASCADE)

    def __str__(self):
            return f"{self.title} {self.date}"
    
# def save(self, *args, **kwargs):
#     self.slug = slugify(self.name)
#     super(Course, self).save(*args, **kwargs)



