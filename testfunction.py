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
    """.format(current_date)

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





SELECT
    customer_name
    treatment_name
    user_name
    appointment_date
    appointment_time
    treatmentdetail_id
    treatmentdetail_no
    treatmentdetail_date
    treatmentdetail_content
    treatmentdetail_status
FROM
    clinic_appointment
INNER JOIN




appointment_assign_id





print(dm)