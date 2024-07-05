from django.urls import path, include
from . import views
from .views import AccountDetail, Deposit
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('accounts', views.AccountViewSet)
router.register('transfer', views.TransferViewSet, basename='transfer')

urlpatterns = [
    # 1. helps generate urls
    path('', include(router.urls)),
    path('deposits', views.Deposit.as_view()),
    path('withdrawals', views.WithdrawalView.as_view()),
    path('checkbalance', views.check_balance.as_view())

    #  2. for function based view
    # path('accounts', views.ListAccount.as_view()),
    # 3. for class base view
    # # path('accounts', views.list_account),
    # 4. for function base view
    # path('accounts/<str:pk>', AccountDetail.as_view),
    # 5. for class base view
    # # path('accounts/<str:pk>', views.account_details)

]
