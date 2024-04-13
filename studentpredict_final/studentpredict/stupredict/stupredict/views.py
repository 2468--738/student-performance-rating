from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from numpy import roll
from .models import *
from sklearn.ensemble import RandomForestClassifier
import pandas

def index(request):
    error = None
    if request.method == 'POST':

        #Receive entered username and password
        u = request.POST["username"]
        p = request.POST["pwd"]

        #Authenticate and login user
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "No"
            else:
                error = "Yes"
        except:
            error = "Yes"

    d = {'error' : error}
    return render(request, 'index.html', d)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    if not request.user.is_staff:
        return redirect('')
    return render(request, 'home.html')

def insert(request):
    if not request.user.is_staff:
        return redirect('')
    return render(request, 'insert_data.html')

def update(request):
    if not request.user.is_staff:
        return redirect('')
    return render(request, 'modify_data.html')

def delete(request):
    if not request.user.is_staff:
        return redirect('')
    return render(request, 'delete.html')

def predict_students(request):
    if not request.user.is_staff:
        return redirect('')
    lst3 = []
    if not request.session['lst2']:
        return render(request, 'prediction_results.html', {'lst3': lst3})
    data = {'roll_no':[], 'absences':[], 'age':[], 'gap':[], 'gender':[], 'marks':[], 'performance':[]}
    students = Student.objects.all()
    
    for student in students:
        p = Performance.objects.filter(roll_no=student.roll_no)
        if p:
            data['roll_no'].append(student.roll_no)
            data['age'].append(student.age)
            data['gap'].append(student.gap)
            data['gender'].append(student.gender)
    for roll in data['roll_no']:
        absences = 0
        total_days = 0
        att = Attendance.objects.filter(roll_no=roll)
        for z in att:
            total_days += 1
            if z.remarks == 'a':
                absences += 1
        test = Test.objects.filter(roll_no=roll)
        total_obtained_marks = 0
        total_max_marks = 0
        for z in test:
            total_obtained_marks += z.obtained_marks
            total_max_marks += z.max_marks
        p = Performance.objects.filter(roll_no=roll)
        if p:
            data['marks'].append(total_obtained_marks * 100 / total_max_marks)
            data['absences'].append(absences * 100 / total_days)
            data['performance'].append(p[0].grade)
    dataframe = pandas.DataFrame(data)
    gender = dataframe['gender']
    for i in range(len(gender)):
        if gender[i] == 'M':
            gender[i] = 1
        elif gender[i] == 'F':
            gender[i] = 0
    dataframe['gender'] = gender
    x = dataframe.drop(columns=['performance', 'roll_no'])
    y = dataframe['performance']
    lst = request.session['lst2']
    data_to_be_predicted = {'roll_no':[], 'absences':[], 'age':[], 'gap':[], 'gender':[], 'marks':[]}
    for ele in lst:
        student = Student.objects.filter(roll_no=ele[0])[0]
        data_to_be_predicted['roll_no'].append(student.roll_no)
        data_to_be_predicted['age'].append(student.age)
        data_to_be_predicted['gap'].append(student.gap)
        data_to_be_predicted['gender'].append(student.gender)
        absences = 0
        total_days = 0
        att = Attendance.objects.filter(roll_no=student.roll_no)
        for z in att:
            total_days += 1
            if z.remarks == 'a':
                absences += 1
        test = Test.objects.filter(roll_no=student.roll_no)
        total_obtained_marks = 0
        total_max_marks = 0
        for z in test:
            total_obtained_marks += z.obtained_marks
            total_max_marks += z.max_marks
        data_to_be_predicted['marks'].append(total_obtained_marks * 100 / total_max_marks)
        data_to_be_predicted['absences'].append(absences * 100 / total_days)
    rf = RandomForestClassifier()
    rf.fit(x, y)
    stu_to_be_predicted = pandas.DataFrame(data_to_be_predicted)
    gender = stu_to_be_predicted['gender']
    for i in range(len(gender)):
        if gender[i] == 'M':
            gender[i] = 1
        elif gender[i] == 'F':
            gender[i] = 0
    stu_to_be_predicted['gender'] = gender
    a = stu_to_be_predicted.drop(columns=['roll_no'])
    results = rf.predict(a)



    lst = request.session['lst2']
    
    i = 0
    for ele in lst:
        b = Branch.objects.filter(roll_no=ele[0])[0]
        lst3.append(list(ele) + [b.branch_name, results[i]])
        i += 1
        
    return render(request, 'prediction_results.html', {'lst3': lst3})

def predict_given(request):
    if not request.user.is_staff:
        return redirect('')
    students = Student.objects.all()
    lst = []
    for student in students:
        branch = Branch.objects.filter(roll_no=student.roll_no)[0]
        lst.append([student.roll_no, student.name, branch.branch_name])
    request.session["lst2"] = []
    return render(request, 'select_students.html', {"lst": lst, "lst2": []})

def add_student(request, roll):
    if not request.user.is_staff:
        return redirect('')
    students = Student.objects.all()
    lst = []
    for student in students:
        branch = Branch.objects.filter(roll_no=student.roll_no)[0]
        lst.append([student.roll_no, student.name, branch.branch_name])
    student_to_be_added = Student.objects.filter(roll_no=roll)[0]
    lst2 = request.session["lst2"]
    flag = False
    for i in range(len(lst2)):
        if student_to_be_added.roll_no == lst2[i][0]:
            flag = True
    if not flag:
        lst2.append([student_to_be_added.roll_no, student_to_be_added.name])
    request.session["lst2"] = lst2
    return render(request, 'select_students.html', {"lst": lst, "lst2": lst2})

def remove_student(request, roll):
    if not request.user.is_staff:
        return redirect('')
    students = Student.objects.all()
    lst = []
    for student in students:
        branch = Branch.objects.filter(roll_no=student.roll_no)[0]
        lst.append(list([student.roll_no, student.name, branch.branch_name]))
    student_to_be_removed = Student.objects.filter(roll_no=roll)[0]
    lst2 = list(request.session["lst2"])
    for i in lst2:
        if student_to_be_removed.roll_no == i[0]:
            lst2.remove(i)
    request.session["lst2"] = lst2
    return render(request, 'select_students.html', {"lst": lst, "lst2": lst2})

def delete_students(request):
    if not request.user.is_staff:
        return redirect('')
    students = Student.objects.all()
    lst = []
    rolls = []
    for student in students:
        if student.roll_no not in rolls:
            lst.append(student)
            rolls.append(student.roll_no)
            continue
        for i in range(len(lst)):
            if student.roll_no == lst[i].roll_no and student.sem > lst[i].sem:
                lst[i] = student
                break
    
    return render(request, 'delete_students.html', {'lst': lst})

def delete_given_student(request, stu_id):
    if not request.user.is_staff:
        return redirect('')
    stu = Student.objects.get(id=stu_id)
    stu.delete()
    return redirect('/delete_students/')

def delete_branch(request):
    if not request.user.is_staff:
        return redirect('')
    branches = Branch.objects.all()
    return render(request, 'delete_branch.html', {'branches': branches})

def delete_given_branch(request, roll):
    if not request.user.is_staff:
        return redirect('')
    stus = Branch.objects.filter(roll_no=roll)
    for stu in stus:
        stu.delete()
    return redirect('/delete_branch/')

def delete_subject(request):
    if not request.user.is_staff:
        return redirect('')
    subjects = Subject.objects.all()
    return render(request, 'delete_subject.html', {'subjects' : subjects})

def delete_given_subject(request, sub_code):
    if not request.user.is_staff:
        return redirect('')
    subject = Subject.objects.get(subject_code=sub_code)
    subject.delete()
    return redirect('/delete_subject/')

def delete_offer(request):
    if not request.user.is_staff:
        return redirect('')
    offers = JobOffers.objects.all()
    return render(request, 'delete_offer.html', {'offers': offers})

def delete_given_offer(request, off_id):
    if not request.user.is_staff:
        return redirect('')
    has = HasOffers.objects.get(offer_id=off_id)
    job = JobOffers.objects.get(offer_id=off_id)
    job.delete()
    has.delete()
    return redirect('/delete_offer/')

def delete_performance(request):
    if not request.user.is_staff:
        return redirect('')
    pers = Performance.objects.all()
    return render(request, 'delete_performance.html', {'pers': pers})

def delete_given_performance(request, per_id):
    if not request.user.is_staff:
        return redirect('')
    per = Performance.objects.get(id=per_id)
    per.delete()
    return redirect('/delete_performance/')

def delete_test(request):
    if not request.user.is_staff:
        return redirect('')
    tests = Test.objects.all()
    return render(request, 'delete_test.html', {'tests': tests})

def delete_given_test(request, test_id):
    if not request.user.is_staff:
        return redirect('')
    test = Test.objects.get(id=test_id)
    test.delete()
    return redirect('/delete_test/')











def update_student(request):
    if not request.user.is_staff:
        return redirect('')
    students = Student.objects.all()
    return render(request, 'update_students.html', {'students': students})
    

def update_given_student(request, stu_id):
    if not request.user.is_staff:
        return redirect('')
    student = Student.objects.get(id=stu_id)
    if request.method == "POST":
        student.roll_no = request.POST["roll_no"]
        student.session = request.POST["session"]
        student.name = request.POST["name"]
        student.section = request.POST["section"]
        student.sem = request.POST["sem"]
        student.doa = request.POST["doa"]
        student.dob = request.POST["dob"]
        student.age = request.POST["age"]
        student.gap = request.POST["gap"]
        student.phone_no = request.POST["phone_no"]
        student.e_mail = request.POST["e_mail"]
        student.gender = request.POST["gender"]
        student.save()
        return redirect('/update_student/')
    return render(request, 'update_given_student.html', {'student': student})

def update_subject(request):
    if not request.user.is_staff:
        return redirect('')
    subjects = Subject.objects.all()
    return render(request, 'update_subject.html', {'subjects': subjects})

def update_given_subject(request, sub_code):
    if not request.user.is_staff:
        return redirect('')
    subject = Subject.objects.get(subject_code=sub_code)
    if request.method == 'POST':
        subject.subject_code = request.POST["subject_code"]
        subject.session = request.POST['session']
        subject.name = request.POST['name']
        subject.branch_code = request.POST['branch_code']
        subject.sem = request.POST['sem']
        subject.type = request.POST['type']
        subject.max_marks = request.POST['max_marks']
        subject.min_marks = request.POST['min_marks']
        subject.credit = request.POST['credit']
        subject.save()
        return redirect('/update_subject/')
    return render(request, 'update_given_subject.html', {'subject': subject})

def update_performance(request):
    if not request.user.is_staff:
        return redirect('')
    pers = Performance.objects.all()
    return render(request, 'update_performance.html', {'pers': pers})

def update_given_performance(request, roll):
    if not request.user.is_staff:
        return redirect('')
    per = Performance.objects.get(roll_no=roll)
    if request.method == 'POST':
        per.roll_no = request.POST["roll_no"]
        per.grade = request.POST['grade']
        per.save()
        return redirect('/update_performance/')
    return render(request, 'update_given_performance.html', {'per': per})






def insert_attendance(request):
    if not request.user.is_staff:
        return redirect('')
    if request.method == 'POST':
        att_data = pandas.read_excel(request.POST['att_file'])
        last = Attendance.objects.all().last().id + 1
        for ind in att_data.index:
            Attendance.objects.create(
                id=last,
                subject_code=att_data['subject_code'][ind],
                date=att_data['date'][ind],
                lecture_no=att_data['lecture_no'][ind],
                roll_no=att_data['roll_no'][ind],
                remarks=att_data['remarks'][ind],
            )
            last += 1 
        return redirect('/insert/')
    return render(request, 'insert_attendance.html')

def insert_branch(request):
    if not request.user.is_staff:
        return redirect('')
    if request.method == 'POST':
        Branch.objects.create(id=request.POST['id'],
        branch_code=request.POST['branch_code'],
        branch_name=request.POST['branch_name'],
        roll_no=request.POST['roll_no'],
        session=request.POST['session']
        )
        return redirect('/insert/')
    return render(request, 'insert_branch.html')
    
def insert_job(request):
    if not request.user.is_staff:
        return redirect('')
    if request.method == 'POST':
        HasOffers.objects.create(roll_no=request.POST['roll_no'],
        offer_id=request.POST['offer_id']
        )
        last_id = JobOffers.objects.all().last().id if JobOffers.objects.all() else 0
        JobOffers.objects.create(id=last_id + 1,
        offer_id=request.POST['offer_id'],
        company=request.POST['company'],
        package=request.POST['package'])
        return redirect('/insert/')
    return render(request, 'insert_job.html')
    
def insert_mock(request):
    if not request.user.is_staff:
        return redirect('')
    if request.method == 'POST':
        Mock.objects.create(
            id=request.POST['id'],
            session=request.POST['session'],
            subject_name=request.POST['subject_name'],
            subject_code=request.POST['subject_code'],
            roll_no=request.POST['roll_no'],
            obtained_marks=request.POST['obtained_marks'],
            max_marks=request.POST['max_marks']
            )
        return redirect('/insert/')
    return render(request, 'insert_mock.html')

def insert_test(request):
    if not request.user.is_staff:
        return redirect('')
    if request.method == 'POST':
        Test.objects.create(
            id=request.POST['id'],
            session=request.POST['session'],
            subject_name=request.POST['subject_name'],
            type=request.POST['type'],
            subject_code=request.POST['subject_code'],
            roll_no=request.POST['roll_no'],
            obtained_marks=request.POST['obtained_marks'],
            max_marks=request.POST['max_marks']
            )
        return redirect('/insert/')
    return render(request, 'insert_test.html')

def insert_performance(request):
    if not request.user.is_staff:
        return redirect('')
    if request.method == 'POST':
        per_data = pandas.read_excel(request.POST['per_file'])
        for ind in per_data.index:
            Performance.objects.create(
                roll_no=per_data['roll_no'][ind],
                grade=per_data['grade'][ind],
            )
            students = Student.objects.filter(roll_no=per_data['roll_no'][ind])
            for student in students:
                student.graded = 1
                student.save()
        return redirect('/insert/')
    return render(request, 'insert_performance.html')

def insert_session(request):
    if not request.user.is_staff:
        return redirect('')
    if request.method == 'POST':
        ses_data = pandas.read_excel(request.POST['ses_file'])
        last_id = Session.objects.all().last().id
        for ind in ses_data.index:
            Session.objects.create(
                id=last_id + 1,
                roll_no=ses_data['roll_no'][ind],
                session=ses_data['session'][ind],
            )
            last_id += 1
        return redirect('/insert/')
    return render(request, 'insert_session.html')

def insert_student(request):
    if not request.user.is_staff:
        return redirect('')
    if request.method == "POST":
        Student.objects.create(id=Student.objects.all().last().id + 1,
        roll_no = request.POST["roll_no"],
        session = request.POST["session"],
        name = request.POST["name"],
        section = request.POST["section"],
        sem = request.POST["sem"],
        doa = request.POST["doa"],
        dob = request.POST["dob"],
        age = request.POST["age"],
        gap = request.POST["gap"],
        phone_no = request.POST["phone_no"],
        e_mail = request.POST["e_mail"],
        gender = request.POST["gender"],
        graded=0
        )
        return redirect('/insert/')
    return render(request, 'insert_student.html')

def insert_subject(request):
    if not request.user.is_staff:
        return redirect('')
    if request.method == "POST":
        Subject.objects.create(subject_code=request.POST['subject_code'] ,
        session = request.POST["session"],
        name = request.POST["name"],
        sem = request.POST["sem"],
        branch_code=request.POST['branch_code'],
        type=request.POST['type'],
        max_marks=request.POST['max_marks'],
        min_marks=request.POST['min_marks'],
        credit=request.POST['credit']
        )
        return redirect('/insert/')
    return render(request, 'insert_subject.html')