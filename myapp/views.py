from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username Taken')
                return redirect('index')
            else:
                user = User.objects.create_user(first_name = firstname, last_name = lastname, email = email,
                                                username = username, password = password)
                user.save()
                print('user created')
                return redirect('login_page')
        else:
            messages.info(request, 'password not matching')
            return redirect('index')
    else:
            return redirect('index')
        
def login_page(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            request.session['username'] = username
            messages.info(request, 'logged in successfully')
            return redirect('gallery')
        else:
            messages.info(request, 'incorrect username or password')
            return redirect('login')
    else:
            return redirect('login')
    
    
@login_required(login_url='login_page')
def gallery(request):
    
    print(request.session['username'])
    return render(request, 'gallery.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def reg(request):
    return render(request, 'reg.html')

def imageregister(request):
    if request.method == 'POST':
        image = request.FILES['image']
        upload = Upload_image(image=image)
        upload.save()
        return redirect('reg')
    
def imageshow(request):
    empty = Upload_image.objects.all()
    return render(request, 'imageshow.html', {'empty':empty})


def profile(request):
    return render(request, 'profile.html')

def profilesave(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        images = request.FILES['images']
        mobile = request.POST['mobile']
        address = request.POST['address']
        pro =  Profile_card(name=name, email=email, images=images )
        pro.save()
        
        pr = Pr_card(mobile=mobile, address=address, userid = pro)
        pr.save()
        return redirect('profileshow')
    else:
        return redirect('profile')
    
def profileshow(request):
    show = Pr_card.objects.all()
    return render(request, 'profileshow.html',{'show': show})

def profileedit(request,userid):
    pro = Profile_card.objects.get(userid = userid)
    show = Pr_card.objects.get(userid=pro)
    return render(request, 'profileedit.html', {'show':show})

def profileupdate(request,userid):
    if request.method == 'POST':
        pro = Profile_card.objects.get(userid = userid)
        pro.name = request.POST.get('name',pro.name)
        pro.email = request.POST.get('email',pro.email)
        pro.images = request.FILES['images']
        pro.save()
        show = Pr_card.objects.get(userid = pro)
        show.mobile = request.POST.get('mobile',show.mobile)
        show.address = request.POST.get('address',show.address)
        show.save()
        
        return redirect('profileshow')
    
    
def name(request):
    qwer = Profile_card.objects.all()
    try:
        name = request.POST['name']
        email=request.POST['email']
    
        if Profile_card.objects.filter(name=name).exists():
            qwer  =   Profile_card.objects.filter(name=name)
        elif Profile_card.objects.filter(email=email).exists():
            qwer  =   Profile_card.objects.filter(email=email)  
        elif Profile_card.objects.filter(name=name,email=email).exists():
            qwer = Profile_card.objects.filter(name=name,email=email)
    except:
        
        pass
    
    return render(request, 'name.html',{'qwer':qwer})