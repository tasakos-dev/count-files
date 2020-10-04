import os
import os.path

def count_files(start_path):
    file_types = {}
    file_size = {}
    for root, dirs, files in os.walk(start_path):
        for f in files:
            if f[0] != '.' and f[0] != "~":
                f_parts = f.split(".")
                if len(f_parts) > 1:
                    ending = f_parts[-1]
                    file_types[ending] = file_types.get(ending, 0) + 1
                    file_size[ending] = file_size.get(ending, 0) + os.path.getsize(os.path.join(root, f))
    total_size = sum(file_size.values())/1024
    for t in file_types:
        size = file_size[t]/1024
        percent = size*100/total_size
        print("{:5s}: {:3d} {:12.2f} KB {:5.2f} %".format(t, file_types[t], size, percent))

def main():
    while True:
        directory = input('Δώσε αρχικό φάκελο [enter για τρέχων φακελο stop για έξοδο]:')
        if directory == 'stop':
            break
        elif os.path.isdir(directory):
            x = count_files(directory)
            if x == -1 :
                break
        else:
            print('Δεν βρέθηκε ο φάκελος {}'.format(directory))

if __name__ == '__main__':
    main()

