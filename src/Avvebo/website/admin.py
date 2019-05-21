from django.contrib import admin
import Avvebo.website.models as mods

# Register your models here.
myModels=[mods.User,mods.Venue,mods.SocialMedia,mods.TalentContent,mods.AvveboProfile]
admin.site.register(myModels)
