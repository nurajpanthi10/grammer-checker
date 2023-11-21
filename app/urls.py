from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("paraphrasing/", views.paraphrasing, name="paraphrasing"),
    path(
        "grammar-spell-checker/",
        views.grammar_spell_checker,
        name="grammar_spell_checker",
    ),
]
