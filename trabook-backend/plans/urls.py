from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from plans import views

# App configuration
app_name = 'plans'

# Router
router = routers.DefaultRouter()
router.register(r'plans', views.PlanView, basename='plans')

# Api and docs
urlpatterns = [
    path("api/", include(router.urls)),
    path("docs/plans/", include_docs_urls(title = "Plan API"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)