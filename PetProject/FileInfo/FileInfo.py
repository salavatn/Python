from typing import List, Dict, Tuple, Optional, Union, Any
import datetime
import socket
import os
import hashlib
import mimetypes

"""
Description:
    This is script get file path and return File Information
    Refactored: 2023-05-08
"""

class GetInfo:
    """
    This class get file path and return file info
    :param filepath: str
    """

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.file     = os.stat(filepath)

    def get_size(self) -> Dict[str, Union[int, float]]:
        '''Get the file size in bytes, kilobytes, megabytes and gigabytes.
        :return: A dictionary containing the file size in B, KB, MB and GB.
        '''

        bytes     = self.file.st_size
        kilobytes = round(bytes / 1024, 3)
        megabytes = round(kilobytes / 1024, 3)
        gigabytes = round(megabytes / 1024, 3)

        result = {
            "Size Bytes": bytes,
            "Size Kilobytes": kilobytes,
            "Size Megabytes": megabytes,
            "Size Gigabytes": gigabytes
            }

        return result

    def get_hash(self) -> Dict[str, str]:
        '''Calculate and return the MD5 hash of the file.
        :return: The MD5 hash as a string.
        '''

        with open(self.filepath, 'rb') as file:
            md5_hash = hashlib.md5(file.read()).hexdigest()
        result = {"MD5 Hash": str(md5_hash)}

        return result

    def get_datetime(self) -> Dict[str, str]:
        '''Get the file creation, modification and access times.
        :return: A dictionary containing the Created, Modified, Accessed times.
        '''
        created  = datetime.datetime.fromtimestamp(self.file.st_birthtime)
        modified = datetime.datetime.fromtimestamp(self.file.st_mtime)
        accessed = datetime.datetime.fromtimestamp(self.file.st_atime)

        result = {
            "File Created":  str(created),
            "File Modified": str(modified),
            "File Accessed": str(accessed)
            }
        return result
    
    def get_filetype(self) -> Dict[str, str]:
        '''Get the File/Mime Type.
        :return: A string containing the file type.
        '''
        file_type = os.path.splitext(self.filepath)[1]
        mime_type = mimetypes.guess_type(self.filepath)[0]

        result = {
            "Mime Type": str(mime_type),
            "File Type": str(file_type)}

        return result

    def get_host_info(self) -> Dict[str, str]:
        '''Get the host information.
        :return: A dictionary containing the host information.
        '''
        fqdn    = socket.getfqdn()
        ipaddr  = socket.gethostbyname(fqdn)

        result = {
            "FQDN": fqdn,
            "IP Address": ipaddr
            }
        return result
    
