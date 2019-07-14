# Handle excel files with pandas
import pandas as pd
# Read .xlsx file using pandas
excFile = pd.ExcelFile('InputSheets.xlsx')
# Export 0_Deaths_1962_2016 as 0_Deaths_1962_2016.csv
df0 = excFile.parse('0_Deaths_1962_2016')
df0.to_csv('0_Deaths_1962_2016.csv', index=False, encoding='utf-8')
# Export sheet 1_Yearly_AMT as 1_Yearly_AMT.csv
df0 = excFile.parse('1_Yearly_AMT')
df0.to_csv('1_Yearly_AMT.csv', index=False, encoding='utf-8')
# Export sheet 2_EstCO2_AMT as 2_EstCO2_AMT.csv
df0 = excFile.parse('2_EstCO2_AMT')
df0.to_csv('2_EstCO2_AMT.csv', index=False, encoding='utf-8')
# Export sheet 3_Attrib_Year_AMT as 3_Attrib_Year_AMT.csv
df0 = excFile.parse('3_Attrib_Year_AMT')
df0.to_csv('3_Attrib_Year_AMT.csv', index=False, encoding='utf-8')
# Export 4_Prod_Year_AMT as 4_Prod_Year_AMT.csv
df0 = excFile.parse('4_Prod_Year_AMT')
df0.to_csv('4_Prod_Year_AMT.csv', index=False, encoding='utf-8')
# Export sheet 5_Prod_Transm_AMT as 5_Prod_Transm_AMT.csv
df0 = excFile.parse('5_Prod_Transm_AMT')
df0.to_csv('5_Prod_Transm_AMT.csv', index=False, encoding='utf-8')
# Export sheet 6_Prod_Cars as 6_Prod_Cars.csv
df0 = excFile.parse('6_Prod_Cars')
df0.to_csv('6_Prod_Cars.csv', index=False, encoding='utf-8')
# Export sheet 7_Prod_Truck as 7_Prod_Truck.csv
df0 = excFile.parse('7_Prod_Truck')
df0.to_csv('7_Prod_Truck.csv', index=False, encoding='utf-8')
# Export sheet 8_CO2Em_2012 as 8_CO2Em_2012.csv
df0 = excFile.parse('8_CO2Em_2012')
df0.to_csv('8_CO2Em_2012.csv', index=False, encoding='utf-8')
# Export sheet 9_CO2Em_2017 as 9_CO2Em_2017.csv
df0 = excFile.parse('9_CO2Em_2017')
df0.to_csv('9_CO2Em_2017.csv', index=False, encoding='utf-8')