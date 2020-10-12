from django.shortcuts import render, reverse, HttpResponseRedirect
from reviews.models import Reviews
from reviews.forms import PostForm

def index(request):
    all_posts = Reviews.objects.filter().order_by('-id')
    return render(request, 'index.html', {'title': 'Review Post', 'all_posts': all_posts})


def like_view(request):
    likes = Reviews.objects.filter(like_type=True).order_by('-id')
    return render(request, 'likes.html', {'b_title': 'Likes', 'likes': likes})


def dislike_view(request):
    dislikes = Reviews.objects.filter(like_type=False).order_by('-id')
    return render(request, 'dislikes.html', {'r_title': 'Dislikes', 'dislikes': dislikes})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Reviews.objects.create(review = data.get('review'), like_type = data.get('like_type'))
            return HttpResponseRedirect(reverse('homepage'))

    form = PostForm()
    return render(request, 'reviewsubmission.html', {'form': form, 'a_title': 'review'})


def upvote(request, post_id):
    post = Reviews.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote(request, post_id):
    post = Reviews.objects.get(id=post_id)
    post.down_vote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def votes_view(request):
    votes = sorted(Reviews.objects.all(), key=lambda votes: votes.num_votes)[::-1]
    return render(request, 'sorted.html', {'votes': votes, 'v_title': 'Sorted by Likes'})