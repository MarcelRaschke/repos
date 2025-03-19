import os
import subprocess

# Lesen einer HDF5-Datei
df = vaex.open('large_file.hdf5')
# Berechnungen auf dem DataFrame durchführen
result = df.sum(df.column_name)
print(result)
# Filtern und Aggregieren von Daten
filtered_df = df[df.column_name > 0]
aggregated_df = filtered_df.groupby('another_column', agg={'mean_value': vaex.agg.mean('column_name')})
print(aggregated_df)
# Erstellen von Histogrammen und Visualisierungen
df.plot1d(df.column_name, what='count')
import vaex

# Lesen einer großen CSV-Datei mit Vaex
df = vaex.open('large_file.csv')
# Berechnungen auf dem DataFrame durchführen
result = df.mean(df.column_name)
print(result)
from dask_ml.model_selection import train_test_split
from dask_ml.linear_model import LogisticRegression

# Erstellen eines großen Dask-DataFrames
df = dd.read_csv('large_file.csv')
X = df[['feature1', 'feature2']]
y = df['target']

# Aufteilen der Daten in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Trainieren eines Modells
model = LogisticRegression()
model.fit(X_train, y_train)

# Vorhersagen treffen
predictions = model.predict(X_test)
print(predictions.compute())
# Lesen von Daten aus einer SQL-Datenbank mit Dask
df = dd.read_sql_table('table_name', 'sqlite:///database.db')
# Berechnungen auf dem DataFrame durchführen
result = df.sum().compute()
print(result)
import dask.array as da

# Erstellen eines großen Dask-Arrays
x = da.random.random((10000, 10000), chunks=(1000, 1000))
# Berechnungen auf dem Array durchführen
result = x.mean().compute()
print(result)
import dask.dataframe as dd

# Lesen einer großen CSV-Datei mit Dask
df = dd.read_csv('large_file.csv')
# Berechnungen auf dem DataFrame durchführen
result = df.groupby('column_name').mean().compute()
print(result)
from blaze import Data

# Lesen einer großen CSV-Datei mit Blaze
data = Data('large_file.csv')
# Verarbeiten Sie die Daten
print(data.head())
import vaex

# Lesen einer großen CSV-Datei mit Vaex
df = vaex.open('large_file.csv')
# Verarbeiten Sie den DataFrame
print(df.head())
import pyarrow.parquet as pq

# Lesen einer Parquet-Datei
table = pq.read_table('large_file.parquet')
# Verarbeiten Sie die Tabelle
print(table.to_pandas().head())
import dask.dataframe as dd

# Lesen einer großen CSV-Datei mit Dask
df = dd.read_csv('large_file.csv')
# Verarbeiten Sie den DataFrame
print(df.head())
import pandas as pd

# Lesen einer großen CSV-Datei
df = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in df:
    # Verarbeiten Sie jeden Chunk
    print(chunk.head())
from collections import deque

buffer = deque(maxlen=1000)
with open('large_file.txt', 'r', encoding='utf-8') as file:
    for line in file:
        buffer.append(line)
        if len(buffer) == buffer.maxlen:
            # Verarbeiten Sie den Puffer
            buffer.clear()
from multiprocessing import Pool

def process_line(line):
    # Verarbeiten Sie die Zeile
    return result

with open('large_file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

with Pool(processes=4) as pool:
    results = pool.map(process_line, lines)
def process_in_chunks(file_path, chunk_size=1024):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            # Verarbeiten Sie den Chunk
with open('large_file.txt', 'r', encoding='utf-8', buffering=8192) as file:
    for line in file:
        # Verarbeiten Sie jede Zeile
def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line
Absoluter Pfad der Datei: C:\Users\Michi\source\repos\ac43uaj1..txt
Schreibe Datei: C:\Users\Michi\source\repos\ac43uaj1..txt.1
Inhalt der Datei C:\Users\Michi\source\repos\ac43uaj1..txt.1:
Zeile 1
Zeile 2
Zeile 3
Absoluter Pfad der Datei: C:\Users\Michi\source\repos\ac43uaj1..txt
Schreibe Datei: C:\Users\Michi\source\repos\ac43uaj1..txt.1
Absoluter Pfad der Datei: C:\Users\Michi\source\repos\ac43uaj1..txt
with open('C:/Users/Michi/source/repos/ac43uaj1..txt', 'w', encoding='utf-8') as test_file:
    test_file.write("Zeile 1\nZeile 2\nZeile 3\n")
import os

def split_file(input_file, lines_per_file):
    absolute_path = os.path.abspath(input_file)
    print(f"Absoluter Pfad der Datei: {absolute_path}")  # Debug-Ausgabe
    with open(absolute_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    file_count = 1
    for i in range(0, len(lines), lines_per_file):
        with open(f"{absolute_path}.{file_count}", 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines[i:i + lines_per_file])
        file_count += 1

if __name__ == "__main__": 
    input_file = 'ac43uaj1..txt'
    lines_per_file = 160
    split_file(input_file, lines_per_file)
    import os

    def split_file(input_file, lines_per_file):
        absolute_path = os.path.abspath(input_file)
        print(f"Absoluter Pfad der Datei: {absolute_path}")  # Debug-Ausgabe
        with open(absolute_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        file_count = 1
        for i in range(0, len(lines), lines_per_file):
            with open(f"{absolute_path}.{file_count}", 'w', encoding='utf-8') as output_file:
                output_file.writelines(lines[i:i + lines_per_file])
            file_count += 1

    if __name__ == "__main__": 
        input_file = 'ac43uaj1..txt'
        lines_per_file = 160
        split_file(input_file, lines_per_file)
def split_file(input_file, lines_per_file):
    # PowerShell-Befehl ausführen
    subprocess.run(['powershell', '-Command', 'Get-Process -Name "deinProzessName"'])
    subprocess.run(['powershell', '-Command', 'cd "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE"'])

    absolute_path = os.path.abspath(input_file)
    with open(absolute_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    file_count = 1
    for i in range(0, len(lines), lines_per_file):
        with open(f"{absolute_path}.{file_count}", 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines[i:i + lines_per_file])
        file_count += 1

import os

def split_file(input_file, lines_per_file):
    absolute_path = os.path.abspath(input_file)
    with open(absolute_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    file_count = 1
    for i in range(0, len(lines), lines_per_file):
        with open(f"{absolute_path}.{file_count}", 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines[i:i + lines_per_file])
        file_count += 1

import os

def split_file(input_file, lines_per_file):
    absolute_path = os.path.abspath(input_file)
    print(f"Absoluter Pfad der Datei: {absolute_path}")  # Debug-Ausgabe
    with open(absolute_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    file_count = 1
    for i in range(0, len(lines), lines_per_file):
        with open(f"{absolute_path}.{file_count}", 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines[i:i + lines_per_file])
        file_count += 1

import os

# Testdatei erstellen
with open('C:/Users/Michi/source/repos/ac43uaj1..txt', 'w', encoding='utf-8') as test_file:
    test_file.write("Zeile 1\nZeile 2\nZeile 3\n")

def split_file(input_file, lines_per_file):
    absolute_path = os.path.abspath(input_file)
    print(f"Absoluter Pfad der Datei: {absolute_path}")  # Debug-Ausgabe
    with open(absolute_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    file_count = 1
    for i in range(0, len(lines), lines_per_file):
        with open(f"{absolute_path}.{file_count}", 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines[i:i + lines_per_file])
        file_count += 1

import os

# Testdatei erstellen
with open('C:/Users/Michi/source/repos/ac43uaj1..txt', 'w', encoding='utf-8') as test_file:
    test_file.write("Zeile 1\nZeile 2\nZeile 3\n")

def split_file(input_file, lines_per_file):
    absolute_path = os.path.abspath(input_file)
    print(f"Absoluter Pfad der Datei: {absolute_path}")  # Debug-Ausgabe
    with open(absolute_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    file_count = 1
    for i in range(0, len(lines), lines_per_file):
        output_file_path = f"{absolute_path}.{file_count}"
        print(f"Schreibe Datei: {output_file_path}")  # Debug-Ausgabe
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines[i:i + lines_per_file])
        file_count += 1

    # Überprüfen Sie den Inhalt der aufgeteilten Dateien
    for j in range(1, file_count):
        output_file_path = f"{absolute_path}.{j}"
        print(f"Inhalt der Datei {output_file_path}:")
        with open(output_file_path, 'r', encoding='utf-8') as output_file:
            print(output_file.read())

import os

# Testdatei erstellen
with open('C:/Users/Michi/source/repos/ac43uaj1..txt', 'w', encoding='utf-8') as test_file:
    test_file.write("Zeile 1\nZeile 2\nZeile 3\n")

def split_file(input_file, lines_per_file):
    absolute_path = os.path.abspath(input_file)
    print(f"Absoluter Pfad der Datei: {absolute_path}")  # Debug-Ausgabe

    file_count = 1
    line_count = 0
    output_file = open(f"{absolute_path}.{file_count}", 'w', encoding='utf-8')

    with open(absolute_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line_count == lines_per_file:
                output_file.close()
                file_count += 1
                line_count = 0
                output_file = open(f"{absolute_path}.{file_count}", 'w', encoding='utf-8')
            output_file.write(line)
            line_count += 1

    output_file.close()

    # Überprüfen Sie den Inhalt der aufgeteilten Dateien
    for j in range(1, file_count + 1):
        output_file_path = f"{absolute_path}.{j}"
        print(f"Inhalt der Datei {output_file_path}:")
        with open(output_file_path, 'r', encoding='utf-8') as output_file:
            print(output_file.read())

if __name__ == "__main__": 
    input_file = 'ac43uaj1..txt'
    lines_per_file = 160
    split_file(input_file, lines_per_file)
