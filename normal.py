from datetime import datetime
from tqdm import tqdm

@profile
def main():
  with open('data/sample.csv', mode='r') as f:
    with open('data/normal_output.csv', mode='w') as output:
      for line in tqdm(f):
        output.write(line)

if __name__ == '__main__':
  start = datetime.now()
  main()
  print ("elapsed_time:{0}".format(datetime.now() - start))

"""
  10000001it [31:12, 5340.53it/s]
  elapsed_time:0:31:12.492195
  Filename: normal.py

  Line #    Mem usage    Increment   Line Contents
  ================================================
     4   13.340 MiB   13.340 MiB   @profile
     5                             def main():
     6   13.340 MiB    0.000 MiB     with open('data/sample.csv', mode='r') as f:
     7   13.340 MiB    0.000 MiB       with open('data/output.csv', mode='w') as output:     
     8   13.695 MiB    0.355 MiB         for line in tqdm(f):
     9   13.695 MiB    0.000 MiB           output.write(line)
"""