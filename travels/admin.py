from django.contrib import admin

# Register your models here.
from travels.models import Destination
from travels.models import Entry,Tips,Image_Entry

admin.site.register(Destination)
admin.site.register(Entry)
admin.site.register(Image_Entry)
admin.site.register(Tips)