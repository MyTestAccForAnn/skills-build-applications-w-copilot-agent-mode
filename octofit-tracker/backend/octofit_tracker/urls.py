from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet, api_root


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboards', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

import os
codespace_name = os.environ.get('CODESPACE_NAME', '')

urlpatterns = [
    path('', f"https://{codespace_name}-8000.app.github.dev/api/", name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
