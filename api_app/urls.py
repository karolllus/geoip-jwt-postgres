from django.urls import path, include
from api_app import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# # For generic API View - mixins
# urlpatterns = [
#     path('generic/<int:id>', views.GenericAPIView.as_view())
# ]


# For class based - API view
urlpatterns = [
    path('list/', views.geomodel_list.as_view()),
    path('detail/<int:id>', views.geomodel_detail.as_view())
]


## For decorators
# urlpatterns = [
#     path('list/', views.geomodel_list),
#     path('detail/<int:id>', views.geomodel_detail)
# ]

urlpatterns = format_suffix_patterns(urlpatterns)