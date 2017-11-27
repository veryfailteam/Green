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

        sql  =      "   SELECT"
        sql +=      "     appointment_id"
        sql +=      "   , treatment_id"
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
        if request.session['user_role'] == '1':
            sql +=  "       AND appointment_assign_id = '{}'".format(request.session['user_id'])
        sql +=      "       AND appointment_status <> '{}'".format(CONSTANT_KEY['APPOINTMENT_STATUS_PAID'])
        sql +=      "       AND appointment_delete_flag = '{}'".format(CONSTANT_KEY['DELETE_FLAG_FALSE'])
        sql +=      "   ORDER BY"
        sql +=      "         appointment_status"
        sql +=      "       , appointment_time"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            lstCusToday = namedtuplefetchall(cursor)

        lstAppointment = []
        if lstCusToday != []:
            selected_customer = lstCusToday[0]
            lstAppointment = sql_get_appointment_schedule(selected_customer.customer_id)
        context = {
              'user_name' : request.session['user_name']
            , 'user_role' : request.session['user_role']
            , 'lstCusToday' : lstCusToday
            , 'lstAppointment' : lstAppointment
            , 'constant_key' : CONSTANT_KEY
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



# ajax function
def get_appointment_schedule(request):

    lstAppointment = sql_get_appointment_schedule(request.POST['customer_id'])
    context = {
              'user_name' : request.session['user_name']
            , 'user_role' : request.session['user_role']
            # , 'lstCusToday' : lstCusToday
            , 'lstAppointment' : lstAppointment
            , 'constant_key' : CONSTANT_KEY
        }
    return render(request,"clinic/crm_dentalclinic_overview_listappointment.html", context)


def ajax_get_appointment_modal(request):
    if request.method == 'POST':
        appointment_id = request.POST['appointment_id']
        treatment_id = request.POST['treatment_id']
        treatmentdetail_date = request.POST['treatmentdetail_date']
        data_type = request.POST['data_type']
        action = request.POST['action']
        if data_type == CONSTANT_KEY['DATA_TYPE_TREATMENT']:
            selected_treatmentdetail =  sql_get_treatmentdetails(treatment_id,treatmentdetail_date)
            # print("===================================================================" )
            # print(treatmentdetail)
            lst_user = sql_get_all_doctors_active()
            lst_treatmentdetail = sql_get_all_treatmentdetails(treatment_id)
            context = {
                  'main_info' : selected_treatmentdetail[0]
                , 'lst_user' : lst_user
                , 'lst_treatmentdetail': lst_treatmentdetail
                , 'constant_key' : CONSTANT_KEY
                , 'view_modal_mode': CONSTANT_KEY['VIEW_MODAL_MODE_TREATMENT']
            }
            return render(request,"clinic/crm_dentalclinic_overview_modal_appoinment.html", context)
        elif data_type == CONSTANT_KEY['DATA_TYPE_APPOINTMENT']:
            if 'view' == action:
                appointment_info = sql_get_appointment(appointment_id)
                lst_user = sql_get_all_doctors_active()
                lst_treatmentdetail = sql_get_all_treatmentdetails(treatment_id)
                appointmentdetails  = sql_get_appointmentdetails(appointment_id)
                context = {

                      'main_info': appointment_info[0]
                    , 'lst_user' : lst_user
                    , 'lst_treatmentdetail': lst_treatmentdetail
                    , 'constant_key' : CONSTANT_KEY
                    , 'view_modal_mode': CONSTANT_KEY['VIEW_MODAL_MODE_APPOINTMENT']
                    , 'selected_task': appointmentdetails
                }
                return render(request,"clinic/crm_dentalclinic_overview_modal_appoinment.html", context)
            if 'confirm' == action:
                context = {
                    'action': 'confirm'
                }
                return render(request,"error.html",context)
            if 'checked' == action:
                context = {
                    'action': 'checked'
                }
                return render(request,"error.html",context)
            if 'edit' == action:
                context = {
                    'action': 'edit'
                }
                return render(request,"error.html",context)
            if 'done' == action:
                context = {
                    'action': 'done'
                }
                return render(request,"error.html",context)


    return render(request,"clinic/crm_dentalclinic_overview_modal_appoinment.html")



# sql query
def sql_get_appointment_schedule(customer_id):

    sql  =       "(       "
    sql +=       "    (   "
    sql +=       "        SELECT  "
    sql +=       "              appointment_id                      AS id   "
    sql +=       "            , user_name                           AS assign_name  "
    sql +=       "            , appointment_date                    AS date "
    sql +=       "            , appointment_time                    AS time "
    sql +=       "            , clinic_treatment.treatment_id       AS treatment_id "
    sql +=       "            , treatment_name                      AS name "
    sql +=       "            , appointment_content                 AS content  "
    sql +=       "            , appointment_note                    AS note "
    sql +=       "            , appointment_status                  AS status   "
    sql +=       "            , '1'                                 AS data_type "
    sql +=       "        FROM    "
    sql +=       "            clinic_appointment  "
    sql +=       "        INNER JOIN  "
    sql +=       "                clinic_user "
    sql +=       "            ON  "
    sql +=       "                clinic_user.user_id = clinic_appointment.appointment_assign_id  "
    sql +=       "        INNER JOIN  "
    sql +=       "                clinic_treatment    "
    sql +=       "            ON  "
    sql +=       "                clinic_treatment.treatment_id = clinic_appointment.treatment_id "
    sql +=       "        WHERE   "
    sql +=       "                    clinic_appointment.customer_id = '{}'    ".format(customer_id)
    sql +=       "            AND     clinic_appointment.appointment_status <> '{}'    ".format(CONSTANT_KEY['APPOINTMENT_STATUS_PENDING_PAYMENT'])
    sql +=       "            AND     appointment_delete_flag = '{}'   ".format(CONSTANT_KEY['DELETE_FLAG_FALSE'])
    sql +=       "    )   "
    sql +=       "UNION ALL   "
    sql +=       "    (   "
    sql +=       "        SELECT  "
    sql +=       "              '-1'                                          AS id                   "
    sql +=       "            , clinic_user.user_name                         AS assign_name                  "
    sql +=       "            , treatmentdetail_date                          AS date             "
    sql +=       "            , treatmentdetail_time                          AS time                 "
    sql +=       "            , clinic_treatment.treatment_id                 AS treatment_id  "
    sql +=       "            , treatment_name                                AS name         "
    sql +=       "            , string_agg(treatmentdetail_no, ', ')          AS content              "
    sql +=       "            , ''                                            AS note     "
    sql +=       "            , '6'                                           AS status           "
    sql +=       "            , '2'                                           AS data_type            "
    sql +=       "        FROM    "
    sql +=       "            clinic_treatmentdetail  "
    sql +=       "        INNER JOIN  "
    sql +=       "                clinic_treatment    "
    sql +=       "            ON  "
    sql +=       "                    clinic_treatment.treatment_id = clinic_treatmentdetail.treatment_id "
    sql +=       "            AND     clinic_treatment.customer_id = '{}'  ".format(customer_id)
    sql +=       "        inner join  "
    sql +=       "                clinic_user "
    sql +=       "            ON  "
    sql +=       "                clinic_treatment.user_id  = clinic_user.user_id "
    sql +=       "        WHERE   "
    sql +=       "                  clinic_treatmentdetail.treatmentdetail_status = '{}' ".format(CONSTANT_KEY['TREATMENT_STATUS_DONE'])
    sql +=       "            AND   clinic_treatmentdetail.treatmentdetail_delete_flag = '{}' ".format(CONSTANT_KEY['DELETE_FLAG_FALSE'])
    sql +=       "        GROUP BY    "
    sql +=       "              clinic_treatment.treatment_id       "
    sql +=       "            , assign_name         "
    sql +=       "            , date        "
    sql +=       "            , time        "
    sql +=       "            , name    "
    sql +=       "    )   "
    sql +=       ")   "
    sql +=       "ORDER BY    "
    sql +=       "          data_type ASC  "
    sql +=       "        , status ASC    "
    sql +=       "        , date DESC "
    sql +=       "        , time ASC  "


    with connection.cursor() as cursor:
        cursor.execute(sql)
        lstAppointment = namedtuplefetchall(cursor)
    return lstAppointment

def sql_get_treatmentdetails(treatment_id,treatmentdetail_date):

    sql  = "       SELECT          "
    sql += "             customer_name              AS customer_name"
    sql += "           , treatment_name             AS name"
    sql += "           , treatmentdetail_assign_id  AS assign_id       "
    sql += "           , treatmentdetail_date       AS date   "
    sql += "           , treatmentdetail_time       AS time   "
    sql += "       FROM            "
    sql += "           clinic_treatmentdetail          "
    sql += "       INNER JOIN          "
    sql += "               clinic_treatment            "
    sql += "           ON          "
    sql += "                   clinic_treatment.brand_id       = clinic_treatmentdetail.brand_id           "
    sql += "               AND clinic_treatment.treatment_id   = clinic_treatmentdetail.treatment_id           "
    sql += "       INNER JOIN          "
    sql += "               clinic_customer         "
    sql += "           ON          "
    sql += "                   clinic_customer.brand_id    = clinic_treatment.brand_id         "
    sql += "               AND clinic_customer.customer_id = clinic_treatment.customer_id          "
    # sql += "       INNER JOIN          "
    # sql += "               clinic_user         "
    # sql += "           ON          "
    # sql += "                   clinic_user.brand_id    = clinic_treatmentdetail.brand_id         "
    # sql += "               AND clinic_user.user_id = clinic_treatmentdetail.treatmentdetail_assign_id          "
    sql += "       WHERE           "
    sql += "               clinic_treatmentdetail.treatment_id                 = '{}'            ".format(treatment_id)
    sql += "           AND clinic_treatmentdetail.treatmentdetail_date         = '{}'            ".format(treatmentdetail_date)
    sql += "           AND clinic_treatmentdetail.treatmentdetail_delete_flag  = '{}'            ".format(CONSTANT_KEY["DELETE_FLAG_FALSE"])
    sql += "       LIMIT 1            "

    # print(sql)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        treatmentdetail = namedtuplefetchall(cursor)
    return treatmentdetail

def sql_get_all_doctors_active():

    sql = "        SELECT             "
    sql += "              user_id              "
    sql += "            , user_name                "
    sql += "            , user_dob             "
    sql += "            , user_phone_number                "
    sql += "            , user_address             "
    sql += "            , user_specialize              "
    sql += "        FROM               "
    sql += "            clinic_user                "
    sql += "        WHERE              "
    sql += "                (clinic_user.user_role           = '{}'             ".format(CONSTANT_KEY['ROLE_DOCTOR'])
    sql += "            OR  clinic_user.user_role           = '{}')             ".format(CONSTANT_KEY['ROLE_DOCTOR_MASTER'])
    sql += "            AND clinic_user.user_delete_flag    = '{}'             ".format(CONSTANT_KEY['DELETE_FLAG_FALSE'])
    sql += "        ORDER BY        "
    sql += "            user_name        "
    with connection.cursor() as cursor:
        cursor.execute(sql)
        lst_user = namedtuplefetchall(cursor)
    return lst_user

def sql_get_all_treatmentdetails(treatment_id):

    sql  = "       SELECT      "
    sql += "             treatmentdetail_id        "
    sql += "           , treatmentdetail_no        "
    sql += "           , treatmentdetail_date      "
    sql += "           , treatmentdetail_content       "
    sql += "           , treatmentdetail_status        "
    sql += "       FROM        "
    sql += "           clinic_treatmentdetail      "
    sql += "       WHERE       "
    sql += "               clinic_treatmentdetail.treatment_id = '{}'      ".format(treatment_id)
    sql += "           AND clinic_treatmentdetail.treatmentdetail_delete_flag = '{}'       ".format(CONSTANT_KEY['DELETE_FLAG_FALSE'])
    sql += "       ORDER BY         "
    sql += "            treatmentdetail_no         "
    with connection.cursor() as cursor:
        cursor.execute(sql)
        lst_treatmentdetail = namedtuplefetchall(cursor)
    return lst_treatmentdetail

def sql_get_appointment(appointment_id):

    sql  = "       SELECT      "
    sql += "             customer_name              AS customer_name"
    sql += "           , treatment_name             AS name"
    sql += "           , appointment_assign_id      AS assign_id"
    sql += "           , appointment_date           AS date"
    sql += "           , appointment_time           AS time"
    sql += "       FROM        "
    sql += "           clinic_appointment      "
    sql += "       INNER JOIN      "
    sql += "               clinic_treatment        "
    sql += "           ON      "
    sql += "                   clinic_treatment.brand_id       = clinic_appointment.brand_id       "
    sql += "               AND clinic_treatment.treatment_id   = clinic_appointment.treatment_id       "
    sql += "       INNER JOIN      "
    sql += "               clinic_customer        "
    sql += "           ON      "
    sql += "                   clinic_customer.brand_id       = clinic_appointment.brand_id       "
    sql += "               AND clinic_customer.customer_id   = clinic_appointment.customer_id       "
    sql += "       WHERE       "
    sql += "           clinic_appointment.appointment_id = '{}'        ".format(appointment_id)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        appointment_info = namedtuplefetchall(cursor)
    return appointment_info


def sql_get_appointmentdetails(appointment_id):

    sql  = "       SELECT  "
    sql += "           treatmentdetail_id  "
    sql += "       FROM    "
    sql += "           clinic_appointmentdetail    "
    sql += "       WHERE   "
    sql += "           clinic_appointmentdetail.appointment_id = '{}'  ".format(appointment_id)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        appointmentdetails = namedtuplefetchall(cursor)
    return appointmentdetails