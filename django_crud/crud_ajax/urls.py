from django.urls import path
from crud_ajax import  views

urlpatterns = [
    path('',  views.CrudView.as_view(), name='crud_ajax'),
    path('create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('user_create/',  views.CreateCrudUser.as_view(), name='crud_ajax_user_create'),
    path('update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
]
