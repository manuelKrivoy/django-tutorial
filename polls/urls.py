from django.urls import path


from . import views
# defino donde mostrar las vistas
app_name = "polls" # nombre de la aplicación
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]