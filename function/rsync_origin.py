#!/usr/bin/env python3

import argparse
import os
import sys
import hashlib
import difflib


def is_hard_link(file):
    link_number = os.stat(file).st_nlink
    return link_number > 1


def check_size(source_path, dest_path):
    source_size = os.lstat(source_path).st_size
    dest_size = os.lstat(dest_path).st_size
    return source_size == dest_size


def check_mtime(source_path, dest_path, u=False):
    source_time = os.lstat(source_path).st_mtime
    dest_time = os.lstat(dest_path).st_mtime
    if not u:
        return dest_time == source_time
    if u:
        return dest_time > source_time


def change_mode(source_path, dest_path):
    mode = os.lstat(source_path).st_mode
    os.chmod(dest_path, mode)


def change_time(source_path, dest_path):
    stat = os.lstat(source_path)
    atime = stat.st_atime
    mtime = stat.st_mtime
    os.utime(dest_path, (atime, mtime), follow_symlinks=False)


def create_file(source_path, dest_path):
    dest_file = open(dest_path, 'w')
    source_file = open(source_path, 'r')
    content = source_file.read()
    dest_file.write(content)
    dest_file.close()
    source_file.close()


def get_hash(path):
    md5 = hashlib.md5()
    file = open(path, 'rb')
    data = file.read()
    md5.update(data)
    return md5.digest()


def check_hash(source_path, dest_path):
    return get_hash(source_path) == get_hash(dest_path)


def update_content(source_path, dest_path, source_size, dest_size):
    fd_source = os.open(source_path, os.O_RDWR)
    fd_dest = os.open(dest_path, os.O_RDWR)
    source_content = os.read(fd_source, source_size)
    dest_content = os.read(fd_dest, dest_size)
    direction = difflib.SequenceMatcher(None, dest_content,
                                        source_content).get_opcodes()
    for tag, i1, i2, j1, j2 in direction:
        if tag in ['replace', 'insert', 'delete']:
            os.lseek(fd_dest, i1, 0)
            os.write(fd_dest, source_content[j1:])
            os.close(fd_dest)
            os.close(fd_source)


if __name__ == "__main__":
    # create an argparse instance named parser
    parser = argparse.ArgumentParser(prog="dumbrsync", description="A dumb \
                                     version of da mighty rsync")
    # define arguments that will be executed
    parser.add_argument('SRC_FILE', help="input in source file's name")
    parser.add_argument('DESTINATION', help="input in existed directory or \
                        desired destination file's name")
    parser.add_argument('-u', '--update', action='store_true', help='skip \
                        update on newer file in destination')
    parser.add_argument('-c', '--checksum', action='store_true', help='skip \
                        update based on checksum./# REVIEW: ')
    # turn data input from command-line to objects
    args = parser.parse_args()
    # assign variable
    source = args.SRC_FILE
    dest = args.DESTINATION
    source_path = os.path.abspath(source)
    dest_path = os.path.abspath(dest)
    if args.update and args.checksum:
        raise RuntimeError('You can only choose one!!')
    elif not os.path.exists(source_path):  # check source existence
        print('rsync: link_stat "' + source_path +
              '" failed: No such file or directory (2)')
    elif not os.access(source_path, os.R_OK):
        print('rsync: send_files failed to open "' + source_path +
              '": Permission denied (13)')
    elif os.path.isdir(source_path):
        raise OSError(source_path + ' is a directory!!')
    else:
        if "/" in source:
            source_list = source.split("/")
            source = source_list[1]  # get source file name
        if "/" in dest:
            if dest[-1] != "/":
                dest_list = dest.split("/")
                dest_dir = os.path.abspath(dest_list[0])
            elif dest[-1] == "/":
                dest_dir = dest_path
            if not os.path.exists(dest_dir):  # if dest is dir
                os.mkdir(dest_dir)  # create dir/ if not exists yet
        if os.path.exists(dest_path) and (os.path.isdir(dest_path) or
           dest[-1] == "/"):  # Eg: file1 dir or file1 dir/
            dest_path += "/" + source
        if (dest[-1] == "/" and os.path.exists(dest_path) and
           os.path.isfile(dest_path)):  # Eg: file1 dir/, file named dir exist
            print('rsync: ERROR: cannot stat destination "' + source_path
                  + '": Not a directory (20)')
        if source_path == dest_path:  # Eg: dir/test dir/
            sys.exit()
        if os.path.exists(dest_path):
            if (args.update is False and args.checksum is False and
               check_mtime(source_path, dest_path) and
               check_size(source_path, dest_path)):
                change_mode(source_path, dest_path)
                change_time(source_path, dest_path)
                sys.exit()
            elif ((args.update and check_mtime(source_path, dest_path, u=True))
                  or (args.checksum and check_hash(source_path, dest_path))):
                change_mode(source_path, dest_path)
                change_time(source_path, dest_path)
                sys.exit()
            else:
                source_size = os.path.getsize(source_path)
                dest_size = os.path.getsize(dest_path)
                if (os.path.islink(dest_path) or is_hard_link(dest_path) or
                   os.path.islink(source_path) or is_hard_link(source_path) or
                   source_size < dest_size):
                    os.unlink(dest_path)
                else:
                    update_content(source_path, dest_path,
                                   source_size, dest_size)
                    change_mode(source_path, dest_path)
                    change_time(source_path, dest_path)
        if not os.path.exists(dest_path):  # if dest not exist
            if os.path.islink(source_path):  # if source is softlink
                origin_path = os.path.abspath(os.readlink(source_path))
                os.symlink(origin_path, dest_path)
                change_time(source_path, dest_path)
            elif is_hard_link(source_path):  # if source is hardlink
                os.link(source_path, dest_path)
                change_mode(source_path, dest_path)
                change_time(source_path, dest_path)
            else:  # if source is normal file
                create_file(source_path, dest_path)
                change_mode(source_path, dest_path)
                change_time(source_path, dest_path)
