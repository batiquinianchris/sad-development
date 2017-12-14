from django.contrib import admin

from .models import *

#admin controlled
admin.site.register(School_Year)

admin.site.register(Scholarship)

admin.site.register(Promissory)

admin.site.register(Drop)

admin.site.register(SHS_Category)

admin.site.register(Subjects)

admin.site.register(Employee)

#Registrar/Academic head controlled
admin.site.register(Student)

admin.site.register(SHS_Subject)

admin.site.register(Offering)

admin.site.register(Enrollment_Details)

admin.site.register(Section)

admin.site.register(Teacher_Details)

#Cashier controlled

admin.site.register(Payment_Log)

admin.site.register(Fees_Accounts)

admin.site.register(Payment_LogDetails)
