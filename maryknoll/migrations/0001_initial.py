# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-09 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drop',
            fields=[
                ('drop_ID', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=200)),
                ('drop_date', models.DateTimeField(blank=True, null=True)),
                ('reason', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=2)),
                ('approved_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('type', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enrollment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('student_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enrollmentt_Details',
            fields=[
                ('enrollmentDetails_ID', models.AutoField(primary_key=True, serialize=False)),
                ('enrollment_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Enrollment')),
            ],
        ),
        migrations.CreateModel(
            name='Fees_Accounts',
            fields=[
                ('FA_ID', models.AutoField(primary_key=True, serialize=False)),
                ('FA_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('offering_ID', models.AutoField(primary_key=True, serialize=False)),
                ('employee_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Log',
            fields=[
                ('payment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('total_amount', models.IntegerField()),
                ('type', models.IntegerField()),
                ('note', models.CharField(max_length=500)),
                ('enrollment_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Enrollment')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_LogDetails',
            fields=[
                ('payment_detailsID', models.AutoField(primary_key=True, serialize=False)),
                ('FA_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Fees_Accounts')),
                ('payment_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Payment_Log')),
            ],
        ),
        migrations.CreateModel(
            name='Promissory',
            fields=[
                ('promissory_ID', models.AutoField(primary_key=True, serialize=False)),
                ('promisorry_name', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=500)),
                ('date_filed', models.DateTimeField(blank=True, null=True)),
                ('date_approved', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('scholarship_ID', models.AutoField(primary_key=True, serialize=False)),
                ('scholarship_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('validity', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School_Year',
            fields=[
                ('schoolYr_ID', models.AutoField(primary_key=True, serialize=False)),
                ('schoolYr_name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_ID', models.AutoField(primary_key=True, serialize=False)),
                ('section_name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SHS_Category',
            fields=[
                ('category_ID', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=200)),
                ('type', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SHS_Subject',
            fields=[
                ('shs_subjectID', models.AutoField(primary_key=True, serialize=False)),
                ('shs_subjectName', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('track_status', models.CharField(max_length=50)),
                ('category_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.SHS_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('subject_ID', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('employee_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Employee')),
                ('schoolYr_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.School_Year')),
                ('section_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Section')),
                ('subject_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Subjects')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('units', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='scholarship',
            name='schoolYr_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.School_Year'),
        ),
        migrations.AddField(
            model_name='promissory',
            name='schoolYr_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.School_Year'),
        ),
        migrations.AddField(
            model_name='promissory',
            name='student_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Student'),
        ),
        migrations.AddField(
            model_name='offering',
            name='schoolYr_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.School_Year'),
        ),
        migrations.AddField(
            model_name='offering',
            name='subject_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Subjects'),
        ),
        migrations.AddField(
            model_name='enrollmentt_details',
            name='offering_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Offering'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='scholarship_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Scholarship'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='schoolYr_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.School_Year'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.Student'),
        ),
        migrations.AddField(
            model_name='drop',
            name='schoolYr_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maryknoll.School_Year'),
        ),
    ]
