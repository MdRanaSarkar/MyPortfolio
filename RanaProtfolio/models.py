from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from embed_video.fields import EmbedVideoField
from django.forms import ModelForm
# Create your models here.

#This model is used for Specialized Area
class Specialization(models.Model):
	specialized_field=models.CharField(max_length=200)
	ranking=models.IntegerField()

	def __str__(self):
		return self.specialized_field


class WorkingCategory(models.Model):
	category_name=models.CharField(max_length=200)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.category_name


class Service(models.Model):
	category=models.ForeignKey(WorkingCategory,on_delete=models.CASCADE)
	services_class=models.CharField(max_length=200)
	title=models.CharField(max_length=200)
	description=RichTextUploadingField()
	image=models.FileField(upload_to="services/",blank=True, null=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
		image_tag.short_description = 'Image'
	def imageurl(self):
		if self.image:
			return self.image.url
		else:
			return " "


#This is used for working working protfolio 
class Programming_tools(models.Model):
	tool=models.CharField(max_length=200)

	def __str__(self):
		return self.title




class WorkingProtfolio(models.Model):
	category=models.ForeignKey(WorkingCategory,on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	description=RichTextUploadingField()
	image=models.FileField(upload_to="services/",blank=True, null=True)
	client=models.CharField(max_length=200)
	projects_link=models.CharField(max_length=300)
	deleiveri_data=models.DateField()
	location=models.CharField(max_length=200)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
		image_tag.short_description = 'Image'
	def imageurl(self):
		if self.image:
			return self.image.url
		else:
			return " "


#This class is used for youtube videos
class Item(models.Model):
    video = EmbedVideoField()


#this class is used for working experience

class Working_Experience(models.Model):
	w_category=models.CharField(max_length=200)
	W_area=models.CharField(max_length=200)
	w_start_date=models.DateField()
	w_stop_date=models.DateField()
	w_comment=models.TextField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.w_category

	def yearstart(self):
		return self.w_start_date.strftime('%Y')

	def yearend(self):
		return self.w_stop_date.strftime('%Y')




#this is used for contact models
class Contact(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),

    )
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length = 254)
    subject = models.CharField(max_length=200, blank=True)
    comment = models.TextField(max_length=500, blank=True)
    ip = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class ContacttForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject', 'comment']

