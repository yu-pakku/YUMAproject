from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def test(request):
    return HttpResponse('<a href="/main_game/">test</a>')

def base(request):
    afforestation_size = 20
    context = {
        "tree_age" : 1 ,
        "afforestation_size" : range(afforestation_size),
    }
    return render(request, 'base.html', context)


# def afforestation_area(request):
#     tree_image = 'img/tree_img/tree1.png'
#     while True:
#         tree_time += 1
#         if tree_time >= 20 : # 20s経過したら
#             tree_age += 1
#             tree_image = f'img/tree_img/tree{tree_age}.png' #-> 'img/tree_img/tree.png'
#         return render(request, 'afforestation_area.html', tree_image)