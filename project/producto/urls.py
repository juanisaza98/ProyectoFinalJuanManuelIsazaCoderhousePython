from django.urls import path

app_name = "producto"

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("categoria/create/", views.categoria_create, name="categoria_create"),
    # path("producto/create/", views.producto_create, name="producto_create"),
    path("producto/create/", views.ProductoCreate.as_view(), name="producto_create"),
    # path("producto/detail/<int:pk>", views.producto_detail, name="producto_detail"),
    path("producto/detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    # path("producto/update/<int:pk>", views.producto_update, name="producto_update"),
    path("producto/update/<int:pk>", views.ProductoUpdate.as_view(), name="producto_update"),
    # path("producto/delete/<int:pk>", views.producto_delete, name="producto_delete"),
    path("producto/delete/<int:pk>", views.ProductoDelete.as_view(), name="producto_delete"),
]
