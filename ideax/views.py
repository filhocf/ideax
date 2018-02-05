from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Idea
from .forms import IdeaForm

def idea_list(request):
    ideas = Idea.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'ideax/idea_list.html', {'ideas': ideas})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideax/idea_detail.html', {'idea': idea})

@login_required
def idea_new(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user
            idea.published_date = timezone.now()
            idea.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()

    return render(request, 'ideax/idea_edit.html', {'form': form})

@login_required
def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user
            idea.pusblished_date = timezone.now()
            idea.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideax/idea_edit.html', {'form': form})

@login_required
def idea_draft_list(request):
    ideas = Idea.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'ideax/idea_draft_list.html', {'ideas': ideas})

@login_required
def idea_publish(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.publish()
    return redirect('idea_detail', pk=pk)

@login_required
def idea_remove(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.delete()
    return redirect('idea_list')
