# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('brand_id', models.IntegerField(null=True)),
                ('user_id', models.IntegerField(null=True)),
                ('customer_id', models.IntegerField(null=True)),
                ('treatment_id', models.IntegerField(null=True)),
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.CharField(max_length=10, null=True)),
                ('appointment_time', models.CharField(max_length=5, null=True)),
                ('appointment_content', models.CharField(max_length=500, null=True)),
                ('appointment_assign_id', models.IntegerField(null=True)),
                ('appointment_estimated_time', models.CharField(max_length=8, null=True)),
                ('appointment_estimated_difficulty', models.CharField(max_length=2, null=True)),
                ('appointment_status', models.CharField(max_length=10, null=True)),
                ('appointment_note', models.TextField(null=True)),
                ('appointment_create_date', models.CharField(max_length=10, null=True)),
                ('appointment_create_by', models.CharField(max_length=8, null=True)),
                ('appointment_update_date', models.CharField(max_length=10, null=True)),
                ('appointment_update_by', models.CharField(max_length=8, null=True)),
                ('appointment_delete_flag', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=32, null=True)),
                ('brand_address', models.CharField(max_length=300, null=True)),
                ('brand_phone_number', models.CharField(max_length=11, null=True)),
                ('brand_manager_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('brand_id', models.IntegerField(null=True)),
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=32, null=True)),
                ('customer_sex', models.CharField(max_length=32, null=True)),
                ('customer_dob', models.CharField(max_length=10, null=True)),
                ('customer_job', models.CharField(max_length=500, null=True)),
                ('customer_company', models.CharField(max_length=500, null=True)),
                ('customer_phone_number', models.CharField(max_length=11, null=True)),
                ('customer_email', models.CharField(max_length=200, null=True)),
                ('customer_address', models.TextField(null=True)),
                ('customer_source', models.CharField(max_length=500, null=True)),
                ('customer_fingerprint', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('brand_id', models.IntegerField(null=True)),
                ('user_id', models.IntegerField(null=True)),
                ('customer_id', models.IntegerField(null=True)),
                ('treatment_id', models.AutoField(primary_key=True, serialize=False)),
                ('treatment_name', models.CharField(max_length=200, null=True)),
                ('treatment_content', models.CharField(max_length=500, null=True)),
                ('treatment_total_payment', models.IntegerField(default=0, null=True)),
                ('treatment_payment_status', models.IntegerField(default=0, null=True)),
                ('treatment_status', models.CharField(max_length=10, null=True)),
                ('treatment_create_date', models.CharField(max_length=10, null=True)),
                ('treatment_create_by', models.CharField(max_length=8, null=True)),
                ('treatment_update_date', models.CharField(max_length=10, null=True)),
                ('treatment_update_by', models.CharField(max_length=8, null=True)),
                ('treatment_delete_flag', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentDetail',
            fields=[
                ('brand_id', models.IntegerField(null=True)),
                ('treatment_id', models.IntegerField(null=True)),
                ('treatmentdetail_id', models.AutoField(primary_key=True, serialize=False)),
                ('treatmentdetail_no', models.CharField(max_length=10, null=True)),
                ('treatmentdetail_date', models.CharField(max_length=10, null=True)),
                ('treatmentdetail_content', models.CharField(max_length=500, null=True)),
                ('treatmentdetail_price', models.IntegerField(null=True)),
                ('treatmentdetail_status', models.CharField(max_length=10, null=True)),
                ('treatmentdetail_create_date', models.CharField(max_length=10, null=True)),
                ('treatmentdetail_create_by', models.CharField(max_length=8, null=True)),
                ('treatmentdetail_update_date', models.CharField(max_length=10, null=True)),
                ('treatmentdetail_update_by', models.CharField(max_length=8, null=True)),
                ('treatmentdetail_delete_flag', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('brand_id', models.IntegerField(null=True)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_login_id', models.CharField(max_length=8, null=True)),
                ('user_password', models.CharField(max_length=32, null=True)),
                ('user_role', models.CharField(max_length=100, null=True)),
                ('user_name', models.CharField(max_length=300, null=True)),
                ('user_dob', models.CharField(max_length=10, null=True)),
                ('user_phone_number', models.CharField(max_length=11, null=True)),
                ('user_address', models.TextField(null=True)),
                ('user_specialize', models.CharField(max_length=200, null=True)),
                ('user_delete_flag', models.CharField(max_length=1, null=True)),
            ],
        ),
    ]