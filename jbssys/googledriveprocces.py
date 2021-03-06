import datetime
import os
import json
import re
import time

import pandas as pd
from pprint import pprint

import requests
import bs4
from requests.auth import HTTPBasicAuth
from pyxlsb import convert_date



def validate_date(date_text):
    try:
        dtime = str(datetime.datetime.strptime(
            date_text, '%Y-%m-%d')
        ).split(" ")[0]

    except :
        try:
            dtime = datetime.datetime.strptime(date_text, "%d/%m/%Y").strftime("%Y-%m-%d")
        except:
            dtime = ""

    return dtime


class GoogleDrive:
    def __init__(self,url="",format=""):
        self.url = url
        self.format = format
        self.request_count = 0
        self.dir_path = os.path.dirname(os.path.realpath(__file__))



    def request(self):
        headers = {"user-agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}
        self.resp = requests.get(self.url,headers=headers, auth=HTTPBasicAuth('honcharykandrey0@gmail.com',"googleaccountidtorrent641"))



    def gog_drive_to_json(self):
        self.request_count += 1
        soup = bs4.BeautifulSoup(self.resp.text, 'html.parser')

        script_s = soup.find_all('script')
        json_ = None
        for script_ in script_s:
            if "DOCS_cseBlobCreationArtifactsHolder" in str(script_):
                json_ = str(script_).split("bootstrapData = ")[1].split(";")[0]
        if json_:
            self.json_data = json.loads(json_)


        else:
            print("Not connect to file: ", self.request_count)

            if self.request_count >= 3:
                self.json_data = None
            else:
                time.sleep(5)
                self.request()
                self.gog_drive_to_json()


    def wtite_to_json(self,outputfile=""):

        if outputfile:
            outputfile = outputfile
        else:
            outputfile = "data_output.json"
        if self.json_data:
            with open(self.dir_path + '/' + str(outputfile), 'w') as file_:
                json.dump(self.json_data, file_)
        else:
            print("Json not found")

    def data_from_jjson(self):
        self.table_ = self.json_data['changes']['firstchunk']
        for data in self.table_:
            if 25813757 in data:

                table_data = json.loads(data[1])
        self.table_size = (table_data[0][4],table_data[0][2])


        try:
            self.table_data_list = table_data[2]
            self.table_gd_list_to_list()
        except:
            self.get_table_max100()

    def table_gd_list_to_list(self):
        data_list = []
        self.table_data = [["" for i in range(self.table_size[0])] for ii in range(self.table_size[1])]

        for list_data in self.table_data_list:
            data = list_data[2][0]

            indexes = [list_data[0],list_data[1]]
            if "3" in data.keys():
                data_ = data["3"][0]


                if type(data_ ) == int and data_== 2:
                    val_ = data["3"][1]
                    data_list.append(val_)

                    try:
                        val_ = float(val_)

                    except:
                        val_ = val_


                elif type(data_ ) == dict and "3" in data_.keys():
                    if len(str(data_["3"])) > 7:

                        val_ = float(data_["3"])
                        val_ = format(convert_date(val_), '%Y-%m-%d %H:%M:%S')

                        data_list.append(str(val_))

                    elif len(str(data_["3"])) > 5:
                        val_ = float(data_["3"])
                        val_ = format(convert_date(val_), '%Y-%m-%d')
                        data_list.append(str(val_))

                    else:
                        val_ = str(int(data_["3"]))

                        data_list.append(val_)


            elif "25" in data.keys():

                val_ = data_list[data["25"]]
                data_list.append(val_)

            elif "7" in data.keys():
                val_ = data["7"][1]
                data_list.append(val_)

            self.table_data[indexes[0]][indexes[1]] = val_

        self.table_data = self.table_data[1:]

    def read_from_json(self,inputfile):
        with open(self.dir_path + '/' + str(inputfile), 'r+') as file_:
            self.json_data = json.load(file_)

    def get_table_max100(self):
        soup = bs4.BeautifulSoup(self.resp.text, 'html.parser')

        table = soup.find_all("div", class_="ritz grid-container")[0].find_all('table')[0]

        header = table.find("tr")

        self.list_header = []
        self.table_data = []

        for items in header:
            try:
                self.list_header.append(items.get_text())
            except:
                continue
        self.list_header.append('gd_id')
        # for getting the data
        HTML_data = table.find_all("tr")[1:]

        for element in HTML_data:
            sub_data = []
            for sub_element in element:
                try:
                    sub_data.append(sub_element.get_text(separator="\n"))
                except:
                    continue
            self.table_data.append(sub_data[1:])

        self.table_data = self.table_data[2:]


    def table_to_csv(self):
        dataFrame = pd.DataFrame(data=self.table_data)
        dataFrame.to_csv('Geeks11.csv')


    def table_to_xls(self):
        dataFrame = pd.DataFrame(data=self.table_data)
        dataFrame.to_excel('Geeks1.xls',index=False,header=False)



#
# url = 'https://docs.google.com/spreadsheets/d/1Y5DAslZU8ha3fHVIOkVRl1R8o1UwYeXCFVHDMZLz-cU/edit#gid=1574661862'
# gd = GoogleDrive(url)
# gd.request()
# gd.gog_drive_to_json()
# gd.data_from_jjson()
# gd.table_to_xls()
# a= 3930.62168981481
# a1= 43930.66738425926
# a2= 43930.667604166665
# a3= 44115.49199074074
# a4= 25569.0
# from pyxlsb import convert_date
# print(format(convert_date(44115.49199074074), '%Y-%m-%d %H:%M:%S')
#       )