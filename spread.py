from gspread.models import Worksheet
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from get_requests import get_country_tree, get_country_data, get_all_data

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
