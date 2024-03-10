import numpy as np
from time import sleep

def main():
    while True:
        print_matrix()
        sleep(1)

def print_matrix():
    n = 32
    map = np.random.randint(1 + 1, size=(n, n))
    back_map_modified = np.vectorize(get_color_coded_background)(map)
    print(back_map_modified)
    print_a_ndarray(back_map_modified, row_sep="")

def get_color_coded_background(i):
    return "\033[4{}m {} \033[0m".format(i+1, i)

def print_a_ndarray(map, row_sep=" "):
    n, m = map.shape
    fmt_str = "\n".join([row_sep.join(["{}"]*m)]*n)
    print(fmt_str.format(*map.ravel()))



if __name__ == "__main__":
    main()