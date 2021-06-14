from gspread.models import Worksheet
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from get_requests import get_country_tree, get_country_data, get_all_data, filter_max_year, filter_max_year_bmi

def create_sheet(country, index_):
    # Acceso a Google Sheet
    gc = gspread.service_account(filename='editor_credentials.json')
    sh = gc.open_by_key('1Hj1tvyzA5lSC70DmAGarbpdS8T8kBGH7uUBVwhHpYIE')
    worksheet = sh.get_worksheet(index_)

    data = get_country_data(country)
    # Agregar datos a la hoja
    my_dataframe = pd.DataFrame(data, 
                                columns = ['GHO', 'COUNTRY', 'SEX', 'YEAR', 'GHECAUSES', 'AGEGROUP', 'DISPLAY', 'NUMERIC', 'LOW', 'HIGH'])
    set_with_dataframe(worksheet, my_dataframe)

def create_all_sheet(countries, index_):
    gc = gspread.service_account(filename='editor_credentials.json')
    sh = gc.open_by_key('1Hj1tvyzA5lSC70DmAGarbpdS8T8kBGH7uUBVwhHpYIE')
    worksheet = sh.get_worksheet(index_)

    data = get_all_data(countries)
    # Agregar datos a la hoja
    my_dataframe = pd.DataFrame(data, 
                                columns = ['GHO', 'COUNTRY', 'SEX', 'YEAR', 'GHECAUSES', 'AGEGROUP', 'DISPLAY', 'NUMERIC', 'LOW', 'HIGH'])
    set_with_dataframe(worksheet, my_dataframe)

    # Filtra los datos para la hoja del máximo año
    max_data = filter_max_year(data)
    max_worksheet = sh.get_worksheet(index_ + 1)
    max_dataframe = pd.DataFrame(max_data, 
                                columns = ['GHO', 'COUNTRY', 'SEX', 'YEAR', 'GHECAUSES', 'AGEGROUP', 'DISPLAY', 'NUMERIC', 'LOW', 'HIGH'])
    set_with_dataframe(max_worksheet, max_dataframe)

    #Datos para el máximo año de BMI
    max_data_bmi = filter_max_year_bmi(data)
    bmi_worksheet = sh.get_worksheet(index_ + 2)
    bmi_dataframe = pd.DataFrame(max_data_bmi, 
                                columns = ['GHO', 'COUNTRY', 'SEX', 'YEAR', 'GHECAUSES', 'AGEGROUP', 'DISPLAY', 'NUMERIC', 'LOW', 'HIGH'])
    set_with_dataframe(bmi_worksheet, bmi_dataframe)
