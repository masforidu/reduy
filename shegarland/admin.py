from django.contrib import admin
from .models import ShegarLandForm  # Import your actual model

class ShegarLandFormAdmin(admin.ModelAdmin):
    list_display = (
        'magaalaa', 'aanaa', 'iddo_adda', 'lakk_adda', 
        'gosa_tajajila', 'madda_lafa', 'tajajila_iddo', 
        'haala_beenya', 'qamaa_qophaef', 'tajajila_qophaef', 
        'balina_lafa', 'kan_qophesse', 'guyya_qophae', 
        'shapefile', 'suura_iddoo',
    )
    search_fields = (
        'magaalaa', 'aanaa', 'iddo_adda', 'gosa_tajajila', 
        'madda_lafa', 'haala_beenya', 'qamaa_qophaef',
    )
    list_filter = ('gosa_tajajila', 'aanaa',)  # Add filters for easier searching

# Register your model with the admin interface
admin.site.register(ShegarLandForm, ShegarLandFormAdmin)
