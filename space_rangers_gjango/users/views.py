from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomUserCreationForm, ProfileForm
from users.models import Follow, User


class SingUPView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('games:index')
    template_name = 'users/signup.html'


def profile(request, username):
    author = get_object_or_404(User, username=username)

    following = Follow.objects.filter(
        user__username=request.user, author=author
    )
    context = {"author": author, "following": following}
    return render(request, "profile/profile.html", context)


@login_required
def profile_edit(request, username):
    if request.method == 'POST':
        user_form = ProfileForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid():
            user_form.save()
            return redirect("users:profile", request.user.username)
    else:
        user_form = ProfileForm(instance=request.user)
        context = {"user_form": user_form}
        return render(request, 'profile/profile_edit.html', context)


@login_required
def following_list(request, username):
    author = get_object_or_404(User, username=username)
    page_obj = author.following.all()
    context = {"is_edit": True, "page_obj": page_obj, "author": author}
    return render(request, "profile/following_list.html", context)


@login_required
def follower_list(request, username):
    author = get_object_or_404(User, username=username)
    page_obj = author.follower.all()
    context = {"page_obj": page_obj, "author": author}
    return render(request, "profile/follower_list.html", context)


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    if author != request.user:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect("users:profile", username)


@login_required
def profile_unfollow(request, username):
    get_object_or_404(Follow, user=request.user,
                      author__username=username).delete()
    return redirect("users:profile", username)
