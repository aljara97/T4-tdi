from parametros import countries
from spread import create_sheet, create_all_sheet
"""
for i in range(len(countries)):
    create_sheet(countries[i], i)
"""
create_all_sheet(countries, 6)