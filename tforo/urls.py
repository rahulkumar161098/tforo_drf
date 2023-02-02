
from django.contrib import admin
from django.urls import path
from supplier import views
from supplier.views import( AddViewList1)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api', AddViewList1.as_view())
]
