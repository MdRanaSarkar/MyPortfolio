from django.contrib import admin
from django.http import HttpResponseRedirect
from embed_video.admin import AdminVideoMixin
from RanaProtfolio.models import Item

# Register your models here.
from RanaProtfolio.models import Specialization,WorkingCategory,Service,WorkingProtfolio,Working_Experience,Contact

class SpecializationAdmin(admin.ModelAdmin):
	list_display=['specialized_field','ranking']
	search_field=['specialized_field']
admin.site.register(Specialization,SpecializationAdmin)


admin.site.register(WorkingCategory)
class ServicesAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at', 'updated_at']


admin.site.register(Service,ServicesAdmin)


class WorkingProtfolioAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at', 'updated_at']
admin.site.register(WorkingProtfolio,WorkingProtfolioAdmin)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)



class Working_ExperienceAdmin(admin.ModelAdmin):
	list_display = ['w_category','W_area', 'w_start_date', 'w_stop_date']

admin.site.register(Working_Experience, Working_ExperienceAdmin)



class ContactAdmin(admin.ModelAdmin):
	list_display = ['name','email', 'subject', 'status','created_at','updated_at']
admin.site.register(Contact,ContactAdmin)