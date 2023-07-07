from app.fileinfo import FileInfo
from unittest.mock import MagicMock, patch
import os 


mock_isfile = MagicMock(return_value='path/to/fake/file.txt')
with patch('os.path.isfile', new=)