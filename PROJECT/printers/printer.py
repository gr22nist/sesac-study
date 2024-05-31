import csv

class DataPRT:
  def print_to_screen(self, data):
    for d in data:
      print(d)
      
  def print_to_file(self, data, filename):
    with open(filename, 'w', encoding='utf-8', newline="") as csv_file:
      csv_writer = csv.writer(csv_file)
      for d in data:
        csv_writer.writerow(d)