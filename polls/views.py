from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Poll, Choice, PollVote
from .forms import PollForm, ChoiceForm

# Список всех опросов
class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list.html'
    context_object_name = 'polls'

# Детали опроса и голосование
@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == 'POST':
        if poll.poll_type == Poll.MULTIPLE:
            choice_ids = request.POST.getlist('choices')
            if not choice_ids:
                return render(request, 'polls/poll_detail.html', {'poll': poll, 'error_message': "Выберите хотя бы один вариант."})
            PollVote.objects.filter(poll=poll, user=request.user).delete()
            for cid in choice_ids:
                choice = poll.choices.get(id=cid)
                PollVote.objects.create(poll=poll, user=request.user, choice=choice)
                choice.votes += 1
                choice.save()
        else:
            try:
                choice_id = int(request.POST['choice'])
                choice = poll.choices.get(id=choice_id)
            except (KeyError, Choice.DoesNotExist):
                return render(request, 'polls/poll_detail.html', {'poll': poll, 'error_message': "Выберите вариант ответа."})
            PollVote.objects.update_or_create(poll=poll, user=request.user, defaults={'choice': choice})
            choice.votes += 1
            choice.save()
        return redirect('poll_results', poll_id=poll.id)

    return render(request, 'polls/poll_detail.html', {'poll': poll})

# Результаты опроса
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll_results.html', {'poll': poll})

# Создание опроса (только для staff)
@staff_member_required
def create_poll(request):
    ChoiceFormSet = inlineformset_factory(Poll, Choice, form=ChoiceForm, extra=1, can_delete=True)

    if request.method == 'POST':
        form = PollForm(request.POST)
        formset = ChoiceFormSet(request.POST, prefix='choice_set')  
        if form.is_valid() and formset.is_valid():
            poll = form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            choices = formset.save(commit=False)
            for choice in choices:
                choice.poll = poll
                choice.save()
            formset.save_m2m()
            return redirect('poll_detail', poll_id=poll.id)
    else:
        form = PollForm()
        formset = ChoiceFormSet(prefix='choice_set') 

    return render(request, "polls/create_poll.html", {"form": form, "formset": formset})

# AJAX: добавить форму выбора
@staff_member_required
def add_choice_form(request):
    form_index = request.GET.get('form_index')
    if form_index is None or not form_index.isdigit():
        return JsonResponse({'error': 'Invalid form_index'}, status=400)
    form_index = int(form_index)

    ChoiceFormSet = inlineformset_factory(Poll, Choice, form=ChoiceForm, extra=1, can_delete=True)
    formset = ChoiceFormSet(prefix='choice_set')  
    empty_form = formset.empty_form
    empty_form.prefix = f'choice_set-{form_index}'  

    html = render_to_string("polls/choice_form_snippet.html", {"form": empty_form})
    return JsonResponse({"html": html})

# Редактирование опроса
@staff_member_required
def edit_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    ChoiceFormSet = inlineformset_factory(Poll, Choice, form=ChoiceForm, extra=1, can_delete=True)

    if request.method == 'POST':
        form = PollForm(request.POST, instance=poll)
        formset = ChoiceFormSet(request.POST, instance=poll)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('poll_detail', poll_id=poll.id)
    else:
        form = PollForm(instance=poll)
        formset = ChoiceFormSet(instance=poll)

    return render(request, 'polls/edit_poll.html', {'form': form, 'formset': formset})

# Редактирование выбора
@staff_member_required
def edit_choice(request, poll_id, choice_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    choice = get_object_or_404(Choice, pk=choice_id, poll=poll)

    if request.method == 'POST':
        form = ChoiceForm(request.POST, instance=choice)
        if form.is_valid():
            form.save()
            return redirect('poll_detail', poll_id=poll.id)
    else:
        form = ChoiceForm(instance=choice)

    return render(request, 'polls/edit_choice.html', {'form': form, 'poll': poll, 'choice': choice})

# Удаление опроса
@staff_member_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        poll.delete()
        return redirect('poll_list')
    return render(request, 'polls/poll_confirm_delete.html', {'poll': poll})
