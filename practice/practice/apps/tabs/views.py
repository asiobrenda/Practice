from django.shortcuts import render
from django.http import JsonResponse
from.models import Tab

def home(request):
    varx = "CREATING HTML ELEMENTS USING JAVASCRIPT"

    tabs_ = Tab.objects.all()
    return render(request, 'tabs/index.html', {'varx': varx, 'tabs':tabs_})

def get_tab_name(request):
    dic = request.POST["get_tab_name"]
    dic__ = eval(dic)
    tab_name = dic__['tab_name_']
    title_ = dic__['title']
    description_ = dic__['description']
    color_ = dic__['color']

    tab, t = Tab.objects.get_or_create(city_name=tab_name, title=title_, description=description_, color=color_)
    # print(tab_name)
    dic = {"tab_name_id": tab.id}
    return JsonResponse(dic)