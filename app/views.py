import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from app.models import Movie,Movie_list
from django.db.models import Q, Sum


# Create your views here.

@login_required(login_url='login')
def index(request):
    movies=Movie.objects.filter(coming_soon=1).order_by('-releasedate')
    mov=Movie.objects.all().order_by('views')
    featured_movies=mov[len(mov)-1]
    popular=Movie.objects.filter(coming_soon=1).order_by('-views')[:10]
    coming=Movie.objects.filter(coming_soon=0)
    context = {
        'movies':movies,
        'featured_movies':featured_movies,
        'popular':popular,
        'coming':coming
    }
    return render(request,'index.html',context)

@login_required(login_url='login')
def movie(request,pk):
    mid=pk
    movie_details=Movie.objects.get(u_id=mid)

    context={
        'movie_details':movie_details
    }
    return render(request,'movie.html',context)

@login_required(login_url='login')
def mylist(request):

    movie_list=Movie_list.objects.filter(owner_user=request.user)
    user_list=[]

    for movie in movie_list:
        user_list.append(movie.movie)

    if not user_list:
        msg='Empty list'
        context={
            'movies':user_list,
            'msg':msg
        }
        return render(request,'mylist.html',context)
    else:
        msg='Favorite List'
        context={
            'movies':user_list,
            'msg':msg
        }
        return render(request,'mylist.html',context)


@login_required(login_url='login')
def addlist(request):
    if request.method=='POST':
        movie_url_id=request.POST.get('movie_id')
        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        match = re.search(uuid_pattern, movie_url_id)
        movie_id = match.group() if match else None

        movie=get_object_or_404(Movie,u_id=movie_id)
        movie_list,created=Movie_list.objects.get_or_create(owner_user=request.user,movie=movie,m_id=movie_id)

        if created:
            response_data={'status':'success','message':'Added'}
        else:
            response_data={'status':'info','message':'already added'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'status':'error','message':'invalid request'},status=400)
    

@login_required(login_url='login')
def remove(request):
    movie_url_id=request.POST.get('movieid')
    uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
    match = re.search(uuid_pattern, movie_url_id)
    movie_id = match.group() if match else None

    movie=Movie_list.objects.filter(m_id=movie_id)

    movie.delete()
    return redirect(request,'mylist')



@login_required(login_url='login')
def genere(request,pk):
    gen=pk
    movies=Movie.objects.filter(genre=gen,coming_soon=1)
    if not movies:
        movie_genre='No result found'
        context={
        'movie_genre':movie_genre,
    }
        return render(request,'genere.html',context)
    else:
        msg='Films'
        context={
        'movies':movies,
        'movie_genre':gen,
        'msg':msg
    }
        return render(request,'genere.html',context)

    
@login_required(login_url='login')
def search(request):
        query = request.GET.get('query')
        movies = Movie.objects.filter(Q(title__contains=query) | Q(description__contains=query) | Q(tags__contains=query))
        if not movies:
            msg='No results found'
            context = {
                'movies': movies,
                'msg':msg
            }
            return render(request,'search.html',context)
        else:
            msg='Search Results'
            context = {
                'movies': movies,
                'msg':msg
            }
            return render(request,'search.html',context)




def login(request):
    if request.method=='POST':
        username=request.POST ['username']
        password=request.POST ['password']

        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        email=request.POST ['email']
        username=request.POST ['username']
        password=request.POST ['password']
        password2=request.POST ['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email alredy taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
            
                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')
    

def logout(request):
    auth.logout(request)
    return redirect('login')

def change(request):
    return render(request,'passwordchange.html')

def profile(request):
    return render(request,'profile.html')