import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']=100
sheet['B1']=200
sheet['C1']=300
sheet['D1']='=SUM(A1:C1)'
wb.save("SUM.xlsx")
 
