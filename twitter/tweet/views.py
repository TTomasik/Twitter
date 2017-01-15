from django.shortcuts import render
from django.views import View
from tweet.forms import Login
from tweet.models import Tweet
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    cont = {}
    return render(request, 'base.html', cont)

class LoginView(View):
    def get(self, request):
        form = Login()
        return render(request, "login.html", {"form": form})


    def post(self, request):
        next = request.GET.get('next')
        u = request.POST['login']
        p = request.POST['password']

        user = authenticate(username=u,
                        password=p)
        if user is not None:
            login(request, user)
            if next:
                return redirect(next)
        else:
            return HttpResponse("Nie prawidłowy login lub hasło!")

class TweetView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'welcome.html', {'tweets': tweets})

# class TweetView(View):
#     def get(self, request):
#         cont = {}
#         tweetsObj = Tweet.objects.all()
#         TWEETS = []
#
#         for m in tweetsObj:
#             d = {}
#             d['id'] = m.id
#             d['content'] = m.content
#             d['user'] = m.user
#             d['creation_date'] = m.creation_date
#             d['avatar'] = m.user.userextend.avatar
#             TWEETS.append(d)
#
#         cont['tweets'] = TWEETS
#
#         return render(request, 'welcome.html', cont)


class AddTweet(PermissionRequiredMixin, CreateView):
    permission_required = 'tweet.add_tweet'
    model = Tweet
    fields = ['content']
    success_url = '/welcome'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddTweet, self).form_valid(form)

class MyInfo(View):
    def get(self, request, person_id):
        cont = {}
        person = User.objects.get(id=person_id)
        cont['person'] = person
        cont['image'] = User.objects.get(id=person_id).userextend.avatar
        tweetsALL = Tweet.objects.filter(user__in=[person])
        INFO = []
        for t in tweetsALL:

            a = {}
            a['date'] = t.creation_date.date()
            a['content'] = t.content[:32] + '...'

            INFO.append(a)
        cont['tweets'] = INFO
        return render(request, 'my_info.html', cont)

class ContentAll(View):
    def get(self, request):
        pass

# class MovieDetails(View):
#
#     def get(self, request, movie_id):
#
#         cont = {}
#         movie = Movie.objects.get(id=movie_id)
#         cont['movie'] = movie
#
#         actorsOBJ = Movie.objects.get(id=movie_id).starring.all()
#
#         ACTORS = []
#
#         for c in actorsOBJ:
#             # person = Movie.objects.get(id=movie_id).starring.all()
#             a = {}
#             a['first_name'] = c.first_name
#             a['last_name'] = c.last_name
#             a['role'] = Role.objects.filter(person__in=[c])[0].role
#
#             ACTORS.append(a)
#
#         cont['actors'] = ACTORS
#
#
#         return render(request, 'movie_details.html', cont)






