import os

filename = 'example.txt'
uid = 1000  # new user ID
gid = 1000  # new group ID

# get current owner and group ID of the file
stat_info = os.stat(filename)
current_uid = stat_info.st_uid
current_gid = stat_info.st_gid

# change owner and group ID of the file
os.chown(filename, uid, gid)

# check that owner and group ID have been changed
stat_info = os.stat(filename)
if stat_info.st_uid == uid and stat_info.st_gid == gid:
    print(f'Owner and group ID of {filename} have been changed to {uid}:{gid}')
else:
    print(f'Error: failed to change owner and group ID of {filename}')
