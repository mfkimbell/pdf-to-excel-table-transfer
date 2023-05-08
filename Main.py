# pip install tabula-py
# pip install xlsxwriter

import tabula
import pandas as pd
import os

pdf_path = "data.pdf"
os.mkdir("data")

dfs = tabula.read_pdf(pdf_path, pages="all", stream=True)
# read_pdf returns list of DataFrames
data = 1

for table in dfs:
    filename = "data/Data" + str(data) + ".xlsx"
    print(table)
    table.to_excel(filename)
    data += 1

result_df = pd.concat(dfs)
result_df.to_excel("data.xlsx")
