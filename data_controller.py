import os
import json
from datetime import datetime
from tool import *
import pandas as pd

@singleton
class DataController():
    def __new__(cls):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    #dict 형 반환
    @staticmethod
    def get_meta_data()->dict:
        current_dir = os.path.dirname(__file__)
        meta_path = os.path.join(current_dir,'data','meta.json')
        with open(meta_path,'r',encoding='utf-8') as f:
            meta_data = json.load(f)
        return meta_data
