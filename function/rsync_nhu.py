#!/usr/bin/env python3
# set interpreter


from argparse import ArgumentParser
import hashlib
import os


def handle_args():
    global rsync, current_path
    rsync = ArgumentParser(usage='./rsync.py [OPTIONS] SRC_FILE DESTINATION',
                           description='rsync by Mandy so cute! HAVE FUN!')
    rsync.add_argument("times",
                       help="preserve modification times",
                       action="store_true")
    rsync.add_argument("perms",
                       help="preserve permissions",
                       action="store_true")
    rsync.add_argument("links",
                       help="copy symlinks as symlinks",
                       action="store_true")
    rsync.add_argument("hard-links",
                       help="preserve hard links",
                       action="store_true")
    rsync.add_argument("-c",
                       "--checksum",
                       help="skip based on checksum, not mod-time & size",
                       action="store_true")
    rsync.add_argument("-u",
                       "--update",
                       help="skip files that are newer on the receiver",
                       action="store_true")
    rsync.add_argument('source', type=str, help="SOURCE FILE")
    rsync.add_argument('destination', type=str, help="DESTINATION FILE")
    current_path = os.getcwd()
    args, unknown = rsync.parse_known_args()
    return [args.source, args.destination,
            args.checksum, args.update]


def keep_symlink(src, des):  # -l preserve symlink
    if os.path.islink(src):
        src_link = os.readlink(src)
        os.symlink(src_link, des)


def keep_hardlink(src, des):  # -H preserve hardlink
    if os.stat(src).st_nlink >= 2:
        if os.path.isdir(des):
            des = des + "/" + os.path.basename(src)
        if os.path.isfile(des):
            os.unlink(des)
        os.link(src, des)


def set_default(source, destination):
    info_source = os.stat(source)
    info_destination = os.stat(destination)
    os.chmod(destination, info_source.st_mode)  # -p
    os.utime(destination, (info_source.st_atime, info_source.st_mtime))  # -t


def copy_content(source, destination):
    src = os.open(source, os.O_RDONLY)
    des = os.open(destination, os.O_CREAT | os.O_RDWR)
    data_src = os.read(src, 50)
    while data_src != b"":
        os.write(des, data_src)
        data_src = os.read(src, 50)
    os.close(src)
    os.close(des)


def handle_path(des):
    top = os.path.split(des)[0].split('/')[::-1]
    pth = ""
    while top:
        pth = os.path.join(pth, top.pop())
        if not os.path.exists(pth):
            os.mkdir(pth)


def check_sum(src, des):
    size_des = os.stat(des).st_size
    size_src = os.stat(src).st_size
    des = os.open(des, os.O_RDONLY)
    md5_des = hashlib.md5(os.read(des, size_des)).hexdigest()
    src = os.open(src, os.O_RDONLY)
    md5_src = hashlib.md5(os.read(src, size_src)).hexdigest()
    os.close(src)
    os.close(des)
    return md5_src == md5_des


def is_DES_bigger(src, des):
    size_des = os.stat(des).st_size
    size_src = os.stat(src).st_size
    return size_des > size_src


def is_DES_newer(src, des):
    mtime_src = os.stat(src).st_mtime
    mtime_des = os.stat(des).st_mtime
    return mtime_src < mtime_des


def is_diff_mtime_size(src, des):
    mtime_des = os.stat(des).st_mtime
    size_des = os.stat(des).st_size
    mtime_src = os.stat(src).st_mtime
    size_src = os.stat(src).st_size
    return mtime_src != mtime_des or size_des != size_src


def is_different(src, des, checksum, update):
    if checksum:
        return not check_sum(src, des)
    return (not (update and is_DES_newer(src, des))
            and is_diff_mtime_size(src, des))


def rsync_by_mine(src, dest):
    if is_DES_bigger(src, dest):
        os.unlink(dest)
        copy_content(src, dest)
    else:
        miss_text = ""
        size_des = os.stat(dest).st_size
        size_src = os.stat(src).st_size
        des = os.open(dest, os.O_RDWR)
        des_miss = os.open(dest, os.O_RDWR | os.O_APPEND)
        src = os.open(src, os.O_RDONLY)
        data_des = os.read(des, size_des).decode()
        data_src = os.read(src, size_src).decode()
        diff = {i: data_src[i] for i in range(
            len(data_des)) if data_des[i] != data_src[i]}
        for key in diff.keys():
            os.lseek(des, key, 0)
            os.write(des, str.encode(diff[key]))

        if len(data_src) > len(data_des):
            miss_text = data_src[len(data_des):]
        if miss_text:
            os.write(des_miss, str.encode(miss_text))
        os.close(src)
        os.close(des)
        os.close(des_miss)


def main():
    try:
        args = handle_args()
        src = args[0]
        des = args[1]
        option_checksum = args[2]
        option_update = args[3]
        if not os.path.isfile(des) or not os.path.isdir(des):
            if '/' in des:
                handle_path(des)
        if os.path.isdir(src):
            print("skipping directory .")
        elif not os.path.isfile(src):
            print("rsync: link_stat \"" + current_path + "/" + src +
                  "\" failed: No such file or directory (2)")
        else:
            keep_hardlink(src, des)
            keep_symlink(src, des)
            if not os.path.exists(des):
                copy_content(src, des)
            elif os.path.isdir(des):
                name_des = des + "/" + os.path.basename(src)
                copy_content(src, name_des)
            else:
                pass
                update = is_different(src, des, option_checksum, option_update)
                if update:
                    rsync_by_mine(src, des)
            set_default(src, des)
    except PermissionError:
        print("rsync: send_files failed to open \"" +
              os.path.join(current_path, src) +
              "\": Permission denied (13)")


main()
