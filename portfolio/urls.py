from django.urls import path
from .views import PortfolioListView, PortfolioCreateView, PortfolioUpdateView, PortfolioDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio_list'),
    path('create/', PortfolioCreateView.as_view(), name='portfolio_create'),
    path('update/<int:pk>/', PortfolioUpdateView.as_view(), name='portfolio_update'),
    path('delete/<int:pk>/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)