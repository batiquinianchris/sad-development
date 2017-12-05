from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Drop(models.Model):
    	drop_ID = models.AutoField(primary_key=True)
    	student_name = models.CharField(max_length=200)
    	drop_date = models.DateTimeField(null=True, blank=True)
    	schoolYr_ID = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
    	reason = models.CharField(max_length=500)
	status = models.CharField(max_length=2)
	approved_date = models.DateTimeField(null=True, blank=True)
	
class SHS_Category(models.Model):
    	category_ID = models.AutoField(primary_key=True)
    	category_name = models.CharField(max_length=200)
    	type = models.IntegerField()
    	status = models.CharField(max_length=50)
    	
class Subjects(models.Model):
    	subject_ID = models.AutoField(primary_key=True)
    	subject_name = models.CharField(max_length=200)
    	status = models.CharField(max_length=50)

class Employee(models.Model):
    	employee_ID = models.AutoField(primary_key=True)
    	first_name = models.CharField(max_length=200)
    	last_name = models.CharField(max_length=200)
    	type = models.IntegerField()
    	status = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

class Promissory(models.Model):
	promissory_ID = models.AutoField(primary_key=True)
    	promisorry_name = models.CharField(max_length=200)
    	reason = models.CharField(max_length=500)
    	date_filed =models.DateTimeField(null=True, blank=True)
    	date_approved = models.DateTimeField(null=True, blank=True)
    	deadline = models.DateTimeField(null=True, blank=True)
	studnet_ID = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)
	schoolYr_ID = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
	status = models.CharField(max_length=50)

class Student(models.Model):
    	student_ID = models.AutoField(primary_key=True)
    	first_name = models.CharField(max_length=200)
    	last_name = models.CharField(max_length=200)
    	status = models.CharField(max_length=50)
    	
class Scholarship(models.Model):
    	scholarship_ID = models.AutoField(primary_key=True)
    	scholarship_name = models.CharField(max_length=200)
    	amount = models.IntegerField()
    	schoolYr_ID = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
    	validity =  models.IntegerField()
	status = models.CharField(max_length=50)
	type = models.IntegerField()
	
class SHS_Subject(models.Model):
    	shs_subjectID = models.AutoField(primary_key=True)
    	shs_subjectName = models.CharField(max_length=200)
    	description = models.CharField(max_length=200)
    	track_status = models.CharField(max_length=50)
    	category_ID = models.ForeignKey(SHS_Category, on_delete=models.CASCADE, default=0)

class Payment_Log(models.Model):
    	payment_ID = models.AutoField(primary_key=True)
    	enrollment_ID = models.ForeignKey(Enrollment, on_delete=models.CASCADE, default=0)
    	payment_date = models.DateTimeField(null=True, blank=True)
    	total_amount = models.IntegerField()
    	type = models.IntegerField()
	note = models.CharField(max_length=500)
	
class Section(models.Model):
    	section_ID = models.AutoField(primary_key=True)
    	section_name = models.CharField(max_length=200)
    	status = models.CharField(max_length=50)
    	
class Fees_Accounts(models.Model):
    	FA_ID = models.AutoField(primary_key=True)
    	FA_name = models.CharField(max_length=200)
    	amount = models.IntegerField()
    	
class Enrollent_Details(models.Model):
    	enrollmentDetails_ID = models.AutoField(primary_key=True)
    	enrollment_ID = models.ForeignKey(Enrollment, on_delete=models.CASCADE, default=0)
    	offering_ID = models.ForeignKey(Offering, on_delete=models.CASCADE, default=0)
    	
class Offering(models.Model):
    	offering_ID = models.AutoField(primary_key=True)
    	subject_ID = models.ForeignKey(Subject, on_delete=models.CASCADE, default=0)
    	employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE, default=0)
    	schoolYr_ID = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)

class Enrollment(models.Model):
    	enrollment_ID = models.AutoField(primary_key=True)
    	schoolYr_ID = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
    	student_ID = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)
    	scholarship_ID = models.ForeignKey(Scholarship on_delete=models.CASCADE, default=0)
    	student_type = models.IntegerField()
	
class Payment_LogDetails(models.Model):
    	payment_detailsID = models.AutoField(primary_key=True)
    	payment_ID = models.ForeignKey(Payment_Log, on_delete=models.CASCADE, default=0)
    	FA_ID = models.ForeignKey(Fees_Accounts, on_delete=models.CASCADE, default=0)
    	
class Teacher_Details(models.Model):
    	employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE, default=0)
    	subject_ID = models.ForeignKey(Subject, on_delete=models.CASCADE, default=0)
    	units = models.IntegerField()
    	schoolYr_ID = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
    	status = models.CharField(max_length=50)
	section_ID = models.ForeignKey(Section, on_delete=models.CASCADE, default=0)
	
class School_Year(models.Model):
    	schoolYr_ID = models.AutoField(primary_key=True)
    	schoolYr_name = models.CharField(max_length=200)
    	status = models.CharField(max_length=50)
    	
class User(models.Model):
	user_ID = models.AutoField(primary_key=True)
    	username = models.CharField(max_length=50)
    	password = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	type = units = models.IntegerField()