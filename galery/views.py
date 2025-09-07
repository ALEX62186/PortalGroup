from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Galerys as Galery
from .forms import GaleryForm


def is_admin_or_moderator(user):
    return user.is_superuser or user.groups.filter(name="Moderators").exists()


def galery_list(request):
    galerys = Galery.objects.filter(type__in=['image', 'video']).order_by('-created_at')
    can_edit = request.user.is_authenticated and is_admin_or_moderator(request.user)

    return render(request, 'galery/galery_list.html', {
        'galerys': galerys,
        'can_edit': can_edit,
    })


@login_required
@user_passes_test(is_admin_or_moderator)
def galery_add(request):
    if request.method == "POST":
        form = GaleryForm(request.POST, request.FILES)
        if form.is_valid():
            galery = form.save(commit=False)
            galery.created_by = request.user
            galery.save()
            return redirect('galery_list')
    else:
        form = GaleryForm()
    return render(request, 'galery/galery_form.html', {'form': form})


@login_required
@user_passes_test(is_admin_or_moderator)
def galery_edit(request, pk):
    galery = get_object_or_404(Galery, pk=pk)
    if request.method == "POST":
        form = GaleryForm(request.POST, request.FILES, instance=galery)
        if form.is_valid():
            form.save()
            return redirect('galery_list')
    else:
        form = GaleryForm(instance=galery)
    return render(request, 'galery/galery_form.html', {'form': form})


@login_required
@user_passes_test(is_admin_or_moderator)
def galery_delete(request, pk):
    galery = get_object_or_404(Galery, pk=pk)
    if request.method == "POST":
        galery.delete()
        return redirect('galery_list')
    return render(request, 'galery/galery_confirm_delete.html', {'galery': galery})