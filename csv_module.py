from datetime import datetime
from tqdm import tqdm
import csv

@profile
def main():
  with open('data/sample.csv', mode='r') as f:
    with open('data/csv_module_output.csv', mode='w') as output:
      reader = csv.reader(f)
      for row in tqdm(reader):
        i = 0
        for element in row:
          output.write(element)
          i += 1
          if i != len(row):
            output.write(',')
        output.write('\n')

if __name__ == '__main__':
  start = datetime.now()
  main()
  print ("elapsed_time:{0}".format(datetime.now() - start))