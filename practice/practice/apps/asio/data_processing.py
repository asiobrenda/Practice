from ..core.algo_utilities import Algo
from .models import (Source, Product, YearData)
import pandas as pd
class AlgoUE(Algo):
    def __init__(self):
        super().__init__(chapter_id='ueconomics', target_field=None)

    def upload_data_to_database(self):
        df_imports = self.load_excel_data('imports')
        df_exports = self.load_excel_data('exports')

        source_exports, created = Source.objects.get_or_create(type='exports')
        if (created):
            for index, row in df_exports.iterrows():
                description_ = row['Description']
                sitc2_ = row['SITC2']
                product, created = Product.objects.get_or_create(sitc2=sitc2_, description=description_)
                for ny in range(2015, 2020):
                    y = 'Y' + str(ny)
                    v = row[y]
                    yd, created = YearData.objects.get_or_create(source=source_exports, product=product, year=ny, value=v)

        source_imports, created = Source.objects.get_or_create(type='imports')
        if created:
            for index, row in df_imports.iterrows():
                description_ = row['Description']
                sitc2_ = row['SITC2']
                product, created = Product.objects.get_or_create(sitc2=sitc2_, description=description_)
                for ny in range(2015, 2020):
                    y = 'Y' + str(ny)
                    v = row[y]
                    yd, created = YearData.objects.get_or_create(source=source_imports, product=product, year=ny, value=v)


def get_data(self):
    qs = YearData.objects.all()
    q = qs.values('source', 'product', 'year', 'value')
    print(q)
    pd_ = pd.DataFrame.from_records(q)


    print(pd_)
    source = Source.objects.all()
    product = Product.objects.all()
    return pd_, product, source

