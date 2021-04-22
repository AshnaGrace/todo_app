from django.urls import path

from .import views

urlpatterns = [

          path('',views.task_view,name='task_view'),
          path('delete/<int:taskid>/', views.delete, name='delete'),
          path('update/<int:id>', views.update, name='update'),
      path('cbvtask/',views.TaskList.as_view(),name='cbvtask'),
path('cbvdetail/<int:pk>',views.TaskD.as_view(),name='cbvdetail'),
path('cbvupdate/<int:pk>',views.TaskU.as_view(),name='cbvupdate'),
path('cbvdelete/<int:pk>',views.Taskd.as_view(),name='cbvdelete')
    ]