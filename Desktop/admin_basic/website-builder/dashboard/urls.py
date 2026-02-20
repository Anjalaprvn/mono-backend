from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("plots/", views.plots_list, name="plots_list"),
    path("plots/add/", views.plot_add, name="plots_add"),
    path("plots/edit/<int:pk>/", views.plot_edit, name="plots_edit"),
    path("plots/view/<int:pk>/", views.plot_view, name="plots_view"),
    path("enquiry/", views.enquiry_list, name="enquiry_list"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/add/", views.blog_add, name="blog_add"),
    path("blog/view/", views.blog_view, name="blog_view"),
    path("payment/", views.payment_history, name="payment_history"),
    path("token/", views.token_management, name="token_management"),
    path("leads/", views.lead_management, name="lead_management"),
    path("matching/", views.matching_engine, name="matching_engine"),
]
