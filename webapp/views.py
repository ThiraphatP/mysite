from django.shortcuts import render, redirect, get_object_or_404
from .form import RestuarantForm
from .models import Restuarant


def goToListPage(request):
    restuarants = Restuarant.objects.order_by("-id").all()
    return render(request, 'list.html', { 'isShowingInput': True, 'restuarants': restuarants,'some_flag': True})





def goToAddPage(request, form):
    return render(request, 'add.html', { 'isShowingInput': True, 'form': form, 'isShowingEdit': False })

def save(request, instance):
    if instance is None:
        form = RestuarantForm(request.POST)
    else:
        form = RestuarantForm(request.POST, instance=instance)
    if form.is_valid():
        restuarant = form.save(commit=False)
        restuarant.save()

def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            save(request, None)
            return goToListPage(request)     
        else: 
            form = RestuarantForm()
        return goToAddPage(request, form)
    else:
        return redirect('mainpage')

def mainpage(request):
    return goToListPage(request)



def listpage(request):
    return goToListPage(request)

def delete(request, pk):
    if request.user.is_authenticated:
        try:

            restuarant = Restuarant.objects.get(id=pk).delete()




        except Restuarant.DoesNotExist:
            print('not existed')
        return goToListPage(request)
    else:
        return redirect('mainpage')





def edit(request, pk):
    if request.user.is_authenticated:
        restuarant = get_object_or_404(Restuarant, pk=pk)
        if request.method == "POST":
            save(request, restuarant)
            return goToListPage(request)
        else:
            restuarantForm = RestuarantForm(instance=restuarant)
        return goToAddPage(request, restuarantForm)
    else:
        return redirect('mainpage')



