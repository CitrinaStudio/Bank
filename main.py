"""Main file"""
import sys

import gen


def main():
    type = sys.argv[1]
    
    if type == "name":
        gen.gen_user(int(sys.argv[2]), float(sys.argv[3]))

    elif type == "situations":       
        gen.gen_situations(int(sys.argv[2]), float(sys.argv[3]))
    
    elif type == "all":
        gen.gen_user(int(sys.argv[2]), float(sys.argv[3]))
        gen.gen_situations(int(sys.argv[2]), float(sys.argv[3]))
    
    else:
        print("%s type is not defined" % type)
        exit(1)

if __name__ == "__main__":
    main()
