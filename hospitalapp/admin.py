from django.contrib import admin
# from adminapp.models import Doctor
from .models import Doctor,SlotRequest, SlotAllocation, Room, Prescription, Specialization

# Register your models here.
admin.site.register(Doctor)
admin.site.register(SlotRequest)
admin.site.register(SlotAllocation)
admin.site.register(Room)
admin.site.register(Prescription)
admin.site.register(Specialization)

