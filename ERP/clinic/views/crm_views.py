from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from clinic.models import User
from django.contrib import messages
from django.db import connection

from collections import namedtuple

from .static_variable import CONSTANT_KEY
import logging
import datetime

LOGGER = logging.getLogger("ERP")
CURRENT_DATE = datetime.date.today().strftime('%d-%m-%Y')


def crm_dentalclinic_overview(request):
    if request.session.has_key('user_name'):

        # lstCusToday = CalendarAppointment.object.filter(dateAppointment=datetime.date.today())


        sql  =      "   SELECT"
        sql +=      "     appointment_id"
        sql +=      "   , clinic_customer.customer_id"
        sql +=      "   , customer_name"
        sql +=      "   , customer_phone_number"
        sql +=      "   , appointment_time"
        sql +=      "   , appointment_content"
        sql +=      "   , appointment_status"
        sql +=      "   FROM"
        sql +=      "         clinic_customer"
        sql +=      "   INNER JOIN"
        sql +=      "         clinic_appointment"
        sql +=      "   ON"
        sql +=      "       clinic_customer.customer_id = clinic_appointment.customer_id"
        sql +=      "   WHERE"
        sql +=      "           appointment_date = '{}'".format(CURRENT_DATE)
        if request.session['role'] == '1':
            sql +=  "       AND appointment_assign_id = '{}'".format(request.session['user_id'])
        sql +=      "       AND appointment_delete_flag = '{}'".format(CONSTANT_KEY['DELETE_FLAG_FALSE'])
        sql +=      "   ORDER BY"
        sql +=      "         appointment_status"
        sql +=      "       , appointment_time"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            lstCusToday = namedtuplefetchall(cursor)
        # print(lstCusToday)

        lstAppointment = []
        if lstCusToday != []:
            selected_customer = lstCusToday[0]
            sql  =      "    SELECT"
            sql +=      "          appointment_id"
            sql +=      "        , user_name AS assign_name"
            sql +=      "        , appointment_date"
            sql +=      "        , appointment_time"
            sql +=      "        , treatment_name"
            sql +=      "        , appointment_content"
            sql +=      "        , appointment_note"
            sql +=      "    FROM"
            sql +=      "        clinic_appointment"
            sql +=      "    INNER JOIN"
            sql +=      "            clinic_user"
            sql +=      "        ON"
            sql +=      "            clinic_user.user_id = clinic_appointment.appointment_assign_id"
            sql +=      "    INNER JOIN"
            sql +=      "            clinic_treatment"
            sql +=      "        ON"
            sql +=      "            clinic_treatment.treatment_id = clinic_appointment.treatment_id"
            sql +=      "    WHERE"
            sql +=      "                clinic_appointment.customer_id = {}".format(selected_customer.customer_id)
            sql +=      "        AND     appointment_delete_flag = '{}'".format(CONSTANT_KEY['DELETE_FLAG_FALSE'])
            sql +=      "    ORDER BY"
            sql +=      "        CAST   (appointment_date AS DATE) ASC"
            sql +=      "        ,      appointment_time ASC"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                lstAppointment = namedtuplefetchall(cursor)



        context = {
              'user_name' : request.session['user_name']
            , 'user_role' : request.session['user_role']
            , 'lstCusToday' : lstCusToday
            , 'lstAppointment' : lstAppointment
            , 'appointment_status' : CONSTANT_KEY
        }

        return render(request,"clinic/crm_dentalclinic_overview.html", context)
    else:
        return HttpResponseRedirect('/login/')
    # return render(request,"clinic/crm_dentalclinic_overview.html")

def crm_contactcenter_overview(request):
    return render(request,"clinic/crm_contactcenter_overview.html")

def crm_openchannel_overview(request):
    return render(request,"clinic/crm_openchannel_overview.html")

def crm_ordermanagement_overview(request):
    return render(request,"clinic/crm_ordermanagement_overview.html")


# internal function
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]