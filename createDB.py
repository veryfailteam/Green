import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ERP.settings");
django.setup()

from clinic.models import Appointment
from clinic.models import Customer
from clinic.models import User
from clinic.models import Treatment
from clinic.models import TreatmentDetail

User.objects.create(brand_id ='1',user_id = '1',user_login_id = 'D001',user_password = '1234',user_role = '1',user_name = 'Trần Trung Hiến',user_dob = '03/09/1991',user_phone_number = '0906858628',user_address = '1079',user_specialize = 'Không có')
User.objects.create(brand_id ='1',user_id = '2',user_login_id = 'R001',user_password = '1234',user_role = '2',user_name = 'Trần Trung ',user_dob = '03/09/1991',user_phone_number = '0906858628',user_address = '1079',user_specialize = 'Không có')
User.objects.create(brand_id ='1',user_id = '3',user_login_id = 'M001',user_password = '1234',user_role = '0',user_name = 'Trần',user_dob = '03/09/1991',user_phone_number = '0906858628',user_address = '1079',user_specialize = 'Không có')


Customer.objects.create(brand_id = "1", customer_id = "1", customer_name = "Phạm Tú", customer_sex = "Nam", customer_dob = "01-01-1991", customer_job = "Nhân viên văn phòng", customer_company = "Cty CP FunnyDay", customer_phone_number = "0906858628", customer_email = "jostrunghien@gmail.com", customer_address = "1079CMT8", customer_source = "", customer_fingerprint = "")
Customer.objects.create(brand_id = "1", customer_id = "2", customer_name = "Phạm Tình", customer_sex = "Nam", customer_dob = "02-01-1991", customer_job = "Nhân viên văn phòng", customer_company = "Cty CP FunnyDay", customer_phone_number = "0906858628", customer_email = "jostrunghien@gmail.com", customer_address = "1079CMT8", customer_source = "", customer_fingerprint = "")
Customer.objects.create(brand_id = "1", customer_id = "3", customer_name = "Phạm Tu", customer_sex = "Nam", customer_dob = "03-01-1991", customer_job = "Nhân viên văn phòng", customer_company = "Cty CP FunnyDay", customer_phone_number = "0906858628", customer_email = "jostrunghien@gmail.com", customer_address = "1079CMT8", customer_source = "", customer_fingerprint = "")


Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "1",appointment_id = "1",appointment_date = "11-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "0",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")

Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "3",appointment_id = "3",appointment_date = "11-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "2",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")

Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "5",appointment_id = "5",appointment_date = "04-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "4",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")


Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "1",appointment_id = "8",appointment_date = "04-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "6",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "1",appointment_id = "9",appointment_date = "04-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "6",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "1",appointment_id = "10",appointment_date = "04-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "6",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "1",appointment_id = "11",appointment_date = "04-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "5",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "1",appointment_id = "12",appointment_date = "04-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "1",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "1",appointment_id = "13",appointment_date = "04-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "2",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "1",appointment_id = "14",appointment_date = "04-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "3",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "1")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "1",treatment_id = "1",appointment_id = "15",appointment_date = "20-11-2017",appointment_time = "09:00",appointment_content = "Là làm cái gì",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "0",appointment_status = "4",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "1")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "2",treatment_id = "4",appointment_id = "4",appointment_date = "11-11-2017",appointment_time = "10:00",appointment_content = "uh",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "1",appointment_status = "3",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "2",treatment_id = "6",appointment_id = "6",appointment_date = "04-11-2017",appointment_time = "10:00",appointment_content = "uh",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "1",appointment_status = "5",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "2",treatment_id = "7",appointment_id = "7",appointment_date = "04-11-2017",appointment_time = "10:00",appointment_content = "uh",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "1",appointment_status = "6",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")
Appointment.objects.create(brand_id = "1",user_id = "1",customer_id = "2",treatment_id = "2",appointment_id = "2",appointment_date = "11-11-2017",appointment_time = "10:00",appointment_content = "uh",appointment_assign_id = "1",appointment_estimated_time = "60",appointment_estimated_difficulty = "1",appointment_status = "1",appointment_note = "nothing",appointment_create_date = "02-11-2017",appointment_create_by = "1",appointment_update_date = "02-11-2017",appointment_update_by = "1",appointment_delete_flag = "0")




Treatment.objects.create(brand_id = "1", user_id = "1", customer_id = "1", treatment_id = "1", treatment_name = "treatment_name", treatment_content = "treatment_content", treatment_total_payment = 0, treatment_payment_status = 0, treatment_status = "0", treatment_create_date = "0", treatment_create_by = "0", treatment_update_date = "0", treatment_update_by = "1", treatment_delete_flag = "0")


TreatmentDetail.objects.create(brand_id = "" ,treatment_id = "" ,treatmentdetail_id = "" ,treatmentdetail_no = "" ,treatmentdetail_date = "" ,treatmentdetail_time = "" ,treatmentdetail_assign_id = "" ,treatmentdetail_content = "" ,treatmentdetail_price  = "" ,treatmentdetail_status = "" ,treatmentdetail_create_date = "" ,treatmentdetail_create_by = "" ,treatmentdetail_update_date = "" ,treatmentdetail_update_by = "" ,treatmentdetail_delete_flag = "")








# old

# CalendarAppointment.objects.create(brand_id = '001' ,user_id = 'R001' ,customer_id = 'CUS001', appointment_id = 'A001', treatment_id = 'T001', date_appointment = '06-09-2017',time_appointment = '09:00',appointment_name = 'face-care', content = 'face-care', assign_id = 'D001', estimated_time = '30',estimated_difficulty = '1',status = '0',note ='none', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')
# CalendarAppointment.objects.create(brand_id = '001' ,user_id = 'R001' ,customer_id = 'CUS002', appointment_id = 'A002', treatment_id = 'T002', date_appointment = '06-09-2017',time_appointment = '10:00',appointment_name = 'Nhổ răng 31 & cạo vôi', content = 'Cắt chỉ, nhổ răng 18, nhớ chụp film CB', assign_id = 'D001', estimated_time = '30',estimated_difficulty = '1',status = '1',note ='none', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')
# CalendarAppointment.objects.create(brand_id = '001' ,user_id = 'R001' ,customer_id = 'CUS003', appointment_id = 'A003', treatment_id = 'T003', date_appointment = '06-09-2017',time_appointment = '09:00',appointment_name = 'Implant,  dvcb', content = 'Nội dung của Implant,  dvcb', assign_id = 'D001', estimated_time = '30',estimated_difficulty = '1',status = '2',note ='none', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')
# CalendarAppointment.objects.create(brand_id = '001' ,user_id = 'R001' ,customer_id = 'CUS004', appointment_id = 'A004', treatment_id = 'T004', date_appointment = '06-09-2017',time_appointment = '11:00',appointment_name = 'Tư vấn nâng mũi', content = 'Nội dung của tư vấn nâng mũi', assign_id = 'D001', estimated_time = '30',estimated_difficulty = '1',status = '3',note ='none', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')
# CalendarAppointment.objects.create(brand_id = '001' ,user_id = 'R001' ,customer_id = 'CUS005', appointment_id = 'A005', treatment_id = 'T005', date_appointment = '06-09-2017',time_appointment = '09:00',appointment_name = 'Implant,  dvcb', content = 'Nội dung của Implant,  dvcb', assign_id = 'D001', estimated_time = '30',estimated_difficulty = '1',status = '4',note ='none', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')
# CalendarAppointment.objects.create(brand_id = '001' ,user_id = 'R001' ,customer_id = 'CUS006', appointment_id = 'A006', treatment_id = 'T006', date_appointment = '06-09-2017',time_appointment = '14:00',appointment_name = 'Tư vấn nâng mũi', content = 'Nội dung của tư vấn nâng mũi', assign_id = 'D001', estimated_time = '30',estimated_difficulty = '1',status = '5',note ='none', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')
# CalendarAppointment.objects.create(brand_id = '001' ,user_id = 'R001' ,customer_id = 'CUS004', appointment_id = 'A007', treatment_id = 'T001', date_appointment = '28-09-2017',time_appointment = '11:00',appointment_name = 'Tư vấn nâng mũi', content = 'Nội dung của tư vấn nâng mũi', assign_id = 'D001', estimated_time = '30',estimated_difficulty = '1',status = '4',note ='none', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')
# CalendarAppointment.objects.create(brand_id = '001' ,user_id = 'R001' ,customer_id = 'CUS005', appointment_id = 'A008', treatment_id = 'T001', date_appointment = '01-11-2017',time_appointment = '09:00',appointment_name = 'Implant,  dvcb', content = 'Nội dung của Implant,  dvcb', assign_id = 'D001', estimated_time = '30',estimated_difficulty = '1',status = '4',note ='none', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')
# CalendarAppointment.objects.create(brand_id = '001' ,user_id = 'R001' ,customer_id = 'CUS006', appointment_id = 'A009', treatment_id = 'T001', date_appointment = '15-12-2017',time_appointment = '14:00',appointment_name = 'Tư vấn nâng mũi', content = 'Nội dung của tư vấn nâng mũi', assign_id = 'D001', estimated_time = '30',estimated_difficulty = '1',status = '4',note ='none', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')



# Customer.objects.create(brand_id = '001',customer_id = 'CUS001' ,customer_name = 'Phạm Tú',dob = '1991-01-01', sex = 'Nam', job = "Nhân viên văn phòng" , company = "Cty cp FunnyDay", phone_number = '0906858628', email = 'hoangducthinh2012@gmail.com' ,address = 'none',source = 'none',fingerprint = 'none',medical_biography = 'none')
# Customer.objects.create(brand_id = '001',customer_id = 'CUS002' ,customer_name = 'Pham Tuấn',dob = '1991-01-01', sex = 'Nữ', job = "Nhân viên văn phòng" , company = "Cty cp FunnyDay", phone_number = '0906858628', email = 'hoangducthinh2013@gmail.com' ,address = 'none',source = 'none',fingerprint = 'none',medical_biography = 'none')
# Customer.objects.create(brand_id = '001',customer_id = 'CUS003' ,customer_name = 'Pham Tân',dob = '1991-01-01', sex = 'Nam', job = "Nhân viên văn phòng" , company = "Cty cp FunnyDay", phone_number = '0906858628', email = 'hoangducthinh2014@gmail.com' ,address = 'none',source = 'none',fingerprint = 'none',medical_biography = 'none')
# Customer.objects.create(brand_id = '001',customer_id = 'CUS004' ,customer_name = 'Pham Tiên',dob = '1991-01-01', sex = 'Nữ', job = "Nhân viên văn phòng" , company = "Cty cp FunnyDay", phone_number = '0906858628', email = 'hoangducthinh2015@gmail.com' ,address = 'none',source = 'none',fingerprint = 'none',medical_biography = 'none')
# Customer.objects.create(brand_id = '001',customer_id = 'CUS005' ,customer_name = 'Pham Tùng',dob = '1991-01-01', sex = 'Nữ', job = "Nhân viên văn phòng" , company = "Cty cp FunnyDay", phone_number = '0906858628', email = 'hoangducthinh2016@gmail.com' ,address = 'none',source = 'none',fingerprint = 'none',medical_biography = 'none')
# Customer.objects.create(brand_id = '001',customer_id = 'CUS006' ,customer_name = 'Pham Tủn',dob = '1991-01-01', sex = 'Nam', job = "Nhân viên văn phòng" , company = "Cty cp FunnyDay", phone_number = '0906858628', email = 'hoangducthinh2017@gmail.com' ,address = 'none',source = 'none',fingerprint = 'none',medical_biography = 'none')

# Treatment.objects.create(brand_id = 'CN01',user_id = 'R001',customer_id = 'CUS006',treatment_id = 'T001',describe = 'nothing',total_payment = 0,payment_status = 0,treatment_status = 'proccess', create_date = '07-06-2017', create_by = 'D001', update_date = '07-06-2017', update_by = 'D001', delete_flag = '0')