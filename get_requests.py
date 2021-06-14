from sys import displayhook
import requests
import xml.etree.ElementTree as ET
from parametros import gho_ind
from datetime import datetime

# Se utilizó código de respuestas del siguiente link: https://stackoverflow.com/questions/29810572/save-xml-response-from-get-call-using-python/29810645

def get_country_file(country):
    r = requests.get(f'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_{country}.xml')
    root = ET.fromstring(r.text)
    tree = ET.ElementTree(root)
    tree.write(f'file_{country}.xml')

def get_country_tree(country):
    r = requests.get(f'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_{country}.xml')
    root = ET.fromstring(r.text)
    print(f'Root tag: {root.tag}')
    tree = ET.ElementTree(root)
    if tree:
        return tree
    else:
        return -1

def get_country_data(country):
    r = requests.get(f'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_{country}.xml')
    root = ET.fromstring(r.text)
    rows = []
    for child in root:

        gho = child.find('GHO').text
        if gho in gho_ind or "BMI" in gho:
            country = child.find('COUNTRY').text
            sex = child.find('SEX').text
            year = int(child.find('YEAR').text)
            ghe_causes = child.find('GHECAUSES').text
            age_group = child.find('AGEGROUP').text
            display = child.find('Display').text
            numeric = child.find('Numeric')
            low = child.find('Low')
            high = child.find('High')
            numeric_ = None
            low_ = None
            high_ = None
            if numeric is not None:
                numeric_ = float(numeric.text)
            if low is not None:
                low_ = float(low.text)
            if high is not None:
                high_ = float(high.text)
            child_attributes = [gho, country, sex, year, ghe_causes, age_group, display, numeric_, low_, high_]
            rows.append(child_attributes)
            print(child_attributes)
    return rows

def get_all_data(countries):
    rows = []
    for country in countries:
        r = requests.get(f'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_{country}.xml')
        root = ET.fromstring(r.text)
        for child in root:
            gho = child.find('GHO').text
            if gho in gho_ind or "BMI" in gho:
                country = child.find('COUNTRY').text
                sex = child.find('SEX').text
                year = int(child.find('YEAR').text)
                ghe_causes = child.find('GHECAUSES').text
                age_group = child.find('AGEGROUP').text
                display = child.find('Display').text
                numeric = child.find('Numeric')
                low = child.find('Low')
                high = child.find('High')
                numeric_ = None
                low_ = None
                high_ = None
                if numeric is not None:
                    numeric_ = float(numeric.text)
                if low is not None:
                    low_ = float(low.text)
                if high is not None:
                    high_ = float(high.text)
                child_attributes = [gho, country, sex, year, ghe_causes, age_group, display, numeric_, low_, high_]
                rows.append(child_attributes)
                print(child_attributes)
    return rows

def filter_max_year(data):
    max_year = 0
    for row in data:
        if row[3] > max_year:
            max_year = row[3]
    data_max = filter(lambda row: row[3] == max_year, data)
    return list(data_max)


def filter_max_year_bmi(data):
    max_year = 0
    for row in data:
        if int(row[3]) > max_year and "Mean BMI" in row[0]:
            max_year = row[3]
    data_max = filter(lambda row: int(row[3]) == max_year, data)
    return list(data_max)

        
