import uuid
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Profile, Movie

def home(request):
    if request.user.is_authenticated:
        return redirect('app:profile_list')
    return render(request, 'index.html')

@login_required
def getProfileList(request):
    profiles = request.user.profiles.all()

    context = {
        'profiles' : profiles,
    }
    return render(request, 'profilelist.html', context)



@login_required
def createProfile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('app:profile_list')
    else:
        form = ProfileForm
        context = {
        'form' : form,
    }
    return render(request, 'createprofile.html', context)
   

@login_required
def getMovies(request, profile_id):
    try:
        profile = Profile.objects.get(uuid = profile_id)
        movies = Movie.objects.filter(age_limit = profile.age_limit)
        if profile not in request.user.profiles.all():
            return redirect('app:profile_list')
        
        context = {
            'movies' : movies,
        }
        return render(request, 'movielist.html', context)
    except Profile.DoesNotExist:
        return redirect('app:profile_list')
  
@login_required
def getMovieDetail(request, movie_id):
    try:
        movie = Movie.objects.get(uuid=movie_id)
        context = {
            'movie' : movie,
        }
        return render(request, 'moviedetail.html', context)
    except Movie.DoesNotExist:
        return redirect('app:profile_list')

@login_required
def playMovie(request, movie_id):
    try:
        movie = Movie.objects.get(uuid=movie_id)
        movie = movie.video.values()
            
        context = {
            'movie':list(movie)
        }

        return render(request, 'playmovie.html', context)
    except Movie.DoesNotExist:
        return redirect('app:profile_list')
  