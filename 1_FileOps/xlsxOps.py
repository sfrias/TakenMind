import pandas as pd

# installed xlrd for excel
#import xlrd

# installed openpyxl
#import openpyxl

# Handle excel files with pandas
excFile = pd.ExcelFile('test.xlsx')

df = excFile.parse('test')
print df

