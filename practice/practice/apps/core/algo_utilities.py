import warnings
import os
from django.conf import settings
#import matplotlib as mpl
#import matplotlib.pyplot as plt

#import numpy as np
import pandas as pd


#mpl.use('Agg')

class Algo(object):
      def __init__(self, chapter_id, target_field):
            self.CHAPTER_ID = chapter_id

            #change to this when you start to use django
            self.PROJECT_ROOT_DIR = os.path.join(settings.PRAC_DIR, "data", self.CHAPTER_ID)
            os.makedirs(self.PROJECT_ROOT_DIR, exist_ok=True)

            self.TO_DATA_PATH = os.path.join(self.PROJECT_ROOT_DIR, "datasets")
            os.makedirs(self.TO_DATA_PATH, exist_ok=True)
            #print(self.TO_DATA_PATH)

            self.TARGET_FIELD = target_field
            self.DATA = None

      def load_excel_data(self, file):
           excel_path = os.path.join( self.TO_DATA_PATH, file + ".xlsx")
           self.DATA = pd.read_excel(excel_path)
           return self.DATA

