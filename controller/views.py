from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Member, Dog, Address, Race
from .forms import MemberForm, MemberModelForm

def index(request):
    return render(request, "controller/alsobase.html")

# Create your views here.

def landing(request):
    if(request.POST):
        post_mg = request.POST
        print(post_mg["username"])
    else:
        print("landing")
    return render(request, "landing.html")

def list_members(request):
    print("here")
    members = Member.objects.all()
    context = {
        "members": members
    }
    return render(request,"controller/member/member_list.html",context )

def create_member(request):
    form = MemberModelForm()
    if request.method == "POST":
        print("receiving a new POST: new member..")
        form = MemberModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/controller/member/list")
    context = {
        "form": form
    }
    return render(request, "controller/member/member_form.html",context)

def update_member(request, pk):
    member = Member.objects.get(id=pk)
    addresses = Address.objects.all()
    form = MemberModelForm(instance=member)
    if request.method == "POST":
        print("here")
        form = MemberModelForm(request.POST, instance=member)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect("/controller/member/list")
    context = {
        "form":form,
        "member":member,
        "addresses": addresses
    }
    return render(request, "controller/member/member_update.html",context)

def member_detail(request,pk):
    member = Member.objects.get(id=pk)
    context = {
        "member":member
    }
    print(member)
    return render(request, "controller/member/member_detail.html", context)

def delete_member(request, pk):
    member = Member.objects.get(id=pk)
    member.delete()
    return redirect("/controller/member/list")