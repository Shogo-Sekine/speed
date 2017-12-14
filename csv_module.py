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

"""
  10000001it [22:57:55, 120.96it/s]
  elapsed_time:22:57:55.272260
  Filename: csv_module.py

  Line #    Mem usage    Increment   Line Contents
  ================================================
     5   13.695 MiB   13.695 MiB   @profile
     6                             def main():
     7   13.695 MiB    0.000 MiB     with open('data/sample.csv', mode='r') as f:
     8   13.695 MiB    0.000 MiB       with open('data/csv_module_output.csv', mode='w') as output:
     9   13.695 MiB    0.000 MiB         reader = csv.reader(f)
    10   16.090 MiB    0.082 MiB         for row in tqdm(reader):
    11   16.090 MiB    0.000 MiB           i = 0
    12   16.090 MiB    0.305 MiB           for element in row:
    13   16.090 MiB    1.477 MiB             output.write(element)
    14   16.090 MiB    0.531 MiB             i += 1
    15   16.090 MiB    0.000 MiB             if i != len(row):
    16   16.090 MiB    0.000 MiB               output.write(',')
    17   16.090 MiB    0.000 MiB           output.write('\n')

"""