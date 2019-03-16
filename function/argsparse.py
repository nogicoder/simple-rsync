import argparse

#create an argparse instance named parser
parser = argparse.ArgumentParser(prog="dumbrsync", description="A dumb version of \
                                 da mighty rsync")
#define arguments that will be executed
parser.add_argument('-u', '--update', help='skip files that are newer on the \
                    receiver')
parser.add_argument('-c', '--checksum', help='skip based on checksum, not \
                    mod-time & size')
parser.add_argument('SRC_FILE', help="input in source file's name")
parser.add_argument('DESTINATION', help="input in existed directory or desired\
                    destination file's name")
#turn data input from command-line to objects
arg = vars(parser.parse_args())
src_file = arg['SRC_FILE']
dest = arg['DESTINATION']
