
# Data Entry

DataEntry.py contains a set of scripts that read DigiKala datasets and normalizes their attributes and stores them in a Relational Database.

Analysis.py and Analysis.ipynb contain sets of scripts to analyse the datasets using DataFrames.

## Requirements:

- MySQL Server 8.0.16
- Python 3.7.3
- Python Modules:
  - openpyxl 2.6.2
  - pandas 0.24.2
  - numpy 1.16.4
  - matplotlib 3.1.0

## Usage

In order to read Excel and CSV files, you should specify the path to the fifth dataset "5-awte8wbd.xlsx" into product_list_path variable and the path to the third dataset "3-p5s3708k.csv" into buying_history_path variable.

```python
product_list_path = '{path to the project extraction folder}\\part1\\codes\\data\\\\5-awte8wbd.xlsx'
buying_history_path = '{path to the project extraction folder}\\part1\\codes\\data\\\\3-p5s3708k.csv'
```

For instance:

```python
product_list_path = 'C:\\Users\\James\\Desktop\\project\\part1\\codes\\data\\5-awte8wbd.xlsx'
buying_history_path = 'C:\\Users\\James\\Desktop\\project\\part1\\codes\\data\\\\3-p5s3708k.csv'
```

Before running the code, you should initialize a MySQL Server with mentioned parameters set to:


```bash
host = '127.0.0.1'
username = 'root' OR user = 'root'
password = '0000'
```

Then, you can run the code, and wait till the code finishes the data entry process. (This can take some time depending on your system processing power.)

For the second part, you should do the same thing as seen before and enter the addresses belonging to the datasets in proper places in Analysis.py (or Analysis.ipynb) respectively.