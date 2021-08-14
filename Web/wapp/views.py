from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .forms import OwnerForm,CompanyForm,Owner,Company


class Main(View):
    def get(self,request):
        return render(request,'index.html',{'companies':Company.objects.all()})
    def post(self,request):
        pass
    def patch(self,request):
        pass
    def delete(self,request):
        pass


# class CRUD(View):
#     def get(self,request):
#         return render(request,'create.html',)
#     def post(self,request):
#         pass
#     def patch(self,request):
#         pass
#     def delete(self,request):
#         pass


def owner(request):
    if request.method=='POST':
        owf = OwnerForm(request.POST)
        if owf.is_valid():
            owf.save()
            return redirect('main')
        else:
            return redirect('main')
    else:
        return render(request,'owner.html',{'form':OwnerForm()})


def company(request):
    if request.method=='POST':
        cpf = CompanyForm(request.POST)
        if cpf.is_valid():
            cpf.save()
            return redirect('main')
        else:
            return redirect('main')
    else:
        return render(request,'company.html',{'form':CompanyForm()})


def delete(request):
    id = request.GET.get('id')
    Company.objects.get(id=id).delete()
    return redirect('main')