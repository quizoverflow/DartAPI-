import pandas as pd
import json
from tool import *
from data_controller import DataController
from tqdm import tqdm
import OpenDartReader

@singleton
class ReportCrawler():

    def __init__(self):
        #api key등이 담긴 data/meta.json 파일을 불러옵니다
        meta_data = DataController().get_meta_data()
        self.api_key = meta_data["api_key"]
        
        #OpenDartReader 객체 생성
        self.dart = OpenDartReader(self.api_key)

        

