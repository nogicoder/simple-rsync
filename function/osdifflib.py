import difflib, os


source_size = os.stat("test_source").st_size
dest_size = os.stat("test_dest").st_size

fd_source = os.open("test_source", os.O_RDWR)
fd_dest = os.open("test_dest", os.O_RDWR)

source_content = os.read(fd_source, source_size)
dest_content = os.read(fd_dest, dest_size)

source_list = source_content.decode().splitlines()
dest_list = dest_content.decode().splitlines()

# print(source_list)
# print(dest_list)


diff = difflib.ndiff(dest_list, source_list)
direction = difflib.SequenceMatcher(None, dest_content, source_content).get_opcodes()
print("\n".join(diff))
print(direction)

if source_size >= dest_size:
    for tag, i1, i2, j1, j2 in direction:
        if tag in ['replace', 'insert', 'delete']:
            os.lseek(fd_dest, i1, 0)
            os.write(fd_dest, source_content[j1:])
elif source_size < dest_size:
    for tag, i1, i2, j1, j2 in direction:
        if tag in ['replace', 'insert', 'delete']:
            os.lseek(fd_dest, i1, 0)
            os.write(fd_dest, source_content[j1:])

os.close(fd_dest)
