from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required

from .forms import AlbumForm, ReviewForm
from .models import List, Album, Review


def detail_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if 'last_viewed' not in request.session:
        request.session['last_viewed'] = []
    request.session['last_viewed'] = [album_id] + request.session['last_viewed']
    if len(request.session['last_viewed']) > 5:
        request.session['last_viewed'] = request.session['last_viewed'][:-1]
    context = {'album': album}
    return render(request, 'albuns/detail.html', context)


class AlbumListView(generic.ListView):
    model = Album
    template_name = 'albuns/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'last_viewed' in self.request.session:
            context['last_albuns'] = []
            for album_id in self.request.session['last_viewed']:
                context['last_albuns'].append(
                    get_object_or_404(Album, pk=album_id))
        return context


@login_required
@permission_required('albuns.add_album')
def create_album(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
    else:
        album_form = AlbumForm()
    context = {'album_form': album_form, }
    return render(request, 'albuns/create.html', context)


def update_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album.name = form.cleaned_data['name']
            album.release_year = form.cleaned_data['release_year']
            album.poster_url = form.cleaned_data['poster_url']
            album.save()
            return HttpResponseRedirect(
                reverse('albuns:detail', args=(album.id, )))
    else:
        form = AlbumForm(
            initial={
                'name': album.name,
                'release_year': album.release_year,
                'poster_url': album.poster_url
            })

    context = {'album': album, 'form': form}
    return render(request, 'albuns/update.html', context)


def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    if request.method == "POST":
        album.delete()
        return HttpResponseRedirect(reverse('albuns:index'))

    context = {'album': album}
    return render(request, 'albuns/delete.html', context)


def create_review(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = request.user
            review_text = form.cleaned_data['text']
            review = Review(author=review_author,
                            text=review_text,
                            album=album)
            review.save()
            return HttpResponseRedirect(
                reverse('albuns:detail', args=(album_id, )))
    else:
        form = ReviewForm()
    context = {'form': form, 'album': album}
    return render(request, 'albuns/review.html', context)


class ListListView(generic.ListView):
    model = List
    template_name = 'albuns/lists.html'
