from django.shortcuts import render
from .forms import BookForm
from .models import Book
from django.http import JsonResponse


def index(request):
    data = Book.objects.all()
    form = BookForm()
    return render(request, 'index.html', {'form':form, 'data':data})

def save_data(request):
    if(request.method == 'POST'):
        form = BookForm(request.POST)
        if(form.is_valid()):
            id = request.POST.get('id')
            name = form.cleaned_data.get('name')
            author = form.cleaned_data.get('author')
            if(id != None):
                new_book = Book.objects.get(pk=id)
                print(new_book)
                new_book.name = name
                new_book.author = author
                new_book.save()
            else:
                new_book = Book.objects.create(name=name, author=author)
            new_book = list(Book.objects.values())
            return JsonResponse({'status':1, 'data':new_book})
        else:
            return JsonResponse({'status':0})

def delete_data(request):
    if(request.method == "POST"):
        id = request.POST.get('id')
        delete = Book.objects.get(pk=id).delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def edit_data(request):
    if(request.method == "POST"):
        id = request.POST.get('id')
        print(id)
        book = Book.objects.get(pk=id)
        book_data = {'id':book.id, 'name':book.name, 'author':book.author}
        return JsonResponse({'data':book_data, 'status':1})
    else:
        return JsonResponse({'status':0})