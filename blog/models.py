from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.

# creating catogory model
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    discription = models.TextField()
    urls=models.CharField(max_length=100)
    image =models.ImageField(upload_to="category/")
    add_date = models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self):
        return format_html('<img src = "/media/{}" style= "width:50px;hight:70px; border-radius:50% "'.format(self.image))
    def __str__(self):
        return self.title
    #post models
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = HTMLField()
    url = models.CharField( max_length=100)
    cat =models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField( upload_to="post/", height_field=None, width_field=None, max_length=None)
    def image_tag(self):
        return format_html('<img src = "/media/{}" style= "width:50px;hight:70px; border-radius:50% "'.format(self.image))
    def __str__(self):
        return self.title