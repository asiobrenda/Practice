from django.shortcuts import render
from django.http import JsonResponse
from.models import Tab
from django.shortcuts import get_object_or_404
import json

def home(request):
    varx = 'CREATING HTML ELEMENTS USING JAVASCRIPT'

    tab = Tab.objects.all()

    # if request.method == 'POST':
    #     name_ = request.POST['name']
    #     gender_ = request.POST['gender']
    #
    #     Client.objects.create(name=name_, gender=gender_)

    return render(request, 'tabs/index.html', {'varx': varx, 'tabs':tab})




def tabs(request):
    tab_name = request.POST['dic_']
    #print('type is_', type(tab_name))

    #print(type(tab_name))
    dic__ = eval(tab_name)
    #print('-----' *20)
    #print("type_of_dic_is_", type(dic__))
    name = dic__['city_name']
    color_ = dic__['color']
    title_= dic__['title']
    description_ = dic__['description']
    tab_name, t = Tab.objects.get_or_create(city_name=name, color=color_, title=title_,description=description_)
    #print(tab_name.city_name)
    #print(tab_name.id)
    dic = {
      'tab_id': tab_name.id,
        'tab_name': tab_name.city_name,
        'tab_content':tab_name.description,
        'tab_color': tab_name.color,
    }

    return JsonResponse(dic)


def get_data(request):
    content = Tab.objects.all()
    #print(content)
    dic = {}

    for c in content:
        dic[c.id] = {'city_name': c.city_name, 'tab_color': c.color,'tab_content':c.description}
        print('----'*20)
        print(dic)
    return JsonResponse(dic)

def delete_data(request):
    delete_content = request.POST['delete_tab_']
    content = Tab.objects.get(city_name=delete_content)
    tab_id = content.id
    content.delete()
    dic = {
         'tab_id_':tab_id

    }
    return JsonResponse(dic)

def save_data(request):
    content_id = request.POST['tab_id']
    #print(content_id)
    saved_content = request.POST['dic_']
    #print(11111)
    #print(saved_content)
    content = Tab.objects.get(id=content_id)
    content.description = saved_content
    content.save()

    dic = {
         'content':saved_content,
    }
    #print('----'*10)
    #print(dic)
    return JsonResponse(dic)



def save_btn(request):
    tab_id = request.POST['tab_id_']
    btn_id_ = request.POST['btn_id']
    saved_btn_ = request.POST['saved_copied_btn']
    tab_name = request.POST['tab_name_']

    # Create content dictionary
    content = {"btn_" + tab_name: saved_btn_, "btn_id_": btn_id_, "btn_code":""}

    tab = Tab.objects.get(id=tab_id)

    saved_data = tab.saved_btn if tab.saved_btn else {}

    # Ensure that the saved_data[tab_id] is a list
    if tab_id not in saved_data:
        saved_data[tab_id] = []

    # Append the content
    saved_data[tab_id].append(content)

    # Updating the appended content
    tab.saved_btn = saved_data
    tab.save()
    dic = {'tab_id':tab.id, 'tab_name': tab.city_name}
    return JsonResponse(dic)

def saved_btn(request):
    saved_btn = Tab.objects.all()

    dic = {}
    # print(dic)
    # print('--'*10)

    for s in saved_btn:
        dic[s.id] = s.saved_btn
        #print(dic[s.id])

    dic = {'saved_btn_':dic}
    #print("--"*70)
    #print(dic)
    return JsonResponse(dic)

def saved_btn_code(request):
    code__ = request.POST['code_'].strip('"')
    #print(code__)
    tab_id = request.POST['tab_id_']
    btn_id = request.POST['btn_id']

    #print(tab_id)
    #print(btn_id)

    s = Tab.objects.get(id=tab_id)
    saved_btn_data = s.saved_btn.get(tab_id, [])
    #print(saved_btn_data)
    for btn in saved_btn_data:
        if btn.get('btn_id_') == btn_id:
            btn['btn_code'] = code__

    s.saved_btn[tab_id] = saved_btn_data
    #print(s.saved_btn[tab_id])
    s.save()

    response_data = {'saved_code':s.saved_btn}  # Data to be sent in the JSON response
    print(response_data)
    return JsonResponse(response_data)

def get_saved_btn_code(request):
    get_saved_btn_code = Tab.objects.all()

    #print(get_saved_btn_code)
    dic = {}

    for c in get_saved_btn_code:
        dic[c.id] = c.saved_btn
        #print(dic[c.id])

    dic = {'saved_code': dic, 'id':c.id}

    return JsonResponse(dic)