import pandas as pd
import os
import csv

path = '/Users/austinpage/Downloads/RE__NONTA_Reports/{0}'

cpi_dict = {}


report_list = [file for file in os.listdir(path[:-3]) if '~' not in file]
index = 1
for excel in report_list:
    print('{0}/{1}'.format(index, len(report_list)))
    current_path = path.format(excel)
    df = pd.read_excel(current_path, sheet_name='Affected CPIs')
    cpis = df['CPI']
    statuses = df['CPI Status']
    sams = df['SAM']
    adas = df['ADA']

    for i in range(len(cpis)):
        current_cpi = cpis[i]
        if current_cpi not in cpi_dict:
            cpi_dict[current_cpi] = {
                'Appearances':{},
                'SAM': None,
                'ADA': None
            }

            cpi_dict[current_cpi]['SAM'] = sams[i]
            cpi_dict[current_cpi]['ADA'] = sams[i]

        cpi_dict[current_cpi]['Appearances'][excel] = {'Status': statuses[i]}


    index += 1

with open('nonta_output.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)

    headers = ['SAM', 'ADA', 'CPI'] + report_list
    writer.writerow(headers)
    appearances_temp = {}
    for cpi, cpi_data in cpi_dict.items():
        sam = cpi_data['SAM']
        ada = cpi_data['ADA']

        first = [sam, ada, cpi]
        appearance_w = []

        for header in report_list:
            if header in cpi_data['Appearances']:
                appearance_w.append(cpi_data['Appearances'][header]['Status'])
            else:
                appearance_w.append('-')

        writer.writerow(first + appearance_w)

