from django.contrib import admin
from .models import Profil
from .models import Tanecnik
from .models import Zavod
from .models import Tanecni_jednotka
from .models import Prihlaska_zavod

# Register your models here.


admin.site.register(Profil)
admin.site.register(Tanecnik)
admin.site.register(Zavod)
admin.site.register(Tanecni_jednotka)
admin.site.register(Prihlaska_zavod)