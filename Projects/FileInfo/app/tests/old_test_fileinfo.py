from unittest.mock import MagicMock, patch
from app.fileinfo import FileInfo
import os



# Create a mock for os.path functions
mock_isfile = MagicMock(return_value='path/to/fake/file.txt')



mock_isfile = MagicMock(return_value=True)


mock_isdir  = MagicMock(return_value=False)

# Patch the os.path functions
with patch('os.path.isfile', new=mock_isfile), patch('os.path.isdir', new=mock_isdir):
    result1 = os.path.isfile('path/to/file')
    result2 = os.path.isdir('path/to/directory')

print(result1)  # Output: True
print(result2)  # Output: False



path = '/your/file/path/MVI_6500.AVI'
info = FileInfo(path)



def test_get_size():
    result   = info.size(2548040)
    expected = "2.43 MB"
    assert result == expected

    result   = info.size(2748779069440)
    expected = "2.5 TB"
    assert result == expected

    result  = info.size(0)
    expected = "0  B"
    assert result == expected

    result   = info.size(-34)
    expected = False
    assert result == expected

    result   = info.size('string')
    expected = False
    assert result == expected

def test_fileinfo_get():
    result  = info.get()
    expected = 'MVI_6533-1.AVI'
    assert expected == result['File Name']


# def test_get_hash():
#     result   = info.get()['File Hash']
#     expected = '6bd41f08615143a3382344ca37ef170e'
#     assert result == expected

#     result   = len(info.get())
#     expected = 32
#     assert result == expected

#     info     = FileInfo()
#     result   = info.get()
#     expected = False
#     assert result == expected

#     result   = info.hash("string")
#     expected = False
#     assert result == expected

# def test_get_type():    
#     result   = convert.type(path)
#     expected = {'Mime Type': 'image/jpeg', 'File Type': 'JPG'}
#     assert result == expected

#     result   = convert.type()
#     expected = False
#     assert result == expected

#     result   = convert.type("string")
#     expected = False
#     assert result == expected

# def test_properties():
#     result      = properties.get()
#     count_keys  = len(result.keys())
#     expected    = 8
#     assert count_keys == expected

#     file_name   = result['File Name']
#     expected    = 'monkey.jpg'
#     assert file_name == expected

#     hash_len    = len(result['MD5 Hash'])
#     expected    = 32
#     assert hash_len == expected

    

