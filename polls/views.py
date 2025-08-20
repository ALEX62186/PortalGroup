from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Poll, Choice, PollVote
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from django.forms import inlineformset_factory


class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list.html'
    context_object_name = 'polls'


def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})


@login_required
def vote_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        choice_ids = request.POST.getlist('choices')  # список выбранных вариантов
        if not choice_ids:
            return render(request, 'polls/poll_detail.html', {
                'poll': poll,
                'error_message': "Выберите хотя бы один вариант."
            })

        for choice_id in choice_ids:
            try:
                selected_choice = poll.choices.get(id=int(choice_id))
            except Choice.DoesNotExist:
                continue

            # Сохраняем голос
            PollVote.objects.update_or_create(
                poll=poll,
                user=request.user,
                defaults={'choice': selected_choice}
            )
            selected_choice.votes += 1
            selected_choice.save()

        return redirect('poll_results', poll_id=poll.id)
    return redirect('poll_detail', poll_id=poll.id)


def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll_results.html', {'poll': poll})


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']


@staff_member_required
def create_poll(request):
    ChoiceFormSet = inlineformset_factory(
        Poll, Choice, form=ChoiceForm, extra=1, can_delete=True
    )

    if request.method == 'POST':
        form = PollForm(request.POST)
        formset = ChoiceFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            poll = form.save()
            choices = formset.save(commit=False)
            for choice in choices:
                choice.poll = poll
                choice.save()
            return redirect('poll_detail', poll_id=poll.id)
    else:
        form = PollForm()
        formset = ChoiceFormSet()

    return render(request, 'polls/create_poll.html', {'form': form, 'formset': formset})


@staff_member_required
def edit_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    ChoiceFormSet = inlineformset_factory(Poll, Choice, form=ChoiceForm, extra=0, can_delete=True)

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

    return render(request, 'polls/edit_poll.html', {'form': form, 'formset': formset, 'poll': poll})


@staff_member_required
def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        poll.delete()
        return redirect('poll_list')
    return render(request, 'polls/poll_confirm_delete.html', {'poll': poll})
