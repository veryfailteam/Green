"SELECT appointment_id, a.customer_id, customer_name, job, time_appointment, estimated_time, appointment_name, content, status FROM clinic_calendarappointment a, clinic_customer b WHERE date_appointment = '{0}' AND a.customer_id = b.customer_id ORDER BY status"
"""SELECT
          appointment_id
        , customer_id
        , customer_name
        , customer_phone_number
        , appointment_time
        , appointment_name
        , appointment_content
        , appointment_status
    FROM
          clinic_customer customer
        , clinic_appointment appoinment
    WHERE
            date_appointment = '{0}'
        AND customer.customer_id = appoinment.customer_id
        AND appointment_delete_flag = '0'
"""

"""
    SELECT
          appointment_id
        , user_name
        , appointment_date
        , appointment_time
        , treatment_name
        , appointment_content
        , appointment_note
    FROM
        clinic_appoinment
    INNER JOIN
            clinic_user
        ON
            clinic_user.user_id = clinic_appoinment.appointment_assign_id
    INNER JOIN
            clinic_treatment
        ON
            clinic_treatment.treatment_id = clinic_appointment.treatment_id
    WHERE
                clinic_appointment.customer_id = {}
        AND     appointment_delete_flag = "0"
    ORDER BY
        CAST    (appointment_date AS DATE) ASC
        AND     appointment_time ASC


"""




"""
SELECT
      customer_name
    , treatment_name
    , user_name
    , treatmentdetail_date
    , treatmentdetail_time
FROM
    clinic_treatmentdetail
INNER JOIN
        clinic_treatment
    ON
            clinic_treatment.brand_id       = clinic_treatmentdetail.brand_id
        AND clinic_treatment.treatment_id   = clinic_treatmentdetail.treatment_id
INNER JOIN
        clinic_customer
    ON
            clinic_customer.brand_id    = clinic_treatment.brand_id
        AND clinic_customer.customer_id = clinic_treatment.customer_id
WHERE
        clinic_treatmentdetail.treatment_id                 = {}
    AND clinic_treatmentdetail.treatmentdetail_date         = {}
    AND clinic_treatmentdetail.treatmentdetail_delete_flag  = {}
"""

"""
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
sql += "                clinic_user.user_role           = '{}'             "
sql += "            AND clinic_user.user_delete_flag    = '{}'             "
"""

"""
sql  = "       SELECT      "
sql += "             treatmentdetail_id        "
sql += "           , treatmentdetail_no        "
sql += "           , treatmentdetail_date      "
sql += "           , treatmentdetail_content       "
sql += "           , treatmentdetail_status        "
sql += "       FROM        "
sql += "           clinic_treatmentdetail      "
sql += "       WHERE       "
sql += "               clinic_treatmentdetail.treatment_id = '{}'      "
sql += "           AND clinic_treatmentdetail.treatmentdetail_delete_flag = '{}'       "
"""

"""
sql  = "       SELECT      "
sql += "           appointment_id      "
sql += "           , treatment_name        "
sql += "           , appointment_assign_id     "
sql += "           , appointment_date      "
sql += "           , appointment_time      "
sql += "       FROM        "
sql += "           clinic_appointment      "
sql += "       INNER JOIN      "
sql += "               clinic_treatment        "
sql += "           ON      "
sql += "                   clinic_treatment.brand_id       = clinic_appointment.brand_id       "
sql += "               AND clinic_treatment.treatment_id   = clinic_appointment.treatment_id       "
sql += "       WHERE       "
sql += "           clinic_appointment.appointment_id = '{}'        "
"""

# sql  = "       SELECT  "
# sql += "           treatmentdetail_id  "
# sql += "       FROM    "
# sql += "           clinic_appointmentdetail    "
# sql += "       WHERE   "
# sql += "           clinic_appointmentdetail.appointment_id = '{}'  "



# sql  = "            UPDATE          "
# sql += "                clinic_appointment          "
# sql += "            SET             "
# sql += "                appointment_date = {}         "
# sql += "                appointment_time = {}         "
# sql += "                appointment_content = {}          "
# sql += "                appointment_assign_id = {}            "
# sql += "                appointment_estimated_time = {}           "
# sql += "                appointment_estimated_difficulty = {}         "
# sql += "                appointment_status = {}           "
# sql += "                appointment_note = {}         "
# sql += "                appointment_update_date = {}          "
# sql += "                appointment_update_by = {}            "
# sql += "                appointment_delete_flag = {}          "
# sql += "            WHERE           "
# sql += "                appointment_id = {}           "



# sql += "        SELECT      "
# sql += "              customer_id       "
# sql += "            , customer_name     "
# sql += "            , customer_phone_number     "
# sql += "        FROM        "
# sql += "            clinic_customer     "





def func(foo, bar = None):
    print(foo, bar)




func(foo=42)