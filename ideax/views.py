from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.views.decorators.http import require_http_methods

from .models import Idea, Phase, Criterion,Popular_Vote
from .forms import IdeaForm, PhaseForm, CriterionForm

def idea_list(request):
    ideas = Idea.objects.order_by('creation_date')
    ideas_liked = get_ideas_liked(request)
    ideas_created_by_me = get_ideas_created(request)
    return render(request, 'ideax/idea_list.html', {'ideas': ideas, 'ideas_liked' : list(ideas_liked), 'link_title': True, 'ideas_created_by_me': ideas_created_by_me,})

"""
def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideax/idea_detail.html', {'idea': idea})
"""
def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    context={'idea': idea, 'link_title': False}
    data = dict()
    data['html_form'] = render_to_string('ideax/includes/idea_detail.html', context, request=request,)
    return JsonResponse(data)

@login_required
def save_idea(request, form, template_name):
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user
            idea.creation_date = timezone.now()
            idea.phase= Phase.objects.get(name='Crescendo')
            idea.save()
            data['form_is_valid'] = True
            ideas = Idea.objects.order_by('creation_date')
            ideas_created_by_me = get_ideas_created(request)
            data['html_idea_list'] = render_to_string('ideax/idea_list_loop.html', {'ideas': ideas, 'link_title': True, 'ideas_created_by_me': ideas_created_by_me,})
        else:
            data['form_is_valid'] = False

    context = {'form' : form}
    data['html_form'] = render_to_string(template_name, context, request=request,)

    return JsonResponse(data)

@login_required
def idea_new(request):
    if request.method == "POST":
        form = IdeaForm(request.POST)
    else:
        form = IdeaForm()

    if request.is_ajax():
        return save_idea(request, form, 'ideax/includes/partial_idea_create.html')
    else:
        return redirect('idea_list')

@login_required
def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        form = IdeaForm(request.POST, instance=idea)
    else:
        form = IdeaForm(instance=idea)
    return save_idea(request, form, 'ideax/includes/partial_idea_update.html')

@login_required
def idea_draft_list(request):
    ideas = Idea.objects.filter(creation_date__isnull=True).order_by('creation_date')
    return render(request, 'ideax/idea_draft_list.html', {'ideas': ideas})

@login_required
def idea_publish(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.publish()
    return redirect('idea_detail', pk=pk)

@login_required
def idea_remove(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    data = dict()
    if request.method == 'POST':
        idea.delete()
        data['form_is_valid'] = True
        ideas = Idea.objects.order_by('creation_date')
        ideas_created_by_me = get_ideas_created(request)
        data['html_idea_list'] = render_to_string('ideax/idea_list_loop.html', {'ideas': ideas, 'link_title': True, 'ideas_created_by_me': ideas_created_by_me,})
    else:
        context = {'idea' : idea}
        data['html_form'] = render_to_string('ideax/includes/partial_idea_remove.html', context, request=request,)

    return JsonResponse(data)

@login_required
def phase_new(request):
    if request.method == "POST":
        form = PhaseForm(request.POST)
        if form.is_valid():
            phase = form.save(commit=False)
            phase.save()
            return redirect('phase_list')
    else:
        form = PhaseForm()

    return render(request, 'ideax/phase_edit.html', {'form': form})

@login_required
def phase_list(request):
    phases = Phase.objects.all()
    return render(request, 'ideax/phase_list.html', {'phases': phases})

@login_required
def phase_edit(request, pk):
    phase = get_object_or_404(Phase, pk=pk)
    if request.method == "POST":
        form = PhaseForm(request.POST, instance=phase)
        if form.is_valid():
            phase = form.save(commit=False)
            phase.save()
            return redirect('phase_list')
    else:
        form = PhaseForm(instance=phase)
    return render(request, 'ideax/phase_edit.html', {'form': form})

@login_required
def phase_remove(request, pk):
    phase = get_object_or_404(Phase, pk=pk)
    phase.delete()
    return redirect('phase_list')

@login_required
def criterion_new(request):
    if request.method == "POST":
        form = CriterionForm(request.POST)
        if form.is_valid():
            criterion = form.save(commit=False)
            criterion.save()
            return redirect('criterion_list')
    else:
        form = CriterionForm()

    return render(request, 'ideax/criterion_edit.html', {'form': form})

@login_required
def criterion_list(request):
    criterion = Criterion.objects.all()
    return render(request, 'ideax/criterion_list.html', {'criterions': criterion})

@login_required
def criterion_edit(request, pk):
    criterion = get_object_or_404(Criterion, pk=pk)
    if request.method == "POST":
        form = CriterionForm(request.POST, instance=criterion)
        if form.is_valid():
            criterion = form.save(commit=False)
            criterion.save()
            return redirect('criterion_list')
    else:
        form = CriterionForm(instance=criterion)
    return render(request, 'ideax/criterion_edit.html', {'form': form})

@login_required
def criterion_remove(request, pk):
    criterion = get_object_or_404(Criterion, pk=pk)
    criterion.delete()
    return redirect('criterion_list')

@login_required
def like_popular_vote(request, pk):
    vote = Popular_Vote.objects.filter(voter=request.user,idea__pk=pk)

    idea_ = Idea.objects.get(pk=pk)
    like_boolean =  request.path.split("/")[3] == "like"

    if vote.count() == 0:
        like = Popular_Vote(like=like_boolean,voter=request.user,voting_date=timezone.now(),idea=idea_)
        like.save()
    else:
        if vote[0].like == like_boolean:
            vote.delete()
            like_boolean = None
        else:
            vote.update(like=like_boolean)


    data = dict()
    data['qtde_votes_likes'] = idea_.count_likes()
    data['qtde_votes_dislikes'] = idea_.count_dislikes()
    data['class'] = like_boolean

    return JsonResponse(data)

def get_ideas_liked(request):
    ideas_liked = []
    if request.user.is_authenticated:
        ideas_liked = Popular_Vote.objects.filter(voter=request.user).values_list('idea_id',flat=True)

    return ideas_liked


def get_ideas_created(request):
    ideas_created = []
    if request.user.is_authenticated:
        ideas_created = Idea.objects.filter(author=request.user).values_list('id',flat=True)

    return ideas_created
