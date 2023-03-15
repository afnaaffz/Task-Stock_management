from django.urls import path

from new_app import views

urlpatterns = [
   path("", views.index, name="index"),
   path("indexx", views.indexx, name="indexx"),
   path("login_page", views.login_page, name="login_page"),


   path("adminbase", views.adminbase, name="adminbase"),
   path("customers_data", views.customers_data, name="customers_data"),
   path("view_stock", views.view_stock, name="view_stock"),
   path("add_stock", views.add_stock, name="add_stock"),
   path("update/<int:id>/", views.update, name="update"),
   path("delete_stock/<int:id>/", views.delete_stock, name="delete_stock"),



   path("customerbase", views.customerbase, name="customerbase"),
   path("customer_register", views.customer_register, name="customer_register"),
   path("view_customers_data", views.view_customers_data, name="view_customers_data"),


   path("logout_view", views.logout_view, name="logout_view"),

]
