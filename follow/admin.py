from django.contrib import admin
from follow.models import Job, Project

# # Register your models here.
class JobAdmin(admin.ModelAdmin):
#
     list_display = ['subject', 'assigned', 'status', 'tracker', 'start_date', 'end_date']
     list_display_links = ['subject']
     list_filter = ['status', 'tracker', 'assigned_to']
     search_fields = ['subject', 'assigned_to']
     # list_editable = ['atanan']
#
     class Meta:
         model = Job
#
admin.site.register(Job, JobAdmin)

class ProjectAdmin(admin.ModelAdmin):

     list_display = ['project_name', 'users']
     list_display_links = ['project_name', 'users']
     # list_filter = ['project_name', 'members']
     # search_fields = ['project_name', 'members']

     class Meta:
          model = Project

admin.site.register(Project, ProjectAdmin)
