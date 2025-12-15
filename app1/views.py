from django.shortcuts import render,redirect

from app1.models import department_model,hod_model,professor_model,student_model
from app1.forms import department_form,hod_form,professor_form,student_form
from app1.forms1 import department_u_form,hod_u_form,professor_u_form,student_u_form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def register_form(request):
   message=''
   if request.method=="POST":
      username=request.POST.get("reg_username")
      useremail=request.POST.get("reg_useremail")
      p1=request.POST.get("reg_userpassword")
      p2=request.POST.get("reg_userconpassword")

      if p1!=p2:
         message="Please Enter Valid Password"

      elif User.objects.filter(email=useremail).exists():
         message="Email Already Exists"
      else:
         user=User.objects.create_user(username=username,email=useremail,password=p1)
         user.save()
         message="User Create Successfully"
         return redirect("log101")
   return render(request,"frontend_app1/reg.html",{"message": message})
      
def login1_form(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("log_userneme")
        password = request.POST.get("log_userpassword")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home101")   
        else:
            message = "Invalid Username or Password"

    return render(request,"frontend_app1/login.html",{"message": message})

def home(request):
   dept_total=department_model.objects.count()
   hod_total=hod_model.objects.count()
   professor_total = professor_model.objects.count()
   students_total = student_model.objects.count()
   content = {
      "dept_total":dept_total,
      "hod_total":hod_total,
      "professor_total":professor_total,
      "students_total":students_total
   }

   return render(request,'frontend_app1/home.html',content)

#Department
def department_table(request):
    data=department_model.objects.all()
    content={
        "data":data
    }
    return render(request,'frontend_app1/department_table.html',content)

def department_empty_form(request):
    form=department_form()
    if request.method=="POST":
       form=department_form(request.POST)
       if form.is_valid():
          form.save()
          return redirect('dept_table101')
    else:
     form=department_form()
     content={
         "form":form
     }
    return render(request,'frontend_app1/department_form.html',content)
def department_update_form(request,id):
    data=department_model.objects.get(id=id)
    if request.method=="POST":
       form=department_u_form(request.POST,instance=data)
       if form.is_valid():
          form.save()
          return redirect('dept_table101')
    else:
     form=department_u_form(instance=data)
     content={
         "form":form
     }
    return render(request,'frontend_app1/department_n_form.html',content)
    
def department_delete(request,id):
   data=department_model.objects.get(id=id)
   data.delete()
   return redirect('dept_table101')



#HOD
def hod_table(request):
    data=hod_model.objects.all()
    content={
        "data":data
    }
    return render(request,'frontend_app1/hod_table.html',content)



def hod_empty_form(request):
    if request.method == "POST":
        form = hod_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hod_table101')
    else:
     form = hod_form()
     content = {
        "form":form
     }
    return render(request, 'frontend_app1/hod_form.html', content)

    


def hod_update_form(request,id):
    data=hod_model.objects.get(id=id)
    if request.method=="POST":
       form=hod_u_form(request.POST,instance=data)
       if form.is_valid():
          form.save()
          return redirect('hod_table101')
    else:
     form=hod_u_form(instance=data)
     content={
         "form":form
     }
    return render(request,'frontend_app1/hod_n_form.html',content)
    
def hod_delete(request,id):
   data=hod_model.objects.get(id=id)
   data.delete()
   return redirect('hod_table101')



#Professor
def professor_table(request):
    data=professor_model.objects.all()
    content={
        "data":data
    }
    return render(request,'frontend_app1/professor_table.html',content)

def professor_empty_form(request):
    form=professor_form()
    if request.method=="POST":
       form=professor_form(request.POST)
       if form.is_valid():
          form.save()
          return redirect('professor_table101')
    else:
     form=professor_form()
     content={
         "form":form
     }
    return render(request,'frontend_app1/professor_form.html',content)
def professor_update_form(request,id):
    data=professor_model.objects.get(id=id)
    if request.method=="POST":
       form=professor_u_form(request.POST,instance=data)
       if form.is_valid():
          form.save()
          return redirect('professor_table101')
    else:
     form=professor_u_form(instance=data)
     content={
         "form":form
     }
    return render(request,'frontend_app1/professor_n_form.html',content)
    
def professor_delete(request,id):
   data=professor_model.objects.get(id=id)
   data.delete()
   return redirect('professor_table101')



#Student
def student_table(request):
    data=student_model.objects.all()
    content={
        "data":data
    }
    return render(request,'frontend_app1/student_table.html',content)

def student_empty_form(request):
    form=student_form()
    if request.method=="POST":
       form=student_form(request.POST)
       if form.is_valid():
          form.save()
          return redirect('student_table101')
    else:
     form=student_form()
     content={
         "form":form
     }
    return render(request,'frontend_app1/student_form.html',content)
def student_update_form(request,id):
    data=student_model.objects.get(id=id)
    if request.method=="POST":
       form=student_u_form(request.POST,instance=data)
       if form.is_valid():
          form.save()
          return redirect('student_table101')
    else:
     form=student_u_form(instance=data)
     content={
         "form":form
     }
    return render(request,'frontend_app1/student_n_form.html',content)
    
def student_delete(request,id):
   data=student_model.objects.get(id=id)
   data.delete()
   return redirect('student_table101')



def verify_user(request, action, model_name, id):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:

            # -------- DEPARTMENT --------
            if model_name == "department":
                if action == "update":
                    return redirect("dept_form102", id=id)
                if action == "delete":
                    return redirect("dept_delete101", id=id)

            # -------- HOD --------
            if model_name == "hod":
                if action == "update":
                    return redirect("hod_form102", id=id)
                if action == "delete":
                    return redirect("hod_delete101", id=id)

            # -------- PROFESSOR --------
            if model_name == "professor":
                if action == "update":
                    return redirect("professor_form102", id=id)
                if action == "delete":
                    return redirect("professor_delete101", id=id)

            # -------- STUDENT --------
            if model_name == "student":
                if action == "update":
                    return redirect("student_form102", id=id)
                if action == "delete":
                    return redirect("student_delete101", id=id)

        else:
            message = "Invalid Username or Password"

    return render(request, "frontend_app1/verify.html", {"message": message})