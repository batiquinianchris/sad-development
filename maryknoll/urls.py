from django.conf.urls import url

from . import views

app_name = 'maryknoll'

#cashier urls:
urlpatterns = [
        
        #index - login
        url(r'^$', views.IndexView.as_view(), name='index'),
        
        url(r'^cashier/$', views.Cash_Dashboard.as_view(), name='cashier-home'),
        
        url(r'^financial_records/$', views.Cash_FinancialRec.as_view(), name='financial-record'),
        
        url(r'^user_records/$', views.Cash_UserRec.as_view(), name='user-record'),
        
        url(r'^promissory/$', views.Form_Promissory.as_view(), name='promissory'),
]