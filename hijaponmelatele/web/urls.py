from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("parrilla/<str:public_name>/", views.view, name="view"),
    path("edit/<str:private_id>/", views.edit, name="edit"),
    path("edit/<str:private_id>/add", views.add_url, name="add-url"),
    path("remove/<str:private_id>/", views.remove_entry, name="remove-entry"),
    path("extract/", views.extract_metadata, name="extract"),
    path("create-config/", views.create_config, name="create-config"),
]
