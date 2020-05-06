from django.contrib import admin

# Register your models here.
from .models import newarrival

admin.site.register(newarrival)


from .models import womenshirt

admin.site.register(womenshirt)


from .models import menshirt

admin.site.register(menshirt)


from .models import womentrouser

admin.site.register(womentrouser)


from .models import mentrouser
admin.site.register(mentrouser)


from .models import equipment
admin.site.register(equipment)

from .models import contactForm
admin.site.register(contactForm)

from .models import order
admin.site.register(order)