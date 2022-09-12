from django.urls import path
from . import views

urlpatterns=[
    path('createadmin',views.AdminView.as_view()),
    path('loginadmin',views.LoginAdmin.as_view()),
    path('getadmin',views.get_admin),
    path('updateadmin',views.update_admin),
    path('allbooks',views.get_books),
    path('createbook',views.create_book),
    path('updatebook',views.update_book),
    path('deletebook',views.delete_book),

]