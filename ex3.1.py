import csv

# Llegim el fitxer CSV d'entrada
input_file = 'airline-flight.csv'
output_file = 'airline-2022-2023.csv'


with open(input_file, mode='r') as infile:
    reader = csv.DictReader(infile)
    

    with open(output_file, mode='w', newline='') as outfile:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        

        writer.writeheader()
        
        for row in reader:

            if row['Year'] in ['2022','2023'] :
                writer.writerow(row)

print(f"S'ha desat a {output_file}")