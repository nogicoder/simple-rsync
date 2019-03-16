#!/usr/bin/env python3
import os
import argparse
import hashlib


def take_args():
    parser = argparse.ArgumentParser(usage='./rsync.py [OPTIONS]\
 SRC_FILE DESTINATION')
    parser.add_argument('src', type=str, nargs='*')
    parser.add_argument('dst', type=str)
    parser.add_argument('-c', '--checksum', action='store_true')
    parser.add_argument('-u', '--update', action='store_true')
    parser.add_argument('-r', '--recursive', action='store_true')
    args = parser.parse_args()
    return args


def file_path(src, dst):
    src_file_name = os.path.split(src)[1]
    dst_file_name = os.path.split(dst)[1]
    return src_file_name, dst_file_name


def check_option(read_src, read_dst, dst_file_name):
    if args.checksum:
        return check_sum(read_src, read_dst)
    elif args.update:
        return check_update(dst_file_name)
    else:
        return check_size(dst_file_name) and check_time(dst_file_name)


"""---------------------------------[OPTION]-------------------------------"""


def check_update(dst_file_name):  # -u update
    dst_mod_time = os.stat(dst_file_name).st_mtime
    src_mod_time = os.stat(filesrc).st_mtime
    if dst_mod_time == src_mod_time:
        return check_size(dst_file_name)
    return dst_mod_time > src_mod_time


def check_sum(read_src, read_dst):  # -c skip based on checksum
    md5_src = hashlib.md5(read_src).hexdigest()
    md5_dst = hashlib.md5(read_dst).hexdigest()
    return md5_src == md5_dst


def check_size(dst_file_name):
    src_size = os.stat(filesrc).st_size
    dst_size = os.stat(dst_file_name).st_size
    return src_size == dst_size


def check_time(dst_file_name):
    src_access_time = os.stat(filesrc).st_atime
    src_modification_time = os.stat(filesrc).st_mtime
    dst_access_time = os.stat(dst_file_name).st_atime
    dst_modification_time = os.stat(dst_file_name).st_mtime
    return src_access_time == dst_access_time and\
        src_modification_time == dst_modification_time


def keep_symlink(src_file_name, dst_file_name):  # -l preserve symlink
    src_link = os.readlink(filesrc)
    dst_link = dst_file_name
    if os.path.isfile(dst_link):
        os.unlink(dst_link)
    src_access_time = os.lstat(filesrc).st_atime
    src_modification_time = os.lstat(filesrc).st_mtime
    os.symlink(src_link, dst_link)
    os.utime(dst_link,
             (src_access_time, src_modification_time), follow_symlinks=False)


def keep_links(src_file_name, dst_file_name):
    """keep hard link if link of file > 1
       if not, check for possible symlink"""
    if os.lstat(filesrc).st_nlink > 1:  # -H preserve hardlink
        if os.path.isfile(dst_file_name):
            os.unlink(dst_file_name)
        os.link(filesrc, dst_file_name)
    elif os.path.islink(filesrc):
        keep_symlink(src_file_name, dst_file_name)


def keep_permission(dst_file_name):   # -p preserve permissions
    get_mod = os.stat(filesrc).st_mode
    os.chmod(dst_file_name, get_mod)


def keep_time(dst_file_name):  # -t preserve modification time and access time
    src_access_time = os.stat(filesrc).st_atime
    src_modification_time = os.stat(filesrc).st_mtime
    os.utime(dst_file_name, (src_access_time, src_modification_time))


"""-----------------------------MAIN------------------------------"""


def longest_common_sub(src_file_name, dst_file_name, read_src, read_dst,
                       src_file, dst_file):
    """Look for the longest common string in text
       if dest file are the the same with source but missing line or text
       => append text
       else => overwrite everything in dest file"""
    src_len = len(read_src)
    dst_len = len(read_dst)
    line = 0
    for line1, line2 in zip(read_src, read_dst):
        if line1 == line2:
            line += 1
        else:
            break
    if len(read_src) < len(read_dst):
        os.truncate(dst_file, os.stat(src_file).st_size)
    os.pwrite(dst_file, read_src[line:], line)


def main(src_file_name, dst_file_name):
    try:
        check_dst = os.path.exists(dst_file_name)
        a = 0
        src_file = os.open(src_file_name, os.O_RDONLY)
        a = 1
        dst_file = os.open(dst_file_name, os.O_RDWR | os.O_CREAT)
        read_src = os.read(src_file, os.stat(src_file).st_size)
        read_dst = os.read(dst_file, os.stat(dst_file).st_size)
        if check_dst and check_option(read_src, read_dst, dst_file_name):
                return
        else:
            keep_links(src_file_name, dst_file_name)
            longest_common_sub(src_file_name, dst_file_name, read_src,
                               read_dst, src_file, dst_file)
            os.close(src_file)
            os.close(dst_file)
            keep_permission(dst_file_name)
            keep_time(dst_file_name)
    except PermissionError:
        if args.recursive and a == 1:
            os.unlink(dst_file_name)
            main(src_file_name, dst_file_name)
        else:
            if a == 0:
                path = os.getcwd() + '/' + src_file_name
            else:
                path = os.getcwd() + '/' + dst_file_name
            print('rsync: send_files failed to open "%s":\
 Permission denied (13)' % path)


"""-----------------------------CHECK-FILE----------------------------"""


def check_file(src_file_name, dst_file_name):
    path = os.path
    if path.isfile(filesrc):
        if path.isdir(dst_file_name) or dst_file_name[-1] == '/':
            if not path.exists(dst_file_name):
                os.mkdir(dst_file_name)
            dst_path = dst_file_name + "/" + src_file_name
            main(filesrc, dst_path)
        else:
            main(filesrc, dst_file_name)
    elif path.isdir(filesrc):
        print('skipping directory %s' % (filesrc))
    else:
        src_path = os.getcwd() + '/' + src_file_name
        print('rsync: link_stat \"%s" failed: \
No such file or directory (2)' % src_path)


def find_all_path(src_file_name):
    all_paths = os.listdir(src_file_name)
    for path in all_paths:
        path = src_file_name + '/' + path
        if os.path.isfile(path):
            path_list.append(path)
        elif os.path.isdir(path):
            path_list.append(path)
            find_all_path(path)


def change_des_path(filesrc):
    turn_path_list = filesrc.split('/')[1:]
    filesrc = '/'.join(turn_path_list)
    return filesrc


if __name__ == '__main__':
    args = take_args()
    if args.recursive and os.path.isdir(args.src[0]) and\
       not os.path.isfile(args.dst):
            if not os.path.exists(args.dst):
                os.mkdir(args.dst)
            src_file_name = args.src[0]
            dst_file_name = args.dst
            path_list = []
            find_all_path(args.src[0])
            if not os.path.exists(dst_file_name + '/' + src_file_name) and\
               src_file_name[-1] != '/':
                os.mkdir(dst_file_name + '/' + src_file_name)
            for filesrc in path_list:
                if src_file_name[-1] != '/':
                    new_path = dst_file_name + '/' + filesrc
                else:
                    new_path = dst_file_name + '/' + change_des_path(filesrc)
                if os.path.isdir(filesrc) and not os.path.isdir(new_path):
                    os.mkdir(new_path)
                elif os.path.isfile(filesrc):
                    check_file(filesrc, new_path)
    else:
        if len(args.src) > 1 and os.path.isdir(args.dst) or len(args.src) == 1:
            for filesrc in args.src:
                src_file_name, dst_file_name = file_path(filesrc, args.dst)
                check_file(src_file_name, args.dst)
        else:
            print('ERROR: destination must be a directory when\
     copying more than 1 file')
