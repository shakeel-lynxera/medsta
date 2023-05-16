from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from users.forms import AddEducationForm, AddExperienceForm, AddAccomplishmentForm
from users.models import Accomplishment, Experience, Friend, FriendRelationsChoices, Interest, Language, Profile, Skill
from utilies.reuseable_methods import get_request_obj
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/auth/login/")
def dashboard(request):
    posts = request.user.posts.all()
    print('posts', posts)
    context = {"experiences" : request.user.experiences.all(),
               "posts" : posts,}
    return render(request, "clients/dashboard/dashboard.html", context=context)


def profile(request):
    if not request.user.is_authenticated:
        return redirect("/auth/login/")
    context = {"experiences" : request.user.experiences.all(),
               "educations" : request.user.educations.all(),
               "skills": request.user.skills.all(),
               "accomplishments": request.user.accomplishments.all(),
               "interests": request.user.interests.all(),
               "languages": request.user.languages.all(),
               "age" : request.user.profile.get_age()}
    return render(request, "clients/dashboard/profile.html", context=context)


def cv(request):
    if not request.user.is_authenticated:
        return redirect("/auth/login/")
    context = {"experiences" : request.user.experiences.all(),
               "educations" : request.user.educations.all(),
               "skills": request.user.skills.all(),
               "accomplishments": request.user.accomplishments.all(),
               "interests": request.user.interests.all(),
               "languages": request.user.languages.all(),
               "age" : request.user.profile.get_age()}
    return render(request, "clients/cv/cv.html", context=context)


def network(request):
    # exclude_list = User.objects.all().values_list("friends", flat=True)
    # users = User.objects.all().exclude(id__in=exclude_list)
    users = User.objects.all()
    # Friend.objects.all().delete()
    
    # Invited friends
    invites = request.user.friends.filter(status=1)
    # Requested friends
    requests = request.user.friend_of.filter(status=1)
    # Friends
    friend_connections = request.user.friends.filter(status=2)
    
    context = {"users" : users,
               "invites" : invites,
               "user_requests": requests,
               "friend_connections": friend_connections}
    return render(request, "clients/network/social-network.html", context=context)


def update_profile_basic_information(request):
    if not request.user.is_authenticated:
        return redirect("/auth/login/")
    if request.method == "POST":
        full_name = request.POST.get("full_name") or None
        phone_number = request.POST.get("phone_number") or None
        country = request.POST.get("country") or None
        state = request.POST.get("state") or None
        dob = request.POST.get("dob") or None
        print(full_name, phone_number, country, state, dob)
        Profile.objects.filter(user=request.user).update(full_name=full_name,
                                                         phone_number=phone_number,
                                                         country=country,
                                                         state=state,
                                                         dob=dob)
        return redirect("/profile/")
    return HttpResponseServerError("Method not allowed")


@csrf_exempt
@login_required(login_url="/auth/login/")
def update_profile_title(request):
    if request.method == "PUT":
        try:
            data = get_request_obj(request)
            title = data.get("title")
            request.user.profile.title = title
            request.user.profile.save()
            return HttpResponse("Success")
        except Exception as e:
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return HttpResponseForbidden("Method Not Allowed.")


@csrf_exempt
@login_required(login_url="/auth/login/")
def update_profile_about(request):
    if request.method == "PUT":
        try:
            data = get_request_obj(request)
            about = data.get("about")
            request.user.profile.about = about
            request.user.profile.save()
            return HttpResponse("User profile about updated")
        except Exception as e:
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return HttpResponseForbidden("Method Not Allowed.")


@login_required(login_url="/auth/login/")
def add_education(request):
    if request.method == "POST":
        try:
            form = AddEducationForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.instance.user = request.user
                form.instance.save()
                return redirect("/profile/")
            return render(request, "clients/dashboard/profile.html", context={"error": form.errors.as_text()})
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return HttpResponseForbidden("Method Not Allowed.")

@login_required(login_url="/auth/login/")
def add_experience(request):
    if request.method == "GET":
        return redirect("/profile/")

    if request.method == "POST":
        try:
            form = AddExperienceForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect("/profile/")
            return render(request, "clients/dashboard/profile.html", context={"error": form.errors.as_text()})
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")


@csrf_exempt
@login_required(login_url="/auth/login/")
def update_experience(request):
    if request.method == "PUT":
        try:
            data = get_request_obj(request)
            id = data["id"]
            title = data["title"]
            company = data["company"]
            try:
                start_date = data["start_date"]
                end_date = data["end_date"]
                if end_date == "" or end_date == None:
                    end_date = None
                    
            except:
                start_date = None
            location = data["location"]
            description = data["description"]
            Experience.objects.filter(id=id).update(title=title,
                                                    company=company,
                                                    location=location,
                                                    start_date = start_date,
                                                    end_date = end_date,
                                                    description=description)
            return HttpResponse("Experience updated")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return redirect("/profile/")


@csrf_exempt
@login_required(login_url="/auth/login/")
def delete_experience(request, id):
    if request.method == "DELETE":
        try:
            Experience.objects.filter(id=id).delete()
            return HttpResponse("Experience deleted")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return redirect("/profile/")


@csrf_exempt
@login_required(login_url="/auth/login/")
def add_skills(request):
    if request.method == "POST":
        skills = request.POST.getlist('skills')
        skills_rating = request.POST.getlist('skill-rating')
        try:
            for item in range(len(skills)):
                skill = skills[item].strip().lower()
                rating = int(skills_rating[item])*10
                if skill is not None or not skill == "":
                    Skill.objects.update_or_create(user=request.user, skill=skill, rating=rating)
            return redirect("/profile/")
        except Exception as e:
            print(e)
            return render(request, "clients/dashboard/profile.html", context={"error": "Something went wrong, try agian later."})
    else:
        return HttpResponseForbidden("Method Not Allowed.")


@csrf_exempt
@login_required(login_url="/auth/login/")
def delete_skill(request, id):
    if request.method == "DELETE":
        try:
            Skill.objects.filter(id=id).delete()
            return HttpResponse("Skill deleted")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return redirect("/profile/")


@login_required(login_url="/auth/login/")
def add_accomplishment(request):
    if request.method == "GET":
        return redirect("/profile/")

    if request.method == "POST":
        try:
            form = AddAccomplishmentForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect("/profile/")
            return render(request, "clients/dashboard/profile.html", context={"error": form.errors.as_text()})
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")


@csrf_exempt
@login_required(login_url="/auth/login/")
def update_accomplishment(request):
    if request.method == "PUT":
        try:
            data = get_request_obj(request)
            id = data["id"]
            title = data["title"]
            start_date = data["start_date"]
            end_date = data["end_date"]
            description = data["description"]
            visit_url = data["visit_url"]
            Accomplishment.objects.filter(id=id).update(title=title,
                                                        start_date=start_date,
                                                        end_date=end_date,
                                                        description=description,
                                                        visit_url=visit_url)
            return HttpResponse("Accomplishment updated")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return redirect("/profile/")


@csrf_exempt
@login_required(login_url="/auth/login/")
def delete_accomplishment(request, id):
    if request.method == "DELETE":
        try:
            Accomplishment.objects.filter(id=id).delete()
            return HttpResponse("Accomplishment deleted")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return redirect("/profile/")


@csrf_exempt
@login_required(login_url="/auth/login/")
def add_interests(request):
    if request.method == "POST":
        interests = request.POST.getlist('interests')
        try:
            for interest in interests:
                interest = interest.strip().lower()
                if interest is not None or not interest == "":
                    Interest.objects.update_or_create(user=request.user, interest=interest)
            return redirect("/profile/")
        except Exception as e:
            print(e)
            return render(request, "clients/dashboard/profile.html", context={"error": "Something went wrong, try agian later."})
    else:
        return HttpResponseForbidden("Method Not Allowed.")


@csrf_exempt
@login_required(login_url="/auth/login/")
def delete_interest(request, id):
    if request.method == "DELETE":
        try:
            Interest.objects.filter(id=id).delete()
            return HttpResponse("Interest deleted")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return redirect("/profile/")


@csrf_exempt
@login_required(login_url="/auth/login/")
def add_languages(request):
    if request.method == "POST":
        languages = request.POST.getlist('languages')
        try:
            for language in languages:
                language = language.strip().lower()
                if language is not None or not language == "":
                    Language.objects.update_or_create(user=request.user, language=language)
            return redirect("/profile/")
        except Exception as e:
            print(e)
            return render(request, "clients/dashboard/profile.html", context={"error": "Something went wrong, try agian later."})
    else:
        return HttpResponseForbidden("Method Not Allowed.")


@csrf_exempt
@login_required(login_url="/auth/login/")
def delete_language(request, id):
    if request.method == "DELETE":
        try:
            Language.objects.filter(id=id).delete()
            return HttpResponse("Language deleted")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return redirect("/profile/")


#Network APIs
@csrf_exempt
@login_required(login_url="/auth/login/")
def send_connect_request(request, reciever_id):
    if request.method == "POST":
        try:
            if User.objects.filter(id=reciever_id).exists():
                user = User.objects.get(id=reciever_id)
                Friend.objects.update_or_create(sender=request.user, reciever=user)
                return HttpResponse("Request sent")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return redirect("/cv/")


@csrf_exempt
@login_required(login_url="/auth/login/")
def cancel_connect_request(request, id):
    if request.method == "DELETE":
        try:
            Friend.objects.filter(id=id).delete()
            return HttpResponse("Request cancelled")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")
    else:
        return redirect("/cv/")


@csrf_exempt
@login_required(login_url="/auth/login/")
def accept_friend_request(request, id):
    if request.method == "POST":
        try:
            if Friend.objects.filter(id=id).exists():
                Friend.objects.filter(id=id).update(status=FriendRelationsChoices.FRIEND)
                return HttpResponse("Request accepted")
            else:
                return HttpResponseNotFound("Request not found")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")


@csrf_exempt
@login_required(login_url="/auth/login/")
def reject_friend_request(request, id):
    if request.method == "DELETE":
        try:
            if Friend.objects.filter(id=id).exists():
                Friend.objects.filter(id=id).delete()
                return HttpResponse("Request rejected")
            else:
                return HttpResponseNotFound("Request not found")
        except Exception as e:
            print(e)
            return HttpResponseServerError("Something went wrong, try agian later.")