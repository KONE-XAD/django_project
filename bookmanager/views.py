from django.shortcuts import render, HttpResponse, redirect
from bookmanager import models


# Create your views here.

def publisher_lists(request):
    all_publishers = models.Publisher.objects.all()
    # for i in l:
    #     print(i.id,i.name)

    # return HttpResponse('hhhh')
    return render(request, 'publisher_lists.html', {'all_publishers': all_publishers})


def publisher_add(request):
    if request.method == 'POST' and request.POST.get('pub_name') != '':
        pub_name = request.POST.get('pub_name')
        if models.Publisher.objects.filter(name=pub_name):
            return render(request, 'publisher_add.html', {'error': "出版社已存在"})
        else:
            ret = models.Publisher.objects.create(name=pub_name)
            print(ret, type(ret))
            return redirect('/publisher_lists/')

    return render(request, 'publisher_add.html')


def publisher_del(request):
    pub_id = request.GET.get('id')
    ret = models.Publisher.objects.filter(id=pub_id)
    if ret:
        ret.delete()
    return redirect('/publisher_lists/')


def publisher_change(request):
    pub_id = request.GET.get('id')
    ret = models.Publisher.objects.get(id=pub_id)
    pub_name = ret.name
    if request.method == 'POST':
        ret.name = request.POST.get('pub_name')
        ret.save()
        return redirect('/publisher_lists/')
    return render(request, 'publisher_change.html', {"pub_name": pub_name})


def bookinfo_lists(request):
    if request.method == "GET":
        all_bookinfo = models.Bookinfo.objects.all()
        for i in all_bookinfo:
            print(i.book_name)
            print(i.publister_id)
            print(i.publister_id.name)
        return render(request, 'bookinfo_lists.html', {'all_bookinfo': all_bookinfo})


def bookinfo_add(request):
    all_publishers = models.Publisher.objects.all()
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        if models.Bookinfo.objects.filter(book_name=book_name):
            return render(request, 'bookinfo_add.html', {'all_publishers': all_publishers, 'error': "书籍已存在"})
        else:
            ret = models.Bookinfo.objects.create(book_name=book_name, publister_id_id=pub_id)
            return redirect('/bookinfo_lists/')
    return render(request, 'bookinfo_add.html', {'all_publishers': all_publishers})


def bookinfo_del(request):
    book_id = request.GET.get('book_id')
    ret = models.Bookinfo.objects.filter(id=book_id)
    if ret:
        ret.delete()
        return redirect('/bookinfo_lists/')


def bookinfo_change(request):
    book_id = request.GET.get('book_id')
    book_obj = models.Bookinfo.objects.get(id=book_id)
    print(type(book_obj.publister_id))
    if request.method == "POST":
        book_obj.book_name = request.POST.get('book_name')
        book_obj.publister_id_id = request.POST.get('pub_id')
        book_obj.save()
        return redirect('/bookinfo_lists/')
    all_publishers = models.Publisher.objects.all()
    return render(request, 'bookinfo_change.html', {'all_publishers': all_publishers, 'book_obj': book_obj})


def author_lists(request):
    if request.method == "GET":
        all_authors = models.Author.objects.all()
        for i in all_authors:
            print("*" * 50)
            print(i.author_name, i.books.all())
            for j in i.books.all():
                print(j.book_name, j.publister_id.name)
        return render(request, 'author_lists.html', {'all_author': all_authors})


def author_add(request):
    if request.method == "POST":
        author_name = request.POST.get("author_name")
        books_ids = request.POST.getlist("book_ids")
        print(author_name, books_ids)
        author_obj = models.Author.objects.create(author_name=author_name)
        # 读者绑定书籍（多对多关系绑定）
        author_obj.books.set(books_ids)
        author_obj.save()
        return redirect("/author_lists/")
    all_books = models.Bookinfo.objects.all()
    return render(request, "author_add.html", {"all_books": all_books})


def author_del(request):
    if request.method == "GET":
        author_id = request.GET.get("author_id")
        author_obj = models.Author.objects.get(id=author_id)
        author_obj.delete()
        return redirect('/author_lists/')


def author_change(request):
    author_id = request.GET.get('author_id')
    author_obj = models.Author.objects.get(id=author_id)
    if request.method == "POST":
        author_name = request.POST.get("author_name")
        book_ids = request.POST.getlist("book_ids")
        author_obj.author_name = author_name
        author_obj.books.set(book_ids)
        author_obj.save()
        return redirect("/author_lists/")
    all_books = models.Bookinfo.objects.all()
    return render(request, "author_change.html", {"author_obj": author_obj, "all_books": all_books})


def template_test(request):
    name = '谢安东'
    location = '中国'
    age = 14
    my_list = ['xieandong', 'xad', 'xiead', 'adxie']
    my_tuple = ('xieandong', 'xad', 'xiead', 'adxie')
    my_set = {'xieandong', 'xad', 'xiead', 'adxie'}
    my_dict = {
        'name': 'xad',
        'age': 23,
        'work': 'developer',
    }

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def say_hi(self):
            return '哈撒给'  ###

    return render(request, 'template_test.html',
                  {
                      'name': name,
                      'location': location,
                      'my_list': my_list,
                      'my_tuple': my_tuple,
                      'my_set': my_set,
                      'my_dict': my_dict,
                      'person': Person(name, age),
                  }
                  )
