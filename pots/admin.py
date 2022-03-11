from django.contrib import admin
from .models import User
from .models import Plant
from .models import Pest
from .models import Imgae
from .models import State
admin.site.register(User)
admin.site.register(Plant)
admin.site.register(Pest)
admin.site.register(Imgae)
admin.site.register(State)
