# .xlsx file

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?
#my_excel_file = open("/intermediate/ejemplo.xlsx","r+")

import xlrd

book = xlrd.open_workbook("../Intermediate/ejemplo.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name,     sh.nrows, sh.ncols))
print("Cell C2 is {0}".format(sh.cell_value(rowx=1, colx=2)))
for rx in range(sh.nrows):
    print(sh.row(rx))   