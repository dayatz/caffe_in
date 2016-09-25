from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from apps.cafe.views import CafeViewset, MenuViewset, GalleryViewset

router = DefaultRouter(trailing_slash=False)
router.register(r'cafes',
                CafeViewset,
                base_name='cafe')

cafe_nested_router = NestedSimpleRouter(router, r'cafes', lookup='cafe')
cafe_nested_router.register(r'menus', MenuViewset, base_name='menu')
cafe_nested_router.register(r'galleries', GalleryViewset, base_name='gallery')

urlpatterns = router.urls + cafe_nested_router.urls
