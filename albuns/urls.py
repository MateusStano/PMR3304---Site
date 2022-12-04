from django.urls import path

from . import views

app_name = 'albuns'
urlpatterns = [
    path('', views.AlbumListView.as_view(), name='index'),
    path('especialidades', views.AlbumListViewEspecialidades.as_view(), name='especialidades'),    
    path('consultasmarcadas', views.AlbumListViewconsultasmarcadas.as_view(), name='consultasmarcadas'),    
    path('create/', views.create_album, name='create'),
    path('<int:album_id>/', views.detail_album,
         name='detail'),
    path('update/<int:album_id>/', views.update_album, name='update'),
    path('delete/<int:album_id>/', views.delete_album, name='delete'),
    path('<int:album_id>/review/', views.create_review, name='review'),
    path('lists/', views.ListListView.as_view(), name='lists'),
]
