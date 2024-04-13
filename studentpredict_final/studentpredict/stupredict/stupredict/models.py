from django.db import models

class Session(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, editable=False)
    session = models.CharField(max_length=9)
    student_rollno = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'session'

    def __str__(self):
        return self.session


class Student(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    session = models.CharField(max_length=9)
    roll_no = models.BigIntegerField()
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    sem = models.IntegerField()
    doa = models.DateField()
    dob = models.DateField()
    age = models.IntegerField()
    gap = models.IntegerField()
    phone_no = models.BigIntegerField()
    e_mail = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    graded = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student'

    def __str__(self):
        return self.roll_no

class Performance(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, editable=False)
    roll_no = models.BigIntegerField()
    grade = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'performance'

    def __str__(self):
        return self.roll_no + self.grade

class Branch(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, editable=False)
    branch_code = models.IntegerField()
    branch_name = models.CharField(max_length=25)
    roll_no = models.BigIntegerField()
    session = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'branch'

    def __str__(self):
        return self.branch_code

class Subject(models.Model):
    subject_code = models.CharField(primary_key=True, max_length=10)
    session = models.CharField(max_length=9)
    name = models.CharField(max_length=50)
    branch_code = models.IntegerField()
    sem = models.IntegerField()
    type = models.CharField(max_length=6)
    max_marks = models.IntegerField()
    min_marks = models.IntegerField()
    credit = models.FloatField()

    class Meta:
        managed = False
        db_table = 'subject'

    def __str__(self):
        return self.subject_code

class Attendance(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, editable=False)
    subject_code = models.CharField(max_length=10)
    date = models.DateField()
    lecture_no = models.IntegerField()
    roll_no = models.BigIntegerField()
    remarks = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'attendance'

    def __str__(self):
        return self.id

class Test(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, editable=False)
    session = models.CharField(max_length=9)
    subject_code = models.CharField(max_length=10)
    type = models.CharField(max_length=9)
    subject_name = models.CharField(max_length=50)
    obtained_marks = models.IntegerField()
    max_marks = models.IntegerField()
    roll_no = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'test'

    def __str__(self):
        return self.obtained_marks

class Mock(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, editable=False)
    session = models.CharField(max_length=9)
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=50)
    roll_no = models.BigIntegerField()
    obtained_marks = models.IntegerField()
    max_marks = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mock'

    def __str__(self):
        return self.obtained_marks



class HasOffers(models.Model):
    roll_no = models.BigIntegerField()
    offer_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'has_offers'

    def __str__(self):
        return self.offer_id


class JobOffers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, editable=False)
    offer_id = models.IntegerField()
    company = models.CharField(max_length=50)
    package = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'job_offers'

    def __str__(self):
        return self.offer
