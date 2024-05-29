import csv

input_file = "menu.csv"
output_file = "menus.csv"

with open(input_file, 'r', encoding='utf-8') as csv_in_file:
    with open(output_file, 'w', encoding='utf-8', newline="") as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header_list = ["Name","Type","Price"]
        filewriter.writerow(header_list)
        print(header_list)
        for row in filereader:
            filewriter.writerow(row)
            print(row)