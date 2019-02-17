from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post
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

		new_post=Post.objects.create(title=form_title,body=form_body)
		return redirect(f"/post/{new_post.id}/")
		# print(new_post.id)
		# return HttpResponse(form_title)
	return render(request,"create.html")

def post_page(request,post_id):
	print(post_id)
	post=Post.objects.get(id=post_id)
	# return HttpResponse(post)
	return render(request,"post.html",{"post":post})

