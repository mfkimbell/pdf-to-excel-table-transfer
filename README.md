# pdf-to-excel-table-transfer
This purpose of this project is to learn about data aquisition from PDFs to Excel using Python. 

Tools used:
* `os` for creation of a folder to store data
* `tabula` for reading pdf data into pandas dataframes
* `pandas` for storing and manipulating data into excel
* `pdm` package manager
* `docker` for containerizing the application

```Python
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
```
    
This reads all pages of the pdf for tables and stores them into seperate excel files named sequentially. 

```Python
with pd.ExcelWriter(fullpath) as writer:
        df=table.describe()
        df.index = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
        
        df.to_excel(
            writer, sheet_name="Sheet1", index=True
        )

        table.to_excel(writer, sheet_name="Sheet2", index=False)
```

Additionally, another sheet in the excel file is created that supplies more data for the user, such as mean, count, max, and min.

Here is the original pdf shown with all its images. 

<img width="449" alt="pdf-example" src="https://user-images.githubusercontent.com/107063397/236738618-31556423-39b8-4c4f-ae24-7164d7dd00fa.png">

After the file runs, the data is all stored in a folder.

<img width="791" alt="Screenshot 2023-05-08 at 12 10 22 AM" src="https://user-images.githubusercontent.com/107063397/236739208-6aa09bfc-25b9-4c71-855c-ca1c8f8cef51.png">

Here is a snippet (limit 5) of some of the data retrieved from `tabula`:

| Unnamed: 0     | mpg  | cyl | disp | hp  | drat | wt    | qsec  | vs | am | gear | carb |
| -------------- | ---- | --- | ---- | --- | ---- | ----- | ----- | -- | -- | ---- | ---- |
| Mazda RX4      | 21   | 6   | 160  | 110 | 3.9  | 2.62  | 16.46 | 0  | 1  | 4    | 4    |
| Mazda RX4 Wag  | 21   | 6   | 160  | 110 | 3.9  | 2.875 | 17.02 | 0  | 1  | 4    | 4    |
| Datsun 710     | 22.8 | 4   | 108  | 93  | 3.85 | 2.32  | 18.61 | 1  | 1  | 4    | 1    |
| Hornet 4 Drive | 21.4 | 6   | 258  | 110 | 3.08 | 3.215 | 19.44 | 1  | 0  | 3    | 1    |

Here is the extra data aquired from the `describe()` method from pandas.

|       | mpg         | cyl         | disp        | hp          | drat         | wt          | qsec        | vs           | am           | gear         | carb        |
| ----- | ----------- | ----------- | ----------- | ----------- | ------------ | ----------- | ----------- | ------------ | ------------ | ------------ | ----------- |
| count | 32          | 32          | 32          | 32          | 32           | 32          | 32          | 32           | 32           | 32           | 32          |
| mean  | 20.090625   | 6.1875      | 230.721875  | 146.6875    | 3.5965625    | 3.21725     | 17.84875    | 0.4375       | 0.40625      | 3.6875       | 2.8125      |
| std   | 6.026948052 | 1.785921647 | 123.9386938 | 68.56286849 | 0.5346787361 | 0.978457443 | 1.786943236 | 0.5040161288 | 0.4989909172 | 0.7378040653 | 1.615199978 |
| min   | 10.4        | 4           | 71.1        | 52          | 2.76         | 1.513       | 14.5        | 0            | 0            | 3            | 1           |
| 25%   | 15.425      | 4           | 120.825     | 96.5        | 3.08         | 2.58125     | 16.8925     | 0            | 0            | 3            | 2           |
| 50%   | 19.2        | 6           | 196.3       | 123         | 3.695        | 3.325       | 17.71       | 0            | 0            | 4            | 2           |
| 75%   | 22.8        | 8           | 326         | 180         | 3.92         | 3.61        | 18.9        | 1            | 1            | 4            | 4           |
| max   | 33.9        | 8           | 472         | 335         | 4.93         | 5.424       | 22.9        | 1            | 1            | 5            | 8           |

