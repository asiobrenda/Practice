from django.shortcuts import render
from .models import Tabs
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    tabs = Tabs.objects.all()
    context = {'tabs': tabs}
    return render(request, 'analysis/index.html', context)


def add_tab(request):
    tab_name = request.POST['dic_']
    dic__ = eval(tab_name)
    name = dic__['name']
    tab_name_, t = Tabs.objects.get_or_create(tab_name=name)
    # print('type is_', type(tab_name))
    # print(type(tab_name))
    # print('-----' *20)
    # print("type_of_dic_is_", type(dic__))
    #print(tab_name_.tab_name)
    # #print(tab_name.id)
    dic = {
        'tab_id': tab_name_.id,
        'tab_name': tab_name_.tab_name
    }

    return JsonResponse(dic)

def get_data(request):
    content = Tabs.objects.all()
    dic = {}

    for c in content:
        dic[c.id] = {'tab_name': c.tab_name}
        #print('----'*20)
        #print(dic)
    return JsonResponse(dic)

def delete_tab(request):
    delete_tab = request.POST['delete_tab_']
    tab = Tabs.objects.get(tab_name=delete_tab)
    tab_id = tab.id
    tab.delete()
    dic = {
        'tab_id_': tab_id,
        'name': tab.tab_name
    }
    return JsonResponse(dic)

def add_btn(request):
    dic = request.POST['dic_']
    dic__ = eval(dic)
    btn_name_ = dic__['btn_name']
    tab_id = dic__['tab_id_']
    link_id = dic__['id']
    #print(tab_id)
    #print(btn_name_)
    #print(link_id)

    # Create content dictionary
    content = {"btn_": btn_name_, "btn_id_": link_id}
    #print(content)

    tab = Tabs.objects.get(id=tab_id)
    #print(tab)

    # Retrieve the saved_btn field, ensuring it is treated as a dictionary
    if isinstance(tab.saved_btn, str):
        saved_data = eval(tab.saved_btn) if tab.saved_btn else {}
    else:
        saved_data = tab.saved_btn if tab.saved_btn else {}

    # Ensure that the saved_data[tab_id] is a list
    if str(tab_id) not in saved_data:
        saved_data[str(tab_id)] = []

    # Append the new button content to the list
    saved_data[str(tab_id)].append(content)

    # Update the tab's saved_btn field
    tab.saved_btn = saved_data
    tab.save()

    dic = {'tab_id':tab_id, 'name':tab.tab_name, "btn_": btn_name_}
    print(dic)

    return JsonResponse(dic)

def get_add_btn(request):
    added_btn = Tabs.objects.all()
    #print(added_btn)

    dic = {}

    #print(dic)

    for b in added_btn:
        dic[b.id] = b.saved_btn

    dic = {'saved_btn_': dic}
    #print(dic)

    return JsonResponse(dic)

def delete_sub_tab_(request):
            tab_id = request.POST['tab_id']
            btn_id = int(request.POST['subTab_id'])
            btn_name = request.POST['subTab_id_name']

            tab = Tabs.objects.get(id=tab_id)


            # Get the sub-tabs for the specified tab_id
            sub_tabs = tab.saved_btn.get(tab_id, [])

            # Filter out the sub-tab with matching btn_id using list comprehension method
            updated_sub_tabs = [sub_tab for sub_tab in sub_tabs if sub_tab.get('btn_id_') != btn_id]

            # Update the saved_btn dictionary with filtered sub-tabs
            tab.saved_btn[tab_id] = updated_sub_tabs
            tab.save()

            dic = {
                'name': btn_name,
                 'btn_id_': btn_id
            }

            return JsonResponse(dic)


@csrf_exempt
def get_next_btn_id(request):
    if request.method == 'POST':
        tab_id = request.POST.get('tab_id')

        # Ensure the tab exists
        try:
            tab = Tabs.objects.get(id=tab_id)
        except Tabs.DoesNotExist:
            return JsonResponse({'error': 'Tab not found'}, status=404)

        # Initialize saved_btn if it is None
        if tab.saved_btn is None:
            tab.saved_btn = {}

        # Retrieve sub_tabs for the specific tab_id
        sub_tabs = tab.saved_btn.get(str(tab_id), [])

        # Find the highest existing button ID within the tab_id
        max_btn_id = 0
        for btn_info in sub_tabs:
            if "btn_id_" in btn_info:
                max_btn_id = max(max_btn_id, btn_info["btn_id_"])

        # Generate a new button ID as max existing ID + 1, or start from tab_id if no buttons exist
        new_btn_id = max_btn_id + 1 if max_btn_id else int(tab_id) + 1

        # Prepare the response data
        response_data = {
            'btn_id': new_btn_id
        }

        return JsonResponse(response_data)


def cloned_btn(request):
    tab_id = request.POST['tab_id_']
    save_btn = request.POST['save_btn_']
    btnLinkId = int(request.POST['btnLinkId_'])

    tab = Tabs.objects.get(id=tab_id)
    data = tab.saved_btn

    # Find the correct dictionary entry
    if str(tab_id) in data:
        entries = data[str(tab_id)]
        for entry in entries:
            if entry['btn_id_'] == btnLinkId:
                if 'cloned_buttons' not in entry:
                    entry['cloned_buttons'] = {}
                entry['cloned_buttons'][save_btn] = save_btn
                break

    # Save the updated dictionary back to the database
    tab.saved_btn = data
    tab.save()

    dic = {'saved_btn':tab.saved_btn}

    return JsonResponse(dic)


def get_cloned_btn(request):
    get_cloned_btn_code = Tabs.objects.all()

    #print(get_cloned_btn_code)
    dic = {}

    for c in get_cloned_btn_code:
        dic[c.id] = c.saved_btn
        #print(dic[c.id])

    dic = {'saved_code': dic}

    return JsonResponse(dic)

def get_cloned_data(request):
    content = Tabs.objects.all()
    dic = {}

    #print(dic)

    for c in content:
        dic[c.id] = {'saved_btn': c.saved_btn}
        #print('----'*100)
        #print(dic)
    return JsonResponse(dic)
