import pandas as pd
import wget

df = pd.read_excel('path to the excel file', engine='openpyxl')

for index, row, _ in df.intertuples():
    df 
    url = row 
    path = 'path to save the file'

    try: 
        wget.dowload(url, out == path)
    except Exception as ex: 
        continue
