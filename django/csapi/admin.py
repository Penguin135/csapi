from django.contrib import admin
from .models import OriginImage
from .models import SeparatedImage

admin.site.register(OriginImage)
admin.site.register(SeparatedImage)
