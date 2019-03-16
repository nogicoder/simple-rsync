PSEUDO CODE:

#Taking in input from command-line: Options, src, dest
# Take source file path
# Take destination file path
# If source file don't exist -> raise error
# elif source file has no right -> raise error
# elif source file is dir -> raise error
# else:
    # if destination name == source file name:
    #     do nothing
    # if destination name != source file name:
    #     if destination not exist:
    #         if destination is dir: # "/" at the index [-1]
    #             create dir name as DESTINATION
    #             if source file is softlink:
    #                 create inside dir a softlink copy with same name as source file + pointing to the same original file of source file
    #             elif source file is hardlink:
    #                 create inside dir a hardlink copy with same name as source file + inode as the original file of source file
    #             else:
    #                 create inside dir the file copy with same name as source file
    #         if destination is not dir:
    #             if source file is softlink:
    #                 create a softlink copy with same name as source file + pointing to the same original file of source file
    #             elif source file is hardlink:
    #                 create a hardlink copy with same name as source file + inode as the original file of source file
    #             else:
    #                 create a copy with same name as source file
    #     if destination exist:
    #         if destination is dir:
    #             if no file with same source file name inside:
    #                 if source file is softlink:
    #                     create a softlink copy with same name as source file + pointing to the same original file of source file
    #                 elif source file is hardlink:
    #                     create a hardlink copy with same name as source file + inode as the original file of source file
    #                 else:
    #                     create a file copy with same name as source file
    #             elif file_in_dir with same source file name inside:
    #                 if source file is softlink:
    #                     if file_in_dir is softlink:
    #                         if point to the same original file as scr_file:
    #                             do nothing
    #                         if not point to the same original file as scr_file:
    #                             create a softlink copy with same name as source file + pointing to the same original file of source file #auto replace the old softlink file_in_dir
    #                     else: #might be hardlink or normal file
    #                         create a softlink copy with same name as source file + pointing to the same original file of source file #auto replace the file_in_dir
    #                 elif source file is hardlink:
    #                     if file_in_dir is hardlink:
    #                         if have same inode:
    #                             do nothing
    #                         if not have same inode:
    #                             create a hardlink copy with same name as source file + inode as the original file of source file #auto replace the old softlink file_in_dir
    #                     else: #might be softlink or normal file
    #                         create a hardlink copy with same name as source file + inode as the original file of source file #auto replace the file_in_dir
    #                 else:
    #                     **check mode**
            # if destination is file:
            #     if source file is softlink:
            #         if file_in_dir is softlink:
            #             if point to the same original file as scr_file:
            #                 do nothing
            #             if not point to the same original file as scr_file:
            #                 create a softlink copy with same name as source file + pointing to the same original file of source file #auto replace the old softlink file_in_dir
            #         else: #might be hardlink or normal file
            #             create a softlink copy with same name as source file + pointing to the same original file of source file #auto replace the file_in_dir
            #     elif source file is hardlink:
            #         if file_in_dir is hardlink:
            #             if have same inode:
            #                 do nothing
            #             if not have same inode:
            #                 create a hardlink copy with same name as source file + inode as the original file of source file #auto replace the old softlink file_in_dir
            #         else: #might be softlink or normal file
            #             create a hardlink copy with same name as source file + inode as the original file of source file #auto replace the file_in_dir
            #     else:
            #         **check mode**
'''
#**CHECK MODE**
if args.update:
    do stuff
elif args.checksum:
    do stuff
else:
