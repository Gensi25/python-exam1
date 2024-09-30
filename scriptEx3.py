import urllib
import os 
import csv
import zipfile

url = "https://gitlab.com/xtec/python/data/-/raw/main/airline-flight.zip?ref_type=heads"
zip_filename = "airline-flight.zip"

def baixarZip(url, zip_filename):
    
    with urllib3.PoolManager().request('GET', url, preload_content=False) as response, open(zip_filename, 'wb') as out_file:
        print(f"Descarregant {zip_filename}...")
        while (data := response.read(1024)):  
            out_file.write(data)
        print(f"Descàrrega completada: {zip_filename}")

def descomprimirArxiu_ObtenirCSV(zip_filename):
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall()  
        return next((file for file in zip_ref.namelist() if file.endswith('.csv')), None)     

def guardarcontingutCSV(csv_filename):
    with open(csv_filename, 'r') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]    

def main():
    csv_filename = "airline-flight.csv" 
    if not csv_filename:
        if not os.path.exists(zip_filename):
            baixarZip(url, zip_filename)
        csv_filename = descomprimirArxiu_ObtenirCSV(zip_filename)

    csv_lines = guardarcontingutCSV(csv_filename)
    print(csv_lines[:20]) 

if __name__ == "__main__":
    main()