from django.urls import path


from . import views

app_name = 'compile'
urlpatterns = [
    path('insert_ten_thousand_task', views.insert_ten_thousand_task),
    path('task_list', views.task_list),
]
