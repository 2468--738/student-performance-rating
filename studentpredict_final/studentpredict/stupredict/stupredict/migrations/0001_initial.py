# Generated by Django 3.0.7 on 2022-02-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(db_column='id', editable=False, primary_key=True, serialize=False)),
                ('subject_code', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('lecture_no', models.IntegerField()),
                ('roll_no', models.BigIntegerField()),
                ('remarks', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'attendance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(db_column='id', editable=False, primary_key=True, serialize=False)),
                ('branch_code', models.IntegerField()),
                ('branch_name', models.CharField(max_length=25)),
                ('roll_no', models.BigIntegerField()),
                ('session', models.CharField(max_length=9)),
            ],
            options={
                'db_table': 'branch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HasOffers',
            fields=[
                ('roll_no', models.BigIntegerField()),
                ('offer_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'has_offers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JobOffers',
            fields=[
                ('id', models.AutoField(db_column='ID', editable=False, primary_key=True, serialize=False)),
                ('offer', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
                ('package', models.BigIntegerField()),
            ],
            options={
                'db_table': 'job_offers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mock',
            fields=[
                ('id', models.AutoField(db_column='id', editable=False, primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=9)),
                ('subject_code', models.CharField(max_length=10)),
                ('subject_name', models.CharField(max_length=50)),
                ('roll_no', models.BigIntegerField()),
                ('obtained_marks', models.IntegerField()),
                ('max_marks', models.IntegerField()),
            ],
            options={
                'db_table': 'mock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(db_column='id', editable=False, primary_key=True, serialize=False)),
                ('roll_no', models.BigIntegerField()),
                ('grade', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'performance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(db_column='id', editable=False, primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=9)),
                ('student_rollno', models.BigIntegerField()),
            ],
            options={
                'db_table': 'session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=9)),
                ('roll_no', models.BigIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=10)),
                ('sem', models.IntegerField()),
                ('doa', models.DateField()),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gap', models.IntegerField()),
                ('phone_no', models.BigIntegerField()),
                ('e_mail', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('graded', models.IntegerField()),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=50)),
                ('branch_code', models.IntegerField()),
                ('sem', models.IntegerField()),
                ('type', models.CharField(max_length=6)),
                ('max_marks', models.IntegerField()),
                ('min_marks', models.IntegerField()),
                ('credit', models.FloatField()),
            ],
            options={
                'db_table': 'subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(db_column='id', editable=False, primary_key=True, serialize=False)),
                ('session', models.CharField(max_length=9)),
                ('subject_code', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=9)),
                ('subject_name', models.CharField(max_length=50)),
                ('obtained_marks', models.IntegerField()),
                ('max_marks', models.IntegerField()),
                ('roll_no', models.BigIntegerField()),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
    ]
