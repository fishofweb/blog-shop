from django.contrib import admin

# Register your models here.

from .models import Blogpost

admin.site.register(Blogpost)

# legs
from .models import leg

admin.site.register(leg)

# chest
from .models import chest1

admin.site.register(chest1)

# back
from .models import back

admin.site.register(back)

# fullbody
from .models import fullbody1

admin.site.register(fullbody1)
# bi
from .models import bicep1

admin.site.register(bicep1)

# tricep
from .models import tricep1

admin.site.register(tricep1)


# shoulder
from .models import shoulder1

admin.site.register(shoulder1)

# forearm
from .models import forearm1

admin.site.register(forearm1)

# shoulder
from .models import abs1

admin.site.register(abs1)
