from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserLogin, UserSignUp, Verification, FirstName, LastName, Password, Visit, VisitTimeChoice, Username
from .models import User, VisitTime, VTD, Medicine
from django.core.mail import send_mail
from django.conf import settings
import random
from datetime import datetime, date


def sign_in(request):
    if request.method == "GET":
        form = UserLogin()
        return render(request, "reserve/sign-in.html", {'form': form})
    else:
        form = UserLogin(request.POST)
        if form.is_valid():
            global userr
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            userr = username
            try:
                check = User.objects.get(username=username)
                if check.username:
                    if check.password == password:
                        if check.verify == "ok":
                            if check.role == 'user':
                                return redirect('homepage')
                            elif check.role == 'doctor':
                                return redirect('doctor_page')
                            elif check.role == 'secretary':
                                return HttpResponse("SALAM MONSHI")
                        else:
                            return redirect('verification/')
                    else:
                        inv = 0
                        form = UserLogin
                        return render(request, "reserve/sign-in.html", {'form': form, 'inv': inv})
                else:
                    inv = 0
                    form = UserLogin
                    return render(request, "reserve/sign-in.html", {'form': form, 'inv': inv})
            except:
                inv = 0
                form = UserLogin
                return render(request, "reserve/sign-in.html", {'form': form, 'inv': inv})
        else:
            inv = 0
            form = UserLogin
            return render(request, "reserve/sign-in.html", {'form': form, 'inv': inv})


def sign_up(request):
    if request.method == "GET":
        form = UserSignUp()
        return render(request, "reserve/sign-up.html", {'form': form})
    else:
        form = UserSignUp(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            email = userObj['email']
            username = userObj['username']
            phone_number = userObj['phone_number']
            try:
                check_em = User.objects.get(email=email)
                check_us = User.objects.get(username=username)
                check_ph = User.objects.get(phone_number=phone_number)
                if check_em:
                    em = 0
                    form = UserSignUp
                    return render(request, "reserve/sign-up.html", {'form': form, 'em': em})
                if check_us:
                    us = 0
                    form = UserSignUp
                    return render(request, "reserve/sign-up.html", {'form': form, 'us': us})
                if check_ph:
                    ph = 0
                    form = UserSignUp
                    return render(request, "reserve/sign-up.html", {'form': form, 'ph': ph})
            except:
                form.save()
                return render(request, "reserve/sign-up-s.html")
        else:
            form = UserSignUp
            em_ex = 0
            return render(request, "reserve/sign-up.html", {'form': form, "em_ex": em_ex})


def homepage(request):
    return render(request, "reserve/homepage.html")


def verification(request):
    if request.method == 'GET':
        form = Verification()
        low = 1000
        high = 9999
        global ran_number
        ran_number = random.uniform(low, high)
        z = int(ran_number)
        subject = 'Verification Email'
        message = 'This is your verification code: ' + str(z)
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        return render(request, "reserve/verify.html", {'form': form})
    else:
        form = Verification(request.POST)
        if form.is_valid():
            userCode = form.cleaned_data
            code = userCode['verify']
            codee = str(int(code))
            rande = str(int(ran_number))
            if codee == rande:
                user_edit = User.objects.get(username=userr)
                user_edit.verify = "ok"
                user_edit.save()
                return render(request, "reserve/homepage.html")
            else:
                return HttpResponse("HEH")


def menu(request):
    return render(request, "reserve/menu.html")


def edit_profile(request):
    return render(request, "reserve/editprofile.html")


def edit_firstname(request):
    if request.method == 'GET':
        form = FirstName()
        return render(request, "reserve/editfirstname.html", {'form': form})
    else:
        form = FirstName(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            first_name = userObj['first_name']
            user_edit = User.objects.get(username=userr)
            user_edit.first_name = first_name
            user_edit.save()
            return render(request, "reserve/change.html")


def edit_lastname(request):
    if request.method == 'GET':
        form = LastName()
        return render(request, "reserve/editlastname.html", {'form': form})
    else:
        form = LastName(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            last_name = userObj['last_name']
            user_edit = User.objects.get(username=userr)
            user_edit.last_name = last_name
            user_edit.save()
            return render(request, "reserve/change.html")


def edit_password(request):
    if request.method == 'GET':
        form = Password()
        return render(request, "reserve/editpassword.html", {'form': form})
    else:
        form = Password(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            password = userObj['password']
            user_edit = User.objects.get(username=userr)
            user_edit.password = password
            user_edit.save()
            return render(request, "reserve/change.html")


def view_profile(request):
    check = User.objects.get(username=userr)
    if check.case_number:
        hav = 0
    else:
        check.case_number = int(random.uniform(10000, 99999))
        check.save()
    return render(request, "reserve/view_profile.html",
                  {'last_name': check.last_name, 'first_name': check.first_name, 'email': check.email,
                   'phone_number': check.phone_number, 'case_number': check.case_number})


Uhr = datetime.now()

def x(request):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    tim = str(current_time)
    return HttpResponse(tim[0])


heute = date.today()


def add_time(request):
    if request.method == 'GET':
        form = Visit()
        return render(request, "reserve/add_time.html", {'form': form})
    else:
        form = Visit(request.POST)
        if form.is_valid():
            check = User.objects.get(username=userr)
            id = check.id

            date = form.cleaned_data
            datee = date['date']

            s = str(heute)
            s = s.split("-")
            z = []
            z.append(int(s[0]))
            z.append(int(s[1]))
            z.append(int(s[2]))

            s1 = str(datee)
            s1 = s1.split("-")
            z1 = []
            z1.append(int(s1[0]))
            z1.append(int(s1[1]))
            z1.append(int(s1[2]))

            start = date['start_time']
            end = date['end_time']

            cherk = VisitTime.objects.all()
            for i in cherk:
                if i.doctor_id == id:
                    if i.date == datee:
                        if start < i.start_time and end < i.start_time:
                            continue
                        elif start > i.end_time and end > i.end_time:
                            continue
                        else:
                            return HttpResponse("خعلی زرنجی‌")
                    else:
                        continue
                else:
                    continue

            if (z1[0] - z[0]) * 360 + (z1[1] - z[1]) * 60 + (z1[2] - z[2]) > 30:
                tarikh = 0
                form = Visit()
                return render(request, 'reserve/add_time.html', {'form': form, 'tarikh': tarikh})
            elif datee < datetime.date(datetime.now()):
                past = 0
                form = Visit()
                return render(request, 'reserve/add_time.html', {'form': form, 'past': past})
            elif start == end:
                gleich = 0
                form = Visit()
                return render(request, 'reserve/add_time.html', {'form': form, 'gleich': gleich})
            elif start > end:
                greater = 0
                form = Visit()
                return render(request, 'reserve/add_time.html', {'form': form, 'greater': greater})
            else:
                m = str(start)
                e = str(end)

                stt = m.split(":")
                en = e.split(":")

                stt_min = int(stt[1])
                stt_h = int(stt[0])

                end_min = int(en[1])
                end_h = int(en[0])

                while ((end_h - stt_h) * 60) + end_min - stt_min >= 20:
                    time_str1 = str(stt_h) + "::" + str(stt_min) + "::00"
                    time_object1 = datetime.strptime(time_str1, '%H::%M::%S').time()
                    stt_min = stt_min + 20
                    if stt_min >= 60:
                        stt_min = stt_min - 60
                        stt_h = stt_h + 1

                    else:
                        stt_min = stt_min
                        stt_h = stt_h

                    time_str2 = str(stt_h) + "::" + str(stt_min) + "::00"
                    time_object2 = datetime.strptime(time_str2, '%H::%M::%S').time()

                    VisitTime.objects.create(date=datee, start_time=time_object1, end_time=time_object2,
                                             doctor_id=check.id)
                return HttpResponse("Hale dadash!")

        else:
            val = 0
            form = Visit()
            return render(request, 'reserve/add_time.html', {'form': form, 'val': val})


def view_reserves(request):
    if request.method == "GET":
        form = VisitTimeChoice()
        check = VisitTime.objects.all()
        a = []
        for i in check:
            if i.doctor_id is None:
                continue
            else:
                a.append(str(i.doctor_id))
        role = User.objects.get(username=userr)
        docis = User.objects.all()
        if role.role == "doctor":
            rolee = 0
        else:
            rolee = 1

        return render(request, "reserve/view_reserves.html",
                      {'check': check, 'form': form, 'rolee': rolee, 'role': role, 'doocis': docis})
    else:
        form = VisitTimeChoice(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            id = userObj['id']
            try:
                checkk = VisitTime.objects.get(id=id)
                pati = User.objects.get(username=userr)
                checkk.user_id = pati.id
                checkk.empty = False
                checkk.save()
                doctor = VisitTime.objects.get(id=id)
                doc_name = User.objects.get(id=doctor.doctor_id)
                name = doc_name.last_name
                return render(request, "reserve/reserve_suc.html", {'name': name})
            except:
                return HttpResponse('Addad doros bezan')


def doctor_page(request):
    return render(request, 'reserve/doctor_homepage.html')


def reserved_list(request):
    visit_mod = User.objects.get(username=userr)
    user_mod = VisitTime.objects.filter(user_id=visit_mod.id)
    users = User.objects.all()
    return render(request, 'reserve/reserved_list.html', {'a': user_mod, 'users': users})


def patient_list(request):
    if request.method == "GET":
        form = Username()
        doctor = User.objects.get(username=userr)
        patient = VisitTime.objects.filter(doctor_id=doctor.id)
        a = []
        count = 0
        res = 0
        for i in patient:
            if i.user_id != None:
                user = User.objects.get(id=i.user_id).username
                if count == 0:
                    a.append(user)
                    count += 1
                else:
                    for j in a:
                        if j == user:
                            res += 1
                            continue
                    if res == 0:
                        a.append(user)
                    else:
                        res = 0
            else:
                continue
        return render(request, "reserve/patient_list.html", {'a': a, 'form': form})
    else:
        form = Username(request.POST)
        if form.is_valid():
            try:
                userObj = form.cleaned_data
                username = userObj['username']
                kiee = User.objects.get(username=username)
                dateeee = VisitTime.objects.filter(user_id=kiee.id)
                a = []
                for i in dateeee:
                    a.append(i.id)
                b = []
                for j in a:
                    med = VTD.objects.filter(visit_time_id=j)
                    for v in med:
                        b.append(v)
                c = []
                for j in b:
                    c.append(j.id)

                class Information:
                    def __init__(self, docesh, ahh, zaman, medicine, count):
                        self.docesh = docesh
                        self.ahh = ahh
                        self.zaman = zaman
                        self.medicine = medicine
                        self.count = count

                main_list = []
                for e in c:
                    count = VTD.objects.get(id=e).value

                    med_id = VTD.objects.get(id=e).medicine_id
                    medicine = Medicine.objects.get(id=med_id).name

                    pati = VTD.objects.get(id=e).visit_time_id

                    docr = VisitTime.objects.get(id=pati).doctor_id
                    docesh = User.objects.get(id=docr).username

                    zaman = VisitTime.objects.get(id=pati).date

                    tiii = VisitTime.objects.get(id=pati).user_id
                    ahh = User.objects.get(id=tiii).username

                    person = Information(str(docesh), str(ahh), str(zaman), str(medicine), str(count))
                    main_list.append(person)
                return render(request, 'reserve/medical_records.html', {'list': main_list})
            except:
                val = 0
                form = Username()
                doctor = User.objects.get(username=userr)
                patient = VisitTime.objects.filter(doctor_id=doctor.id)
                a = []
                count = 0
                res = 0
                for i in patient:
                    if i.user_id != None:
                        user = User.objects.get(id=i.user_id).username
                        if count == 0:
                            a.append(user)
                            count += 1
                        else:
                            for j in a:
                                if j == user:
                                    res += 1
                                    continue
                            if res == 0:
                                a.append(user)
                            else:
                                res = 0
                    else:
                        continue
                return render(request, "reserve/patient_list.html", {'a': a, 'form': form, 'val': val})


def delete_past(request):
    if request.method == "GET":
        form = VisitTimeChoice()
        joine = User.objects.get(username=userr).id
        check = VisitTime.objects.filter(doctor_id=joine)
        a = []
        for i in check:
            if i.date >= heute:
                continue
            else:
                a.append(i)

        return render(request, "reserve/visit_past.html",
                      {'a': a, 'form': form})
    else:
        form = VisitTimeChoice(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            id = userObj['id']
            try:
                checkk = VisitTime.objects.get(id=id)
                checkk.delete()
                checkk.save()
                return HttpResponse("HALEEE")
            except:
                return HttpResponse('Addad doros bezan')


def view_records(request):
    kiee = User.objects.get(username=userr)
    dateeee = VisitTime.objects.filter(user_id=kiee.id)
    a = []
    for i in dateeee:
        a.append(i.id)
    b = []
    for j in a:
        med = VTD.objects.filter(visit_time_id=j)
        for v in med:
            b.append(v)
    c = []
    for j in b:
        c.append(j.id)

    class Information:
        def __init__(self, docesh, ahh, zaman, medicine, count):
            self.docesh = docesh
            self.ahh = ahh
            self.zaman = zaman
            self.medicine = medicine
            self.count = count

    main_list = []
    for e in c:
        count = VTD.objects.get(id=e).value

        med_id = VTD.objects.get(id=e).medicine_id
        medicine = Medicine.objects.get(id=med_id).name

        pati = VTD.objects.get(id=e).visit_time_id

        docr = VisitTime.objects.get(id=pati).doctor_id
        docesh = User.objects.get(id=docr).username

        zaman = VisitTime.objects.get(id=pati).date

        tiii = VisitTime.objects.get(id=pati).user_id
        ahh = User.objects.get(id=tiii).username

        person = Information(str(docesh), str(ahh), str(zaman), str(medicine), str(count))
        main_list.append(person)
    return render(request, 'reserve/medical_records.html', {'list': main_list})


def cancel_visit(request):
    pat = User.objects.get(username=userr).id
    list = VisitTime.objects.filter(user_id=pat)
    d = []
    for i in list:
        if i.date == heute:
            d.append(i.user_id)
        else:
            continue
    return HttpResponse()
