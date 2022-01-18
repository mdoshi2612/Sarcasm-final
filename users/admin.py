from django.contrib import admin
from .models import Team, Level
# Register your models here.
# class PlayerAdmin(admin.ModelAdmin):
# 	list_display = ('user', 'current_level', 'current_level_time','points', 'bonus_attempted')
# class userdataadmin(admin.ModelAdmin):
# 	list_display=('username','email','roll','referral_count')
# admin.site.register( userdata, userdataadmin)

class TeamAdmin(admin.ModelAdmin):
	list_display = ('leader_name', 'leader_roll_number')

admin.site.register(Team, TeamAdmin)
admin.site.register(Level)