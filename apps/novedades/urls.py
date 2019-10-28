from django.urls import include, path 
from rest_framework import routers 
from .views import NovedadViewSet, IndexView, NovedadDetail, NovedadCreate, NovedadUpdate, NovedadDelete

router = routers.DefaultRouter()
router.register('novedades', NovedadViewSet)

app_name = 'novedades'

urlpatterns = [
	path('api/', include(router.urls)),
	path('', IndexView.as_view(), name="index"),
	path(
    	route='detalle/<int:pk>',
    	view=NovedadDetail.as_view(),
    	name='detalle'
    ),
    path(
    	route='novedad/create/',
    	view=NovedadCreate.as_view(),
    	name='novedad_create'
    ),
    path(
    	route='novedad/update/<int:pk>',
    	view=NovedadUpdate.as_view(),
    	name='novedad_update'
    ),
    path(
    	route='novedad/delete/<int:pk>',
    	view=NovedadDelete.as_view(),
    	name='novedad_delete'
    ),
]
