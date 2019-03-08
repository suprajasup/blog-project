from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User 
def home(request):
	all_posts=Post.objects.all()
	print(all_posts)
	return render(request,"home.html",{'all_posts':all_posts})

def greetings(request):
	return HttpResponse("How are you!!!")

def about(request,name,id1):
	if name=="admin":
		msg=f"hey!You are the boss"
	else:
		msg=f"hey{name}"

	return render(request, "about.html",{'person':name,'id1':id1})
	# return HttpResponse(msg)

def create_post(request):
	if request.method == "POST":
		form_title=request.POST['title']
		form_body=request.POST['body']
		file=request.FILES['mycover']
		if file.name.endswith(".jpg") or file.name.endswith(".jpg") or file.name.endswith(".jpg"):
			new_post=Post.objects.create(title=form_title,body=form_body,cover=file)
			return redirect(f"/post/{new_post.id}/")
		else:
			return render(request,"create.html",{'msg':'Invalid File Format'})

		
		# print(new_post.id)
		# return HttpResponse(form_title)
	return render(request,"create.html")

def post_page(request,post_id):
	print(post_id)
	post=Post.objects.get(id=post_id)
	# return HttpResponse(post)
	return render(request,"post.html",{"post":post})


def signin(request):
	if request.method=="POST":
		username=request.POST.get('username',None)
		password=request.POST.get('password',None)
		print(username,password)
		user=authenticate(request,username=username,password=password)
		print(user)
		if user is not None:
			print("Im in")
			login(request,user)
			return redirect("/home/")

	return render(request,"login.html")

def signup(request):
	if request.method=="POST":
		fullname=request.POST.get('fullname',None)
		email=request.POST.get('email',None)
		username=request.POST.get('username',None)
		password=request.POST.get('password',None)

		user_exists=User.objects.filter(username=username).exists()
		print(user_exists)
		if not user_exists:
			user=User.objects.create_user(
				username=username,
				password=password,
				email=email,
				first_name=fullname.split()[0]
			)
			login(request,user)
			return redirect("/home/")
		else:
			return HttpResponse("User already exists.Try new Username")
	return render(request,"signup.html")



def signout(request):
	logout(request)
	return redirect("/home/")







