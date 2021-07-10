from django.conf.urls import url, include


app_name = "api"


urlpatterns = [
    # Route API end-points
    url(app_name + r'/tender/', include('apps.api.urls.tender')),
]
