import openpyxl as op

local = 'BotEspec/dado/'
name = 'dados_espc.xlsx'
dado1 = local + name

xlsx = op.load_workbook(dado1) 
sheet = xlsx.active 
data = sheet.rows
DataFrameCSV = open('data.csv','w+')
for row in data:
    l = list(row)
    for i in range(len(l)):
        if i == len(l) - 1:
            DataFrameCSV.write(str(l[i].value))
        else:
            DataFrameCSV.write(str(l[i].value) + ',')
        DataFrameCSV.write('\n')
DataFrameCSV.close()