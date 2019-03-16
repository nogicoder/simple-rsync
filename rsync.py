#!/usr/bin/env python3
import argparse
import os
import sys
import hashlib


"""----------------------------SUB-FUNCTION---------------------------------"""


def is_hard_link(file):  # check if file has hardlink
    link_number = os.stat(file).st_nlink
    return link_number > 1


def check_size(source_path, dest_path):  # check if equal size
    source_size = os.lstat(source_path).st_size
    dest_size = os.lstat(dest_path).st_size
    return source_size == dest_size


def check_mtime(source_path, dest_path, u=False):  # check time condition
    source_time = os.lstat(source_path).st_mtime
    dest_time = os.lstat(dest_path).st_mtime
    if not u:
        return dest_time == source_time
    if u:
        return dest_time > source_time


def change_mode(source_path, dest_path):  # change file permission
    mode = os.lstat(source_path).st_mode
    os.chmod(dest_path, mode)


def change_time(source_path, dest_path):  # change file time
    stat = os.lstat(source_path)
    atime = stat.st_atime
    mtime = stat.st_mtime
    os.utime(dest_path, (atime, mtime), follow_symlinks=False)


def create_file(source_path, dest_path):  # create new file
    dest_file = open(dest_path, 'w')
    source_file = open(source_path, 'r')
    content = source_file.read()
    dest_file.write(content)
    dest_file.close()
    source_file.close()


def get_hash(path):  # get hash of two file
    md5 = hashlib.md5()
    file = open(path, 'rb')
    data = file.read()
    md5.update(data)
    return md5.digest()


def check_hash(source_path, dest_path):  # check if hashes equal
    return get_hash(source_path) == get_hash(dest_path)


def common_prefix(lst):  # get common prefix of two strings
    s1 = min(lst)
    s2 = max(lst)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1


# update content from source to dest
def update_content(source_path, dest_path, source_size, dest_size):
    content_list = []
    fd_source = os.open(source_path, os.O_RDONLY)
    fd_dest = os.open(dest_path, os.O_RDWR)
    source_content = os.read(fd_source, source_size)
    dest_content = os.read(fd_dest, dest_size)
    content_list.append(source_content)
    content_list.append(dest_content)
    cp = common_prefix(content_list)
    os.lseek(fd_dest, len(cp), 0)
    os.write(fd_dest, source_content[len(cp):])
    os.close(fd_dest)
    os.close(fd_source)


# check the condition of two files
def sync_file(source_path, dest_path):
    if os.path.exists(dest_path):  # if dest file exists
        # if no options chose and same time & size
        if (not args.update and not args.checksum and
           check_mtime(source_path, dest_path) and
           check_size(source_path, dest_path)):
            change_mode(source_path, dest_path)
            change_time(source_path, dest_path)
        # if -u with newer dest time and -c with same hash
        elif ((args.update and check_mtime(source_path, dest_path, u=True))
              or (args.checksum and check_hash(source_path, dest_path))):
            change_mode(source_path, dest_path)
            change_time(source_path, dest_path)
        else:  # if src/dest is link, dest > source or no permission on source
            source_size = os.path.getsize(source_path)
            dest_size = os.path.getsize(dest_path)
            if (os.path.islink(dest_path) or is_hard_link(dest_path) or
               os.path.islink(source_path) or is_hard_link(source_path) or
               source_size < dest_size or not os.access(dest_path, os.R_OK) or
               not os.access(dest_path, os.W_OK)):
                os.unlink(dest_path)
            else:  # if two file has no link and no options is chose
                update_content(source_path, dest_path, source_size, dest_size)
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


# copy the dirs and files recursively
def copy_tree(src, dst):
    names = os.listdir(src)
    if os.path.exists(dst):  # if dest exist
        pass
    elif not os.path.exists(dst):  # if dest not exist -> create new
        os.mkdir(dst)
    for item in names:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isdir(src_path):
            copy_tree(src_path, dst_path)
        elif os.path.isfile(src_path):
            sync_file(src_path, dst_path)


"""---------------------------MAIN FUNCTION---------------------------------"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="dumbrsync", description="A dumb \
                                     version of da mighty rsync")
    # define arguments that will be executed
    parser.add_argument('SRC_FILE', nargs='+',
                        help='input in source file name')
    parser.add_argument('DESTINATION', help='input in existed directory or \
                        desired destination file name')
    parser.add_argument('-u', '--update', action='store_true', help='skip \
                        update on newer file in destination')
    parser.add_argument('-c', '--checksum', action='store_true', help='skip \
                        update based on checksum')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='recursively copy directories')
    # turn data input from command-line to objects
    args = parser.parse_args()
    # assign variable
    source = args.SRC_FILE
    dest = args.DESTINATION
    if args.recursive and not os.path.exists(dest):  # create dest dir
        os.mkdir(dest)
    for item in source:  # loop through source items
        source_name = item
        source_path = os.path.abspath(item)
        dest_path = os.path.abspath(dest)
        if not os.path.exists(source_path):  # check each item existence
            print('rsync: link_stat "' + source_path +
                  '" failed: No such file or directory (2)')
        elif not os.access(source_path, os.R_OK):  # check each item permission
            print('rsync: send_files failed to open "' + source_path +
                  '": Permission denied (13)')
        elif args.recursive and os.path.isdir(item):  # opt r with item as dir
            if item[-1] != "/":  # if no '/' -> copy the root dir
                dest_path = os.path.abspath(dest) + "/" + item
                os.mkdir(dest_path)
            copy_tree(source_path, dest_path)  # copy childen dirs/ files
        elif os.path.isfile(item):  # if item is file
            if "/" in item:
                source_list = item.split("/")
                source_name = source_list[1]  # get item file name
            if os.path.exists(dest_path) and os.path.isdir(dest_path):
                dest_path += "/" + source_name
            sync_file(source_path, dest_path)
