import requests
import pandas as pd
import json
from tool import *
from data_controller import DataController

@singleton
class ReportCrawler():
    def __new__(cls):
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        meta_data = DataController().get_meta_data()
        self.api_key = meta_data["api_key"]
    


class test():

    def __init__(self,url,params):
        self.url = url
        self.params =params

    def get_data(self):
        return requests.get(self.url,params=self.params)


test_url = "https://opendart.fss.or.kr/api/fnlttSinglAcnt.json"
samsung = test(test_url,params={
    'crtfc_key':"f2705b18ae2074695ae017f4daf9ca085455da31",
    'corp_code':'00126380',
    'bsns_year':'2023',
    'reprt_code':'11012'
})

data = samsung.get_data().json()
df_samsung = pd.DataFrame(data['list'])

print(df_samsung)