from datetime import datetime
from tqdm import tqdm
import pandas as pd

@profile
def main():
  reader = pd.read_csv('data/sample.csv', chunksize=1000)
  header = True
  for row_chunk in tqdm(reader):
    row_chunk.to_csv('data/pandas_output.csv', mode='a', header=header, index=False)
    if header:
      header = False

if __name__ == '__main__':
  start = datetime.now()
  main()
  print ("elapsed_time:{0}".format(datetime.now() - start))