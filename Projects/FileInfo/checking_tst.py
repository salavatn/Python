# import os


# properties = os.stat('app/fileinfo.py')

# print(f'Original data:\n{properties}\n')
# # os.stat_result(st_mode=33188, st_ino=996505, st_dev=16777231, st_nlink=1, st_uid=501, st_gid=20, st_size=2596, st_atime=1686731650, st_mtime=1686731650, st_ctime=1686731650)


# from unittest.mock import MagicMock, patch

# # Create a mock for os.stat
# mock_stat_result = os.stat_result((
#     33188,      # st_mode
#     996505,     # st_ino
#     16777231,   # st_dev
#     1,          # st_nlink
#     501,        # st_uid
#     20,         # st_gid
#     2596,       # st_size
#     1686731650, # st_atime
#     1686731650, # st_mtime
#     1686731650  # st_ctime
# ))

# mock_stat_result = os.stat_result((
#     33188,      # st_mode
#     996505,     # st_ino
#     16777231,   # st_dev
#     1,          # st_nlink
#     501,        # st_uid
#     20,         # st_gid
#     2596,       # st_size
#     1686731650, # st_atime
#     1686731650, # st_mtime
#     1686731650  # st_ctime
# ))

# # Test Size:
# data = [33188, 996505, 16777231, 1, 501, 20, 0, 1686731650, 1686731650, 1686731650]
# data = [33188, 996505, 16777231, 1, 501, 20, 1023, 1686731650, 1686731650, 1686731650]
# data = [33188, 996505, 16777231, 1, 501, 20, 1024, 1686731650, 1686731650, 1686731650]
# data = [33188, 996505, 16777231, 1, 501, 20, 4123168604160, 1686731650, 1686731650, 1686731650]
# mock_stat_result = os.stat_result((*data,))


# mock_stat = MagicMock(return_value=mock_stat_result)
# print(f'Mock data:\n{mock_stat}\n')
# # Use the mocked os.stat
# with patch('os.stat', new=mock_stat):
#     result = os.stat('path/to/file')
#     print(f'Result:\n{result}\n')

# # print(result)




from unittest.mock import MagicMock, patch
import os

path = '/Users/salavat/GitHub/Python/PetProject/FileInfo/app/fileinfo.py'
path = '/Users/salavat/GitHub/Python/PetProject/FileInfo/app/'
result = os.path.isfile(path)
print(f'Path to File? {result}')


# Create a mock for os.path functions
mock_isfile = MagicMock(return_value='path/to/fake/file.txt')
with patch('os.path.isfile', new=mock_isfile):
    result1 = os.path.isfile('path/to/file/that/does/not/exist')

print(result1)  # Output: True


# mock_isfile = MagicMock(return_value=True)


# mock_isdir  = MagicMock(return_value=False)

# # Patch the os.path functions
# with patch('os.path.isfile', new=mock_isfile), patch('os.path.isdir', new=mock_isdir):
#     result1 = os.path.isfile('path/to/file')
#     result2 = os.path.isdir('path/to/directory')

# print(result1)  # Output: True
# print(result2)  # Output: False
