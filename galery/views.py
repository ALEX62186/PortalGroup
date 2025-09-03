from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Materials as Material
from .forms import MaterialForm


def is_admin_or_moderator(user):
    return user.is_superuser or user.groups.filter(name="Moderators").exists()


def materials_list(request):
    materials = Material.objects.filter(type__in=['image', 'video']).order_by('-created_at')
    can_edit = request.user.is_authenticated and is_admin_or_moderator(request.user)

    return render(request, 'galery/materials_list.html', {
        'materials': materials,
        'can_edit': can_edit,
    })


@login_required
@user_passes_test(is_admin_or_moderator)
def material_add(request):
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.created_by = request.user
            material.save()
            return redirect('materials_list')
    else:
        form = MaterialForm()
    return render(request, 'galery/material_form.html', {'form': form})


@login_required
@user_passes_test(is_admin_or_moderator)
def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('materials_list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'galery/material_form.html', {'form': form})


@login_required
@user_passes_test(is_admin_or_moderator)
def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        material.delete()
        return redirect('materials_list')
    return render(request, 'galery/material_confirm_delete.html', {'material': material})