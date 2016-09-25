from rest_framework.routers import DefaultRouter
from apps.cafe.views import CafeViewset

router = DefaultRouter(trailing_slash=False)
router.register(r'cafes',
                CafeViewset,
                base_name='cafe')

urlpatterns = router.urls
