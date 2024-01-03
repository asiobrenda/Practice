from django.shortcuts import render
from .data_processing import AlgoUE
from .models import Source, Product, YearData


def home(request):
    varx = 'Welcome to Data analysis'
    source_ = Source.objects.all()
    product_ = Product.objects.all()
    years = YearData.objects.values_list('year', flat=True)
   # print(years)


    return render(request, 'asio/index.html', {'varx':varx, 'source':source_,
                                               'product':product_, 'year':years})


def load_data(request):
    varx = 'Data was loaded successfully'
    pdu = AlgoUE()
    print(pdu)
    pdu.upload_data_to_database()
    return render(request, 'asio/load_data.html', {'varx': varx})

# def get_data(request):
#     source_name = request.POST.get('source')
#     source_ = Source.objects.get(type=source_name)
#     print(source_)
#     products_ = Product.objects.all()
#     print(products_)
#     p_ = products_[0]
#     print('-------' * 30)
#     print(p_)
#     years = YearData.objects.filter(source=source_, product=p_)
#     print(years)
#
#     # year_data_ = YearData.objects.filter(source__type=source_name)
#     return render(request, 'asio/get_data.html', {
#         'products': products_,
#         'years': years,
#         'source': source_
#         # ,
#         # 'year_data': year_data_
#     })


