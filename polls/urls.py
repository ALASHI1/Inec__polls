from django.urls import path
from polls import views
urlpatterns = [
    path('', views.display_polling_units,name='polls'),
    path('lgas', views.display_lga,name='lgas'),
    path('registerpoll', views.register_new_polling_unit,name='registerpoll'),
    path('lgaresults/<int:lga_id>', views.display_lga_result,name='lgaresults'),
    path('result/<int:_id>', views.display_individual_result,name='result'),
    path('newresults', views.record_new_polling_result,name='newresults'),
    path('newresults/<int:uniqueid>', views.record_new_polling_result,name='newresults'),
]