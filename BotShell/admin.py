from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from .import models
from .models import AllEmployment

class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        #for app in app_list:
        #    app['models'].sort(key=lambda x: x['name'])

        return app_list
admin.site = MyAdminSite()

class AllEmploersSite(admin.ModelAdmin):
    from django.db import models

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    #model = models.Requests
    list_display = ['pk', 'fio', 'phone_num', 'mail', 'id_tele']


class SpecialistSite(admin.ModelAdmin):
    filter_horizontal = ('teamLeader', 'colleagues')
    #model = models.Requests


    list_display = ['pk', 'fio', 'markStart', 'markEnd']


class ManagerSite(admin.ModelAdmin):
    #from django.db import models
    filter_horizontal = ('teamLeader', 'colleagues', 'employers')
  #  formfield_overrides = {
  #      models.ManyToManyField: {'widget': CheckboxSelectMultiple},
  #  }
    #model = models.Requests
    list_display = ['pk', 'fio', 'markStart', 'markEnd']


class TopManagerSite(admin.ModelAdmin):
    #from django.db import models

    filter_horizontal = ('teamLeader', 'colleagues', 'employers')
    #formfield_overrides = {
   #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
   # }
    #model = models.Requests
    list_display = ['pk', 'fio', 'markStart', 'markEnd']

class MY_CHOICESSite(admin.ModelAdmin):
    ist_display = ['pk', 'choice']
    from django.db import models
    formfield_overrides = {
          models.ManyToManyField: {'widget': CheckboxSelectMultiple},
      }
class DeadLinesSite(admin.ModelAdmin):
    list_display = ['pk', 'dead_line']

class MailingRateSite(admin.ModelAdmin):
    list_display = ['pk', '__str__', 'mail_rate', 'time_from_last_mail']

class Messagedmin(admin.ModelAdmin):
    list_display = ['__str__', 'msg_id']


admin.site.register(models.AllEmployment, AllEmploersSite)
admin.site.register(models.Specialist, SpecialistSite)
admin.site.register(models.Manager, ManagerSite)
admin.site.register(models.TopManager, TopManagerSite)
#admin.site.register(models.MY_CHOICES, MY_CHOICESSite)
#admin.site.register(models.DeadLines, DeadLinesSite)
admin.site.register(models.Message, Messagedmin)
admin.site.register(models.MailingRate, MailingRateSite)

class TeamLeaderSite(admin.ModelAdmin):
    from django.db import models
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    #model = models.Requests
    list_display = ['pk', 'fio', 'phone_num', 'mail', 'id_tele']

class EmploymentSite(admin.ModelAdmin):
    from django.db import models
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    #model = models.Requests
    list_display = ['pk', 'fio', 'phone_num', 'mail', 'id_tele']

class HrSite(admin.ModelAdmin):
    from django.db import models
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
   # model = models.Requests
    list_display = ['pk', 'fio', 'phone_num', 'mail', 'id_tele']



class ColleagueSite(admin.ModelAdmin):
    list_display = ['pk', 'fio', 'phone_num', 'mail', 'id_tele']

class MailingSite(admin.ModelAdmin):
    list_display = ['__str__']


admin.site.register(models.Mailing, MailingSite)
#admin.site.register(models.TeamLeader, TeamLeaderSite)
#admin.site.register(models.Employment, EmploymentSite)
#admin.site.register(models.Сolleague, ColleagueSite)
#admin.site.register(models.Hr, HrSite)
'''class FilmsAdminSite(admin.ModelAdmin):
    model = models.Requests
    list_display = ['pk', 'film_name', 'year', 'rating', 'likes', 'dislikes', 'comments_counter', 'watches24h']


class UsersAdminSite(admin.ModelAdmin):
    model = models.Requests
    list_display = ['pk', 'name', 'id_tele']


class RequestsAdminSite(admin.ModelAdmin):
    model = models.Requests
    fields = ['film_name', 'verification_process', 'id_tele']
    list_display = ['pk', 'film_name', 'verification_process', 'id_tele']
    actions = ['in_process_verification', 'apply_verification', 'canceled_verification']

    def in_process_verification(self, request, queryset):
        queryset.update(verification_process='🔄')

    def apply_verification(self, request, queryset):
        queryset.update(verification_process='✅')

    def canceled_verification(self, request, queryset):
        queryset.update(verification_process='⛔️')

class GenresAdmin(admin.ModelAdmin):
    list_display = ['pk', 'genre_name']
    list_editable = ['genre_name']


class Messagedmin(admin.ModelAdmin):
    list_display = ['__str__', 'msg_id']
   # list_editable = ['film_name']


admin.site.register(models.Films, FilmsAdminSite)
admin.site.register(models.Genres)
admin.site.register(models.Comments)
admin.site.register(models.Users, UsersAdminSite)
admin.site.register(models.Requests, RequestsAdminSite)
admin.site.register(models.Message, Messagedmin)
admin.site.register(models.Admins)
admin.site.register(models.Directors)
admin.site.register(models.Stars)
admin.site.register(models.GeneralHistory)
admin.site.register(models.TrendingFilms)
admin.site.register(models.LastSearch)'''