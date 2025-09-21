from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

# Register your models here.
class UserModelAdmin(UserAdmin):
    model = User
    #The fields to be used in displaying the user model
    #these override the definations on the base UserModelAdmin
    #that reference  specific fields on auth.User.
    list_display = ['id','email','name','is_active','is_superuser','is_staff','is_customer','is_seller']

    list_filter = ['is_superuser']

    fieldsets = [
        ("User Credentisls",{"fields":["email","password"]}),
        ("User Information",{"fields":["name","city"]}),
        ("Permissions",{"fields":["is_active","is_staff","is_superuser","is_customer","is_seller","groups","user_permissions"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                #its css class to make full width admin layout
                "classes":["wide"],
                #this fields will apear in admin panel add user form
                "fields":["email","password1","password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["id","email"]
    filter_horizontal = ["groups","user_permissions"]

# Now register the new UserModelAdmin
admin.site.register(User,UserModelAdmin)
