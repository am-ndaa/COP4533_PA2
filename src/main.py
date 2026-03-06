from fifo import fifo  
from lru import lru
from optff import optff
from read_file import read_file
import sys

def main():
    if len(sys.argv) < 2:
        print("ERROR...Must include file name of data set in data/")
        return -1
        
    file_name = sys.argv[1]
    k, requests = read_file(file_name)
    

    fifo_misses = fifo(requests, k)
    lru_misses = lru(k, requests)
    optff_misses = optff(k, requests)
    
    print(f"FIFO: {fifo_misses}")
    print(f"LRU: {lru_misses}")
    print(f"OPTFF: {optff_misses}")

if __name__ == "__main__":
    main()