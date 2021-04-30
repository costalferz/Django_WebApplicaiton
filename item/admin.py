from django.contrib import admin
from .models import Item,Category,itemHistory,Payment
# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name','category', 'detail','amount')
    fields = ('name','category', 'detail','amount','img')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fields = ('category', )

@admin.register(itemHistory)
class itemHistoryAdmin(admin.ModelAdmin):
    list_display = ('user','item','date','trackNum')
    fields = ('user','item','trackNum')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user','name','user','cvv','NumCard','expire')
    fields = ('name','cvv','NumCard','expire')