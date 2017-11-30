from django.conf.urls import url

from . import views

app_name = "clinic"

urlpatterns = [
      url(r'^$', views.login, name='login')
    , url(r'^login/', views.login, name='login')
    , url(r'^logout/', views.logout, name='logout')

    , url(r'^CRM-DentalClinic-Overview',views.crm_dentalclinic_overview, name='CRM-DentalClinic-Overview')
    , url(r'^CRM-ContactCenter-Overview',views.crm_contactcenter_overview, name='CRM-ContactCenter-Overview')
    , url(r'^CRM-OpenChannel-Overview',views.crm_openchannel_overview, name='CRM-OpenChannel-Overview')
    , url(r'^CRM-OrderManagement-Overview',views.crm_ordermanagement_overview, name='CRM-OrderManagement-Overview')

    , url(r'^calendar-index',views.calendar_index, name='calendar-index')
    , url(r'^inventory-index',views.inventory_index, name='inventory-index')
    , url(r'^hr-index',views.hr_index, name='hr-index')


# For AJAX
    , url(r'^get-appointment-schedule',views.get_appointment_schedule, name='get-appointment-schedule')
    , url(r'^ajax-get-appointment-modal',views.ajax_get_appointment_modal, name='ajax-get-appointment-modal')
    , url(r'^ajax-change-status-appointment',views.ajax_change_status_appointment, name='ajax-change-status-appointment')

# For Function
    , url(r'^create-new-customer',views.create_new_customer, name='create-new-customer')
]
