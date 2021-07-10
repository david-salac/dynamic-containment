from rest_framework.routers import SimpleRouter

from apps.api.views import tender

app_name = "tender"

router = SimpleRouter()
router.register(r'auction-results',
                tender.AuctionResultsViewSet,
                basename='auction-results')

urlpatterns = []
urlpatterns += router.urls
