from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def correct_num(request, phone_number):
    return HttpResponse("This phone number: {} is correct".format({phone_number}))


def correct_string(request, some_string):
    return HttpResponse("This string: {} is correct".format(some_string))


def first(request):
    return render(request, 'index.html')

#
# def article(request, article_id, name=''):
#     return HttpResponse(
#         "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
#             name) if name else "This is unnamed article"), 'article.html')


def article_odd(request, article_num, name=''):
    return render(request, 'chetnost.html',
    {
        'article_num': article_num,
        'slug_name': name,
    })


def users(request):
    return render("This is list of users: Dada Yaya, Anatolii Vaserman")


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')

    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True
    })


def article(request):
    return render(request, 'article.html')
#
# def first(request):
#     return render(request, 'first.html')
#


def base(request):
    return render(request, 'base.html')
