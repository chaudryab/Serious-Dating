import json
from django.db.models.expressions import OrderBy
from django.http import response
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import update_session_auth_hash
from .helpers import *
from adminn.models import *
import uuid
from django.http import HttpResponseRedirect
from api.models import *
from chat.models import *
import datetime
from django.db.models import Q
from django.core.paginator import Paginator
# from .models import *
from .forms import *
from bs4 import BeautifulSoup



# Create your views here.

#-----------------------------------------------  Admin --------------------------------------------------------

#------------- Login --------------
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            if user.is_superuser:
                auth.login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Invalid Crendentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

#------------- Dashboard --------------
@login_required
def index(request):
    active_users=Users.objects.filter(status=1)
    active_user=0
    for e in active_users:
        if e.is_deleted == 0:
            active_user = active_user + 1
    non_active_users=Users.objects.filter(status=0)
    non_active_user=0
    for e in non_active_users:
        if e.is_deleted == 0:
            non_active_user = non_active_user + 1
    pro_users=Users.objects.filter(pro=1)
    pro_user=0
    for e in pro_users:
        if e.is_deleted == 0:
            pro_user = pro_user + 1
    free_users=Users.objects.filter(pro=0)
    free_user=0
    for e in free_users:
        if e.is_deleted == 0:
            free_user = free_user + 1
    t_earning = Purchased_subscriptions.objects.filter(from_date = datetime.date.today())
    today_earning=0
    for e in t_earning:
        today_earning = today_earning + e.amount
    earning = Purchased_subscriptions.objects.all()
    total_earning=0
    for e in earning:
        total_earning = total_earning + e.amount
    resolved_reports=Reports.objects.filter(status=0).count()
    unresolved_reports=Reports.objects.filter(status=1).count()
    users = {'active_user':active_user,'non_active_user':non_active_user,'pro_user':pro_user,'free_user':free_user,'total_earning':total_earning,'today_earning':today_earning,'resolved_reports':resolved_reports,'unresolved_reports':unresolved_reports}
    return render(request,'index.html',users)

#------------- Pro Users in Dashboard --------------
@login_required
def pro_users(request):
    pro_users = Users.objects.filter(pro=1,is_deleted=0).order_by('-id')
    users={'pro_users':pro_users}
    return render(request,'pro_users.html',users)

#------------- Free Users in Dashboard --------------
@login_required
def free_users(request):
    free_users = Users.objects.filter(pro=0,is_deleted=0).order_by('-id')
    users={'free_users':free_users}
    return render(request,'free_users.html',users)


#------------- Today Earning in Dashboard --------------
@login_required
def today_earning(request):
    today_earning = Purchased_subscriptions.objects.filter(from_date = datetime.date.today()).order_by('-id')
    users={'today_earning':today_earning}
    return render(request,'today_earning.html',users)

#------------- Total Earning in Dashboard --------------
@login_required
def total_earning(request):
    total_earning = Purchased_subscriptions.objects.order_by('-id').all()
    users={'total_earning':total_earning}
    return render(request,'total_earning.html',users)
    
    
#------------- Users Registered Per Month Graph In Admin Panel --------------
@login_required
def RegisterationChart(request):
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    labels = []
    users_count = []
    thisYear = True
    current_date = datetime.date.today()
    current_month = current_date.month
    current_year = current_date.year
    i=0
    while i<12:
        month = (current_month-i)-1
        if month < 0:
            month = month+12
            thisYear = False
        if thisYear == True:
            date = month_names[month] +' '+ str(current_year)
            users_reg_count = Users.objects.filter(Q(created_at__year=current_year) & Q(created_at__month=month+1)).count()
            users_count.append(str(users_reg_count))

        else:
            date = month_names[month] +' '+str(current_year-1)
            users_reg_count = Users.objects.filter(Q(created_at__year=current_year-1) & Q(created_at__month=month+1)).count()
            users_count.append(str(users_reg_count))

        i = i+1
        labels.append(date)
    
    return JsonResponse({'months': labels, 'users_count': users_count}, safe=False)

#------------- Earnings Per Month Graph In Admin Panel --------------
@login_required
def EarningsChart(request):
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    labels = []
    amount = 0
    total_earning = []
    thisYear = True
    current_date = datetime.date.today()
    current_month = current_date.month
    current_year = current_date.year
    i=0
    while i<12:
        amount = 0
        month = (current_month-i)-1
        if month < 0:
            month = month+12
            thisYear = False
        if thisYear == True:
            date = month_names[month] +' '+ str(current_year)
            earnings = Purchased_subscriptions.objects.filter(Q(created_at__year=current_year) & Q(created_at__month=month+1))
            for t in earnings:
                amount = amount + t.amount

        else:
            date = month_names[month] +' '+str(current_year-1)
            earnings = Purchased_subscriptions.objects.filter(Q(created_at__year=current_year-1) & Q(created_at__month=month+1))
            for t in earnings:
                amount = amount + t.amount
        total_earning.append(str(amount))

        i = i+1
        labels.append(date)
    
    return JsonResponse({'months': labels, 'total_earning': total_earning}, safe=False)


#------------- Admin Change Password --------------
@login_required
@csrf_exempt
def change_password(request):
    superusers = User.objects.get(is_superuser=True)

    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        superusers = User.objects.get(is_superuser=True)
        if check_password(old_password,superusers.password):
            if int(len(new_password)) < 6:
                messages.error(request, 'Password Must Contains Six Characters!!')
                return redirect('change_password')
            elif new_password == confirm_password:
                super_pwd = make_password(new_password, None, 'md5')
                superusers.password = super_pwd
                superusers.save()
                messages.success(request, 'Password successfully changed.')
                update_session_auth_hash(request, superusers)
                return redirect('change_password')
            else:
                messages.error(request, 'Password Did Not Match!!')
                return redirect('change_password')
        else:
            messages.error(request, 'Invalid Old Password!!')
            return redirect('change_password')
    return render(request,'change_password.html')

#------------- Forget Password --------------
@csrf_exempt
def forget_pwd(request):
    if request.method == 'POST':
        email = request.POST['email']
        superuser = User.objects.get(is_superuser=True)
        if superuser.email == email:
            token = str(uuid.uuid4())
            admin_token = Admin_token.objects.get(id=1)
            admin_token.token = token
            admin_token.save()
            send_admin_forget_password_mail(email,token)
            messages.success(request, 'Email Sent!!')
            return redirect('forget_pwd')
        else:
            messages.error(request, 'Email Not Exist!!')
            return redirect('forget_pwd')

    return render(request,'forget_pwd.html')

#------------- Reset Password --------------
@csrf_exempt
def reset_pwd(request,token):
    if request.method == 'GET':
        if Admin_token.objects.filter(token=token).exists():
            return render(request, 'reset_pwd.html')
        else:
            return redirect('error_404')
    else:
        if request.method == 'POST':
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']
            print(new_password == confirm_password)
            superusers = User.objects.get(is_superuser=True)
            if int(len(new_password)) < 6:
                messages.error(request, 'Password Must Contains Six Characters!!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            elif new_password == confirm_password:
                super_pwd = make_password(new_password, None, 'md5')
                superusers = User.objects.get(is_superuser=True)
                superusers.password = super_pwd
                admin_token = Admin_token.objects.filter(id=1).first()
                admin_token.token = ''
                superusers.save()
                admin_token.save()
                messages.success(request, 'Password Changed!!')
                return redirect('success')
            else:
                messages.error(request, 'Password Did Not Match!!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            return redirect('error_404')

#------------- Admin Logout --------------
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

#------------- Error-404 Page --------------
def error_404(request):
    return render(request,'error_404.html')

#------------- Success Page--------------
def success(request):
    return render(request,'success.html')

#------------- Active Users --------------
@login_required
def active_users(request):
    users=Users.objects.filter(status=1,is_deleted=0).order_by('-id').all()
    user = {"users": users}
    return render(request,'active_users.html',user)

#------------- User Detail --------------
@login_required
def user_detail(request,pk):
    users=Users.objects.filter(id=pk)
    subscription=Purchased_subscriptions.objects.filter(user_id=pk)
    matching=Matchings.objects.filter(user_id=pk)
    matched=Matchings.objects.filter(match_id=pk)
    block_users=Blocked_users.objects.filter(user_id=pk)
    reports=Reports.objects.filter(user_id=pk)
    likes_recieved=Matchings.objects.filter(match_id=pk).count()
    likes_send=Matchings.objects.filter(user_id=pk).count()
    matchings=Matchings.objects.filter(user_id=pk)
    t_meetings=Chat.objects.filter( (Q(sender=pk) | Q(receiver=pk)) & ~Q(address=None) & Q(delete_chat_by_user1=0,delete_chat_by_user2=0)).count()
    t_reports=Reports.objects.filter(user_id=pk).count()
    money=Purchased_subscriptions.objects.filter(user_id=pk)
    chats = list(Chat.objects.filter( (Q(sender=pk) | Q(receiver=pk)) & ~Q(address=None) & Q(delete_chat_by_user1=0,delete_chat_by_user2=0)).values('id','sender','receiver','address','latitude','longitude','date','time'))
    meetings = []
    if len(chats) > 0:
        for chat in chats:
            if int(chat['sender']) == int(pk):
                user =list(Users.objects.filter(id=chat['receiver']).values())
                chat['user'] = user[0]
                meetings.append(chat)
            elif int(chat['receiver']) == int(pk):
                user = Users.objects.filter(id=chat['sender']).values()
                chat['user'] = user[0]
                meetings.append(chat)
    t_matchings=0
    for e in matchings:
        if e.liked_by_user1 == 1 and e.liked_by_user2 == 1:
            t_matchings = t_matchings + 1
    spend_money=0
    for e in money:
        spend_money = spend_money + e.amount
    user = {"users": users,"subscription": subscription,"matching": matching,"matched":matched,
    "block_users": block_users,"reports": reports,'meetings': meetings,'t_meetings':t_meetings,
    't_reports':t_reports,'spend_money':spend_money,'t_matchings':t_matchings,'likes_recieved':likes_recieved,'likes_send':likes_send}
    return render(request,'user_detail.html',user)

#------------- MAP --------------
@login_required
def map(request,pk):
    meeting = Chat.objects.filter(pk=pk).first()
    return render(request,'map.html',{'meeting':meeting})
#------------- User Block --------------
@login_required
def user_block(request,pk):
    users=Users.objects.filter(id=pk).first()
    users.status=0
    users.save()
    sbj = 'Your Serious Dating Account Temporary Blocked'
    email = users.email
    auto_msg = Auto_msg.objects.filter(id=1).first()
    message =auto_msg.admin_block
    title = 'Your Serious Dating Account Temporary Blocked'
    auto_message(sbj,email,title,message)
    messages.success(request,"User Blocked Successfully !!")
    return redirect('active_users')

#------------- User Active --------------
@login_required
def user_active(request,pk):
    users=Users.objects.filter(id=pk).first()
    users.status=1
    users.save()
    sbj = 'Your Serious Dating Account Activated'
    email = users.email
    auto_msg = Auto_msg.objects.filter(id=1).first()
    message =auto_msg.admin_unblock
    title = 'Your Serious Dating Account Activated'
    auto_message(sbj,email,title,message)
    messages.success(request,"User Active Successfully !!")
    return redirect('blocked_users')

#------------- User Delete --------------
@login_required
def user_delete(request,pk):
    users=Users.objects.filter(id=pk).first()
    users.status=0
    users.is_deleted=1
    users.save()
    sbj = 'Your Serious Dating Account Permanent Blocked'
    email = users.email
    auto_msg = Auto_msg.objects.filter(id=1).first()
    message =auto_msg.user_delete
    title = 'Your Serious Dating Account Permanent Blocked'
    auto_message(sbj,email,title,message)
    messages.success(request,"User Deleted Successfully !!")
    return redirect('active_users')

@login_required
def user_block_delete(request,pk):
    users=Users.objects.filter(id=pk).first()
    users.is_deleted=1
    users.save()
    sbj = 'Admin has deleted your acount!!'
    email = users.email
    auto_msg = Auto_msg.objects.filter(id=1).first()
    message =auto_msg.user_delete
    auto_message(sbj,email,message)
    messages.success(request,"User Deleted Successfully !!")
    return redirect('blocked_users')


#------------- Blocked Users --------------
@login_required
def blocked_users(request):
    users=Users.objects.filter(status=0,is_deleted=0).order_by('-id').all()
    user = {"users": users}
    return render(request,'blocked_users.html',user)

#------------- Reports --------------
@login_required
def add_subscriptions(request):
    if request.method == 'POST':
        name= request.POST['name']
        amount= request.POST['amount']
        number= request.POST['number']
        packages = Packages()
        packages.name = name
        packages.amount = amount
        packages.duration_in_days = number
        packages.save()
        messages.success(request,"Package add Successfully !!")
        return redirect('add_subscriptions')
    else:
        return render(request,'add_subscriptions.html')

#------------- View All Subscriptions --------------
@login_required
def view_all_subscriptions(request):
    packages = Packages.objects.filter()
    packages = {"packages": packages}
    return render(request,'view_all_subscriptions.html',packages)

#------------- Delete Subscriptions --------------
@login_required
def delete_subscription(request,pk):
    package = Packages.objects.filter(id=pk).first()
    package.delete()
    messages.success(request,'Package Deleted Successfully !!')
    return redirect('view_all_subscriptions')

#------------- Edit Subscriptions --------------
@login_required
def edit_subscription(request,pk):
    packages = Packages.objects.filter(id=pk).first()
    return render(request,'edit_subscription.html',{'packages':packages})

#------------- Edit Subscriptions --------------
@login_required
def update_subscription(request):
    if request.method == 'POST':
        name= request.POST['name']
        amount= request.POST['amount']
        number= request.POST['number']
        pkg_id = request.POST['id']
        packages = Packages.objects.filter(id=pkg_id).first()
        packages.name = name
        packages.amount = amount
        packages.duration_in_days = number
        packages.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('view_all_subscriptions')
    # else:
    #     packages = Packages.objects.filter(id=pk).first()
    #     return render(request,'edit_subscription.html',{'packages':packages})

#------------- View All Gifts --------------
@login_required
def view_all_gifts(request):
    return render(request,'view_all_gifts.html')

#------------- Privacy Policy --------------
@login_required
def privacy_policy(request):
    if request.method == "POST":
        text = request.POST['text']
        if text.strip() == "":
            form=EditorForm()
            policy = Privacy_policies.objects.filter(id=1).first()
            policy = policy.text
            soup = BeautifulSoup(policy)
            policy = soup.get_text()
            messages.error(request, 'Empty Field Not Allowd !!')
            return render(request,'privacy_policy.html',{'form':form,'policy':policy})
        else:
            privacy_policy = Privacy_policies.objects.filter(id=1).first()
            privacy_policy.text = text
            privacy_policy.save()
            form=EditorForm()
            policy = Privacy_policies.objects.filter(id=1).first()
            policy = policy.text
            soup = BeautifulSoup(policy)
            policy = soup.get_text()
            messages.success(request, 'Privacy Policy Updated Successfully !!')
            return render(request,'privacy_policy.html',{'form':form,'policy':policy})
    else:
        form=EditorForm()
        policy = Privacy_policies.objects.filter(id=1).first()
        policy = policy.text
        soup = BeautifulSoup(policy)
        policy = soup.get_text()
        return render(request,'privacy_policy.html',{'form':form,'policy':policy})

#------------- Terms & Conditions --------------
@login_required
def terms_and_conditions(request):
    if request.method == "POST":
        text = request.POST['text']
        term = Terms_and_conditions.objects.filter(id=1).first()
        if text.strip() == "":
            form=EditorForm()
            terms = Terms_and_conditions.objects.filter(id=1).first()
            terms = terms.text
            soup = BeautifulSoup(terms)
            terms = soup.get_text()
            messages.error(request, 'Empty Field Not Allowd !!')
            return render(request,'terms_and_conditions.html',{'form':form,"terms":terms})
        else:
            term.text = text
            term.save()
            form=EditorForm()
            terms = Terms_and_conditions.objects.filter(id=1).first()
            terms = terms.text
            soup = BeautifulSoup(terms)
            terms = soup.get_text()
            messages.success(request, 'Terms & Conditions Updated Successfully !!')
            return render(request,'terms_and_conditions.html',{'form':form,"terms": terms})
    else:
        form=EditorForm()
        terms = Terms_and_conditions.objects.filter(id=1).first()
        terms = terms.text
        soup = BeautifulSoup(terms)
        terms = soup.get_text()
        return render(request,'terms_and_conditions.html',{'form':form,'terms':terms})

#------------- App Links --------------
@login_required
def app_links(request):
    app_links = App_links.objects.get(id=1)
    return render(request,'app_links.html',{'app_links':app_links})

#------------- update app_android link --------------
@login_required
def update_link_android(request):
    if request.method == 'POST':
        app_links = App_links.objects.filter(id=1).first()
        app_links.android = request.POST['android_link']
        app_links.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_links')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_links')

#------------- update app_ios link --------------
@login_required
def update_link_ios(request):
    if request.method == 'POST':
        app_links = App_links.objects.filter(id=1).first()
        app_links.ios = request.POST['ios_link']
        app_links.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_links')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_links')

#------------- Reports --------------
@login_required
def complains(request):
    reports = Reports.objects.all().order_by('-id') # fetching all post objects from database
    p = Paginator(reports, 5) # creating a paginator object
	# getting the desired page number from url
    page_number = request.GET.get('page')
    try:
	    page_obj = p.get_page(page_number) # returns the desired page object
    except PageNotAnInteger:
		# if page_number is not an integer then assign the first page
	    page_obj = p.page(1)
    except EmptyPage:
		# if page is empty then return last page
	    page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
	# sending the page object to index.html
    return render(request, 'complains.html', context)

# ------------------ Reply Complain ------------------
def reply_complain(request):
    if request.method == 'POST':
        report_id = request.POST['report_id']
        reply = request.POST['reply']
        user = Users.objects.filter(id=report_id).first()
        report = Reports.objects.filter(user_id=report_id).first()
        if Users.objects.filter(id=report_id).exists():
            email = user.email
            reply_complain_mail(email,reply)
            report.status = 0
            report.response = reply
            report.save()
            messages.success(request, 'Succeeded !!')
            return redirect('complains')
        else:
            messages.error(request, 'Error !!')
            return redirect('complains')

    return render(request,'complains.html')

#------------- App Settings --------------
@login_required
def app_stg(request):
    accessories = Accessories.objects.get(id=1)
    return render(request,'app_stg.html',{'accessories':accessories})

#------------- update Free User Allowed Swipes --------------
@login_required
def update_free_user_allowed_swipes(request):
    if request.method == 'POST':
        accessories = Accessories.objects.filter(id=1).first()
        accessories.free_user_allowed_swipes = request.POST['free_user_allowed_swipes']
        accessories.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_stg')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_stg')

#------------- update Free User Swipes Time --------------
@login_required
def update_free_user_swipes_time(request):
    if request.method == 'POST':
        accessories = Accessories.objects.filter(id=1).first()
        accessories.free_user_swipes_time = request.POST['free_user_swipes_time']
        accessories.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_stg')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_stg')

#------------- update Pro User Allowed Swipes --------------
@login_required
def update_pro_user_allowed_swipes(request):
    if request.method == 'POST':
        accessories = Accessories.objects.filter(id=1).first()
        accessories.pro_user_allowed_swipes = request.POST['pro_user_allowed_swipes']
        accessories.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_stg')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_stg')

#------------- update Pro User Swipes Times --------------
@login_required
def update_pro_user_swipes_time(request):
    if request.method == 'POST':
        accessories = Accessories.objects.filter(id=1).first()
        accessories.pro_user_swipes_time = request.POST['pro_user_swipes_time']
        accessories.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_stg')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_stg')

#------------- update Free User Super Like Time --------------
@login_required
def update_free_user_super_like_time(request):
    if request.method == 'POST':
        accessories = Accessories.objects.filter(id=1).first()
        accessories.free_user_super_like_time = request.POST['free_user_super_like_time']
        accessories.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_stg')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_stg')

#------------- update Free User Allowed Super Like --------------
@login_required
def update_free_user_allowed_super_like(request):
    if request.method == 'POST':
        accessories = Accessories.objects.filter(id=1).first()
        accessories.free_user_allowed_super_like = request.POST['free_user_allowed_super_like']
        accessories.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_stg')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_stg')

#------------- update Pro User Super Like Time --------------
@login_required
def update_pro_user_super_like_time(request):
    if request.method == 'POST':
        accessories = Accessories.objects.filter(id=1).first()
        accessories.pro_user_super_like_time = request.POST['pro_user_super_like_time']
        accessories.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_stg')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_stg')

#------------- update Pro User Allowed Super Like Time --------------
@login_required
def update_pro_user_allowed_super_like(request):
    if request.method == 'POST':
        accessories = Accessories.objects.filter(id=1).first()
        accessories.pro_user_allowed_super_like = request.POST['pro_user_allowed_super_like']
        accessories.save()
        messages.success(request,"Link Update Successfully !!")
        return redirect('app_stg')
    else:
        messages.error(request,"Unable to Update Link !!")
        return redirect('app_stg')

#------------- Welcome Auto Generate Messages --------------
@login_required
def welcome(request):
    if request.method == "POST":
        text = request.POST['text']
        if text.strip() == "":
            form=EditorForm()
            welcome = Auto_msg.objects.filter(id=1).first()
            welcome = welcome.welcome
            soup = BeautifulSoup(welcome)
            welcome = soup.get_text()
            messages.error(request, 'Empty Field Not Allowd !!')
            return render(request,'welcome.html',{'form':form,'welcome': welcome})
        else:
            welcome = Auto_msg.objects.filter(id=1).first()
            welcome.welcome = text
            welcome.save()
            form=EditorForm()
            welcome = welcome.welcome
            soup = BeautifulSoup(welcome)
            welcome = soup.get_text()
            messages.success(request, 'Welcome Message Updated Successfully !!')
            return render(request,'welcome.html',{'form':form,'welcome': welcome})
    else:
        form=EditorForm()
        welcome = Auto_msg.objects.get(id=1)
        welcome = welcome.welcome
        soup = BeautifulSoup(welcome)
        welcome = soup.get_text()
        return render(request,'welcome.html',{'form':form,'welcome': welcome})
    
#------------- Matching Auto Generate Messages --------------
@login_required
def matching(request):
    # matching = Auto_msg()
    # matching.welcome = 'hello'
    # matching.matching = 'hello'
    # matching.breakup = 'hello'
    # matching.user_block = 'hello'
    # matching.admin_block = 'hello'
    # matching.admin_unblock = 'hello'
    # matching.user_delete = 'hello'
    # matching.save()
    if request.method == "POST":
        text = request.POST['text']
        if text.strip() == "":
            form=EditorForm()
            matching = Auto_msg.objects.filter(id=1).first()
            matching = matching.matching
            soup = BeautifulSoup(matching)
            matching = soup.get_text()
            messages.error(request, 'Empty Field Not Allowed !!')
            return render(request,'matching.html',{'form': form,'matching': matching})
        else:
            matching = Auto_msg.objects.filter(id=1).first()
            matching.matching = text
            matching.save()
            form=EditorForm()
            matching = matching.matching
            soup = BeautifulSoup(matching)
            matching = soup.get_text()
            messages.success(request, 'Matching Message Updated Successfully !!')
            return render(request,'matching.html',{'form': form, 'matching': matching})
    else:
        form=EditorForm()
        matching = Auto_msg.objects.get(id=1)
        matching = matching.matching
        soup = BeautifulSoup(matching)
        matching = soup.get_text()
        return render(request,'matching.html',{'form': form ,'matching': matching})

#------------- Breakup Auto Generate Messages --------------
@login_required
def breakup(request):
    if request.method == "POST":
        text = request.POST['text']
        if text.strip() == "":
            form=EditorForm()
            breakup = Auto_msg.objects.filter(id=1).first()
            breakup = breakup.breakup
            soup = BeautifulSoup(breakup)
            breakup = soup.get_text()
            messages.error(request, 'Empty Field Not Allowd !!')
            return render(request,'breakup.html',{'form': form, 'breakup': breakup})
        else:
            breakup = Auto_msg.objects.filter(id=1).first()
            breakup.breakup = text
            breakup.save()
            form=EditorForm()
            breakup = breakup.breakup
            soup = BeautifulSoup(breakup)
            breakup = soup.get_text()
            messages.success(request, 'Breakup Message Updated Successfully !!')
            return render(request,'breakup.html',{'form': form, 'breakup': breakup})
    else:
        form=EditorForm()
        breakup = Auto_msg.objects.get(id=1)
        breakup = breakup.breakup
        soup = BeautifulSoup(breakup)
        breakup = soup.get_text()
        return render(request,'breakup.html',{'form': form, 'breakup': breakup})

#------------- User Blocked A User Auto Generate Messages --------------
@login_required
def admin_user_block(request):
    if request.method == "POST":
        text = request.POST['text']
        if text.strip() == "":
            form=EditorForm()
            user_block = Auto_msg.objects.filter(id=1).first()
            user_block = user_block.user_block
            soup = BeautifulSoup(user_block)
            user_block = soup.get_text()
            messages.error(request, 'Empty Field Not Allowd !!')
            return render(request,'user_block.html',{'form':form,'user_block':user_block})
        else:
            user_block = Auto_msg.objects.filter(id=1).first()
            user_block.user_block = text
            user_block.save()
            form=EditorForm()
            user_block = user_block.user_block
            soup = BeautifulSoup(user_block)
            user_block = soup.get_text()
            messages.success(request, 'User Blocked A User Message Updated Successfully !!')
            return render(request,'user_block.html',{'form':form,'user_block':user_block})
    else:
        form=EditorForm()
        user_block = Auto_msg.objects.get(id=1)
        user_block = user_block.user_block
        soup = BeautifulSoup(user_block)
        user_block = soup.get_text()
        return render(request,'user_block.html',{'form':form,'user_block':user_block})

#------------- Admin Blocked A User Auto Generate Messages --------------
@login_required
def admin_block(request):
    if request.method == "POST":
        text = request.POST['text']
        if text.strip() == "":
            form=EditorForm()
            admin_block = Auto_msg.objects.filter(id=1).first()
            admin_block = admin_block.admin_block
            soup = BeautifulSoup(admin_block)
            admin_block = soup.get_text()
            messages.error(request, 'Empty Field Not Allowd !!')
            return render(request,'admin_block.html',{'form':form,'admin_block':admin_block})
        else:
            admin_block = Auto_msg.objects.filter(id=1).first()
            admin_block.admin_block = text
            admin_block.save()
            form=EditorForm()
            admin_block = admin_block.admin_block
            soup = BeautifulSoup(admin_block)
            admin_block = soup.get_text()
            messages.success(request, 'Admin Blocked A User Message Updated Successfully !!')
            return render(request,'admin_block.html',{'form':form,'admin_block':admin_block})
    else:
        form=EditorForm()
        admin_block = Auto_msg.objects.get(id=1)
        admin_block = admin_block.admin_block
        soup = BeautifulSoup(admin_block)
        admin_block = soup.get_text()
        return render(request,'admin_block.html',{'form':form,'admin_block':admin_block})

#------------- Admin Unblocked A User Auto Generate Messages --------------
@login_required
def admin_unblock(request):
    if request.method == "POST":
        text = request.POST['text']
        if text.strip() == "":
            form=EditorForm()
            admin_unblock = Auto_msg.objects.filter(id=1).first()
            admin_unblock = admin_unblock.admin_unblock
            soup = BeautifulSoup(admin_unblock)
            admin_unblock = soup.get_text()
            messages.error(request, 'Empty Field Not Allowd !!')
            return render(request,'admin_unblock.html',{'form':form,'admin_unblock':admin_unblock})
        else:
            admin_unblock = Auto_msg.objects.filter(id=1).first()
            admin_unblock.admin_unblock = text
            admin_unblock.save()
            form=EditorForm()
            admin_unblock = admin_unblock.admin_unblock
            soup = BeautifulSoup(admin_unblock)
            admin_unblock = soup.get_text()
            messages.success(request, 'Admin Unblocked A User Message Updated Successfully !!')
            return render(request,'admin_unblock.html',{'form':form,'admin_unblock':admin_unblock})
    else:
        form=EditorForm()
        admin_unblock = Auto_msg.objects.get(id=1)
        admin_unblock = admin_unblock.admin_unblock
        soup = BeautifulSoup(admin_unblock)
        admin_unblock = soup.get_text()
        return render(request,'admin_unblock.html',{'form':form,'admin_unblock':admin_unblock})

#------------- Admin Deleted A User Auto Generate Messages --------------
@login_required
def admin_user_delete(request):
    if request.method == "POST":
        text = request.POST['text']
        if text.strip() == "":
            form=EditorForm()
            user_delete = Auto_msg.objects.filter(id=1).first()
            user_delete = user_delete.user_delete
            soup = BeautifulSoup(user_delete)
            user_delete = soup.get_text()
            messages.error(request, 'Empty Field Not Allowd !!')
            return render(request,'user_delete.html',{'form':form,'user_delete':user_delete})
        else:
            user_delete = Auto_msg.objects.filter(id=1).first()
            user_delete.user_delete = text
            user_delete.save()
            form=EditorForm()
            user_delete = user_delete.user_delete
            soup = BeautifulSoup(user_delete)
            user_delete = soup.get_text()
            messages.success(request, 'Admin Deleted A User Message Updated Successfully !!')
            return render(request,'user_delete.html',{'form':form,'user_delete':user_delete})
    else:
        form=EditorForm()
        user_delete = Auto_msg.objects.get(id=1)
        user_delete = user_delete.user_delete
        soup = BeautifulSoup(user_delete)
        user_delete = soup.get_text()
        return render(request,'user_delete.html',{'form':form,'user_delete':user_delete})

#------------- Add FAQ's --------------
@login_required
@csrf_exempt
def add_faqs(request):
    if request.method == "POST":
        question = request.POST['question']
        anwser = request.POST['anwser']
        faqs = Faqs()
        faqs.question = question
        faqs.answer = anwser
        faqs.save()
        messages.success(request, 'FAQs Added Successfully !!')
        return redirect('add_faqs')
    else:
        return render(request,'add_faqs.html')
    
#------------- View All FAQ's --------------
@login_required
def view_all_faqs(request):
    faqs = Faqs.objects.filter()
    faqs = {"faqs": faqs}
    return render(request,'view_all_faqs.html',faqs)

#------------- Delete FAQ's --------------
@login_required
def delete_faq(request,pk):
    instance_faq = Faqs.objects.filter(id=pk).first()
    instance_faq.is_deleted = 1
    instance_faq.save()
    messages.success(request, 'FAQs Deleted Successfully !!')
    return redirect('view_all_faqs')

#------------- Notification --------------
def notification(request):
    count = Reports.objects.filter(status=1).count()
    names= Reports.objects.filter(status=1).order_by('-id')
    name = []
    for e in names:
        name.append(e.user.name)
    data = {'count':count,'name':name}
    return JsonResponse(data)
#-----------------------------------------------  User --------------------------------------------------------

# ------------------ User Confirm Email ------------------
def confirm_email_msg(request, token):
    if request.method == 'GET':
        if Users.objects.filter(token=token).exists():
            user = Users.objects.filter(token=token).first()
            user.status = 1
            user.token = ''
            user.save()
            messages.success(request, 'Verify Successfully !!')
            return render(request,'success.html')
        else:
            return render(request, 'error_404.html')
    else:
        return render(request, 'error_404.html')

# ------------------ User Change Forget Password ------------------
@csrf_exempt
def change_forget_pwd(request, token):
    if request.method == 'GET':
        user = Users.objects.filter(token=token).first()
        if user:
            return render(request, 'api/change_forget_pwd.html', {'token': token})
        else:
            return render(request, 'error_404.html')
    if request.method == 'POST':
        password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        user = Users.objects.filter(token=token).first()
        if user.id is None:
            messages.error(request, 'No user id found')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        elif password.strip() == '':
            messages.error(request, 'Password should not be empty')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        elif int(len(password)) < 6:
            messages.error(request, 'Password should not be six characters')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        elif password != confirm_password:
            messages.error(request, 'Password should be same')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            pwd = make_password(password, None, 'md5')
            user.password = pwd
            user.token = ''
            user.save()
            messages.success(request, 'Password Change Successfully !!')
            return render(request,'success.html')
    return render(request, 'change_forget_pwd.html')

# ------------------ User Change Email ------------------
def user_change_email(request, token, email):
    if request.method == 'GET':
        if Users.objects.filter(token=token).exists():
            user = Users.objects.filter(token=token).first()
            user.email = email
            user.token = ''
            user.save()
            messages.success(request, 'Email Change Successfully!!')
            return render(request, 'success.html')
        else:
            return render(request, 'error_404.html')
    else:
        return render(request, 'error_404.html')
    
    
#------------- Technical Issue Reports --------------
@login_required
def technical_issue_report(request):
    reports = Admin_reports.objects.filter(subject=1).order_by('-id') # fetching all post objects from database
    p = Paginator(reports, 10) # creating a paginator object
	# getting the desired page number from url
    page_number = request.GET.get('page')
    try:
	    page_obj = p.get_page(page_number) # returns the desired page object
    except PageNotAnInteger:
		# if page_number is not an integer then assign the first page
	    page_obj = p.page(1)
    except EmptyPage:
		# if page is empty then return last page
	    page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
	# sending the page object to index.html
    return render(request, 'technical_issue_report.html', context)

# ------------------ Reply Technical Issue Report ------------------
def reply_technical_issue_report(request):
    if request.method == 'POST':
        report_id = request.POST['report_id']
        reply = request.POST['reply']
        user = Users.objects.filter(id=report_id).first()
        report = Admin_reports.objects.filter(user_id=report_id).first()
        if Users.objects.filter(id=report_id).exists():
            email = user.email
            reply_complain_mail(email,reply)
            report.status = 0
            report.response = reply
            report.save()
            messages.success(request, 'Succeeded !!')
            return redirect('technical_issue_report')
        else:
            messages.error(request, 'Error !!')
            return redirect('technical_issue_report')
    return render(request,'technical_issue_report.html')


#------------- Billing Issue Reports --------------
@login_required
def billing_issue_report(request):
    reports = Admin_reports.objects.filter(subject=2).order_by('-id') # fetching all post objects from database
    p = Paginator(reports, 10) # creating a paginator object
	# getting the desired page number from url
    page_number = request.GET.get('page')
    try:
	    page_obj = p.get_page(page_number) # returns the desired page object
    except PageNotAnInteger:
		# if page_number is not an integer then assign the first page
	    page_obj = p.page(1)
    except EmptyPage:
		# if page is empty then return last page
	    page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
	# sending the page object to index.html
    return render(request, 'billing_issue_report.html', context)

# ------------------ Reply Billing Issue Report ------------------
def reply_billing_issue_report(request):
    if request.method == 'POST':
        report_id = request.POST['report_id']
        reply = request.POST['reply']
        user = Users.objects.filter(id=report_id).first()
        report = Admin_reports.objects.filter(user_id=report_id).first()
        if Users.objects.filter(id=report_id).exists():
            email = user.email
            reply_complain_mail(email,reply)
            report.status = 0
            report.response = reply
            report.save()
            messages.success(request, 'Succeeded !!')
            return redirect('billing_issue_report')
        else:
            messages.error(request, 'Error !!')
            return redirect('billing_issue_report')
    return render(request,'billing_issue_report.html')


#------------- Suggest An Idea --------------
@login_required
def suggest(request):
    reports = Admin_reports.objects.filter(subject=3).order_by('-id') # fetching all post objects from database
    p = Paginator(reports, 10) # creating a paginator object
	# getting the desired page number from url
    page_number = request.GET.get('page')
    try:
	    page_obj = p.get_page(page_number) # returns the desired page object
    except PageNotAnInteger:
		# if page_number is not an integer then assign the first page
	    page_obj = p.page(1)
    except EmptyPage:
		# if page is empty then return last page
	    page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
	# sending the page object to index.html
    return render(request, 'suggest.html', context)

# ------------------ Reply Suggest An Idea ------------------
def reply_suggest(request):
    if request.method == 'POST':
        report_id = request.POST['report_id']
        reply = request.POST['reply']
        user = Users.objects.filter(id=report_id).first()
        report = Admin_reports.objects.filter(user_id=report_id).first()
        if Users.objects.filter(id=report_id).exists():
            email = user.email
            reply_complain_mail(email,reply)
            report.status = 0
            report.response = reply
            report.save()
            messages.success(request, 'Succeeded !!')
            return redirect('suggest')
        else:
            messages.error(request, 'Error !!')
            return redirect('suggest')
    return render(request,'suggest.html')


#------------- Ask A Question --------------
@login_required
def ask_question(request):
    reports = Admin_reports.objects.filter(subject=4).order_by('-id') # fetching all post objects from database
    p = Paginator(reports, 10) # creating a paginator object
	# getting the desired page number from url
    page_number = request.GET.get('page')
    try:
	    page_obj = p.get_page(page_number) # returns the desired page object
    except PageNotAnInteger:
		# if page_number is not an integer then assign the first page
	    page_obj = p.page(1)
    except EmptyPage:
		# if page is empty then return last page
	    page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
	# sending the page object to index.html
    return render(request, 'ask_question.html', context)

# ------------------ Reply Ask A Question ------------------
def reply_ask_question(request):
    if request.method == 'POST':
        report_id = request.POST['report_id']
        reply = request.POST['reply']
        user = Users.objects.filter(id=report_id).first()
        report = Admin_reports.objects.filter(user_id=report_id).first()
        if Users.objects.filter(id=report_id).exists():
            email = user.email
            reply_complain_mail(email,reply)
            report.status = 0
            report.response = reply
            report.save()
            messages.success(request, 'Succeeded !!')
            return redirect('ask_question')
        else:
            messages.error(request, 'Error !!')
            return redirect('ask_question')
    return render(request,'ask_question.html')

#------------- Messages --------------
@login_required
@csrf_exempt
def message(request):
    if request.method == "POST":
        text = request.POST['text']
        if text.strip() == "":
            messages.error(request, 'Empty Field Not Allowd !!')
            return render(request,'message.html')
        else:
            message = Message(message=text,date=datetime.datetime.now().date(),time=datetime.datetime.now().time())
            message.save()
            messages.success(request, 'Message Successfully Send !!')
            return render(request,'message.html')
    else:
        return render(request,'message.html')
    
    
def terms_conditions(request):
    terms = Terms_and_conditions.objects.filter(id=1).first()
    return render(request,'terms&conditions.html',{'terms':terms})

def privacypolicy(request):
    privacy = Privacy_policies.objects.filter(id=1).first()
    return render(request,'privacy&policy.html',{'privacy':privacy})

