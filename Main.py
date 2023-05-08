# pip install tabula-py
# pip install xlsxwriter

import tabula
import pandas as pd
import os
import openpyxl


pdf_path = "data.pdf"
try:
    os.mkdir("data")
except:
    os.replace("data", "data")

dfs = tabula.read_pdf(pdf_path, pages="all", stream=True)

data = 1

for table in dfs:
    filepath = "data/"
    filename = "Data" + str(data) + ".xlsx"
    fullpath = filepath + filename
    print(table)
    print(type(table))
    print(table.describe())
    table.to_excel(fullpath, "data")

    data += 1

    df = table.describe()
    # pd.DataFrame({
    # 'Name': ['Alice', 'Bob', 'Charlie'],
    # 'Age': [25, 30, 35],
    # 'City': ['New York', 'London', 'Paris'] })

    # Write the dataframe to an Excel file
    with pd.ExcelWriter(fullpath) as writer:
        df=table.describe()
        df.index = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
        
        df.to_excel(
            writer, sheet_name="Sheet1", index=True
        )

        table.to_excel(writer, sheet_name="Sheet2", index=False)
