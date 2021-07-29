from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from apps.api.views import tender

app_name = "tender"

router = SimpleRouter()
router.register(r'auction-results',
                tender.AuctionResultsViewSet,
                basename='auction-results')

urlpatterns = [
    url(
        r'^tiles',
        tender.Tiles.as_view({'get': 'list'}),
        name='tiles'
    ),
]
urlpatterns += router.urls
