import csv

def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Extracted Text'])
        for item in data:
            writer.writerow([item])  # Each item is a string of extracted text


 
