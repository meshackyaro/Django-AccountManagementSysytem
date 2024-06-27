from django.urls import path, include
from . import views
from .views import AccountDetail
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('accounts', views.AccountViewSet)

urlpatterns = [
    # 1. helps generate urls
    path('', include(router.urls)),
    path('deposits', views.deposit),
    path('withdrawals', views.withdrawal)
    #  2. for function based view
    # path('accounts', views.ListAccount.as_view()),
    # 3. for class base view
    # # path('accounts', views.list_account),
    # 4. for function base view
    # path('accounts/<str:pk>', AccountDetail.as_view),
    # 5. for class base view
    # # path('accounts/<str:pk>', views.account_details)

]
