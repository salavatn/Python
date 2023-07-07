from typing import List, Dict, Union, Any
from app.config import logger
import hashlib, mimetypes, math
import datetime, socket, os

logger("fileinfo.py")

class FileInfo:
    def __init__(self, filepath: str) -> None:
        exist_file = os.path.isfile(filepath)
        if not exist_file:
            logger.error(f"File not found: {filepath}")
            exit(1)
        self.filepath = filepath


    def collect_data(self) -> Dict[str, Any]:
        '''Collect file data'''
        log_head = "Collect:"

        properties = os.stat(self.filepath)

        file_name = os.path.basename(self.filepath)
        file_size = self.size(properties.st_size)


    
    def get_datetime(self, properties) -> Dict[str, str]:
        '''Get the file creation, modification and access times'''
        log_head = "DateTime:"

        created  = datetime.datetime.fromtimestamp(properties.st_birthtime)
        modified = datetime.datetime.fromtimestamp(properties.st_mtime)
        accessed = datetime.datetime.fromtimestamp(properties.st_atime)

        result = {
            "File Created":  created.strftime("%Y-%m-%d %H:%M:%S"),
            "File Modified": modified.strftime("%Y-%m-%d %H:%M:%S"),
            "File Accessed": accessed.strftime("%Y-%m-%d %H:%M:%S")
            }
        
        logger.debug(f"{log_head} created  at {created}")
        logger.debug(f"{log_head} modified at {modified}")
        logger.debug(f"{log_head} accessed at {accessed}")

        return result
    
    def get_info(self, properties) -> Dict[str, Any]:
        '''Get the file information.'''
        log_head = "Get:"

        # Part 1: Get file properties
        # properties  = os.stat(self.filepath)

        # Part 2: Collect file info
        file_name   = os.path.basename(self.filepath)
        file_size   = self.size(properties.st_size)
        created     = datetime.datetime.fromtimestamp(properties.st_birthtime).strftime("%Y-%m-%d %H:%M:%S")
        modified    = datetime.datetime.fromtimestamp(properties.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        accessed    = datetime.datetime.fromtimestamp(properties.st_atime).strftime("%Y-%m-%d %H:%M:%S")
        file_type   = mimetypes.guess_type(self.filepath)[0]
        mime_type   = os.path.splitext(self.filepath)[1][1:].upper()
        file_hash   = hashlib.md5(open(self.filepath, 'rb').read()).hexdigest()
        logger.debug(f"{log_head} file_name: {file_name}, size {file_size}, type {file_type}, mime {mime_type}")
        logger.debug(f"{log_head} created {created}, modified {modified}, accessed {accessed}")
        logger.debug(f"{log_head} hash: {file_hash};")

        # Part 3: Return file info
        result = {
            "File Name":     file_name,
            "File Size":     file_size,
            "File Type":     file_type,
            'File Mime':     mime_type,
            "File Created":  created,
            "File Modified": modified,
            "File Accessed": accessed,
            "File Hash":     file_hash,
            }
        
        return result
        

    def size(self, bytes) -> str:
        '''Get the file size in bytes, kilobytes, megabytes and gigabytes'''
        log_head = "Size:"

        # Part-1: Check "bytes" - type or equal to 0? 
        if type(bytes) != int or bytes < 0:
            logger.error(f"{log_head} bytes is not int")
            return False
        elif bytes == 0:
            logger.debug(f"{log_head} 0 bytes")
            return '0  B'
        
        units = ['B', 'KB', 'MB', 'GB', 'TB']
        index = int(math.floor(math.log(bytes, 1024)))
        size = round(bytes / (1024 ** index), 2)
        unit = units[index]
        result = f'{size} {unit}'
        logger.debug(f"{log_head} from {bytes} bytes to  {result}")

        return result


# info = FileInfo('/Users/salavat/Downloads/MVI_6533.AVI')
# info.get()


