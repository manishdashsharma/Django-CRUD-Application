from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import schoolForm
from .models import StudyMaterial
from django.utils import timezone

def index(request):
    # schoolList = StudyMaterial.objects.all().order_by('-date')
    schoolList = StudyMaterial.objects.all()
    print(f"This is school list {schoolList}")
    return render(request, 'list.html', {'list': schoolList})

def saveAction(request):
    print(request.POST)
    schoolform = schoolForm(request.POST or None)
    if schoolform.is_valid():
        schoolform.save()
        return redirect('/school')
    return render(request, 'index.html', {'form': schoolform})

def edit(request, pk):
    pickList = StudyMaterial.objects.get(pk=pk)
    editForm = schoolForm(request.POST or None, instance=pickList)
    if editForm.is_valid():
        editForm.save()
        return redirect('/school')
    return render(request, 'index.html', {'form': editForm})

def deleteAction(request, pk):
    pickList = StudyMaterial.objects.get(pk=pk)
    pickList.delete()
    return redirect('school:crud')