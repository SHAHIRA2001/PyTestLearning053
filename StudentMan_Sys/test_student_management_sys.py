import requests
import json
import jsonpath
import pytest

def test_add_student_data():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('C:/Users/SASLAMKH/Documents/JSON/add_stud_data.json','r')
    json_res = json.load(file.read())
    res = requests.post(url,json_res)
    print(res.text)
