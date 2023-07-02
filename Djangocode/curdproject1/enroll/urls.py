from .import views
from django.urls import path

urlpatterns = [
    path('',views.add_show,name="addandshow"),
    path('<int:id>', views.update_data,name="updatedata"),
    path('delete/<int:id>', views.delete_data,name="deletedata"),

]