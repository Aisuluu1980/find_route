from django.contrib import admin

# Register your models here.
from trains.models import Train

class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    list_editable = ('travel_time',)    #по записям с внешними ключами лучше не добавлять в редактирование



admin.site.register(Train, TrainAdmin)

