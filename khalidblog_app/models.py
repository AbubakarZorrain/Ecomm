from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.IntegerField(unique=True, auto_created=True, primary_key=True)

    title= models.CharField(max_length=300, unique=True)
    url= models.SlugField(max_length=300)
    content= models.TextField(max_length=1500)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    author= models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return 'Author : '+str(self.author)+'TiTle' + str(self.title) + 'Dated :' + str(self.pub_date)