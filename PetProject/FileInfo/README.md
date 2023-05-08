
# Get File Info


- [Get File Info](#get-file-info)
  - [Description](#description)
  - [Requirements](#requirements)
  - [How to use](#how-to-use)
  - [Example: Show in Table](#example-show-in-table)
  - [Example: Show in JSON](#example-show-in-json)



---

## Description

Get file information such as:
  - size, 
  - creation, modification and access times, 
  - file type, MD5 hash, 
  - host information.

---

## Requirements
- Python 3.6+
- Install requirements

```shell
pip install -r requirements.txt
```

---
## How to use
1. Show info in table
```python
python main.py <file> -t
```


2. Show info in json
```python
python main.py <file> -j
```

---

## Example: Show in Table
```python
python main.py '/Users/salavat/Downloads/eTicket.pdf' -t 
```

**Output:**
```
  Title          Value                                 
 ───────────────────────────────────────────────────── 
  File Path      /Users/salavat/Downloads/eTicket.pdf  
  Size Bytes     42536                                 
  Size KB        41.539                                
  Size MB        0.041                                 
  Size GB        0.0                                   
  Created        2023-05-03 19:58:02.292746            
  Modified       2023-05-03 19:58:02.293103            
  Accessed       2023-05-05 18:26:55.862897            
  Extension      .pdf                                  
  Mime Type      application/pdf                       
  MD5 Hash       57acb200b179afc2be02b77336cad041      
  FQDN           salavat.home                          
  IP Address     192.168.1.33    
```

---

## Example: Show in JSON
```python
python main.py '/Users/salavat/Downloads/eTicket.pdf' -j
```

**Output:**
```
{'File Created': '2023-05-03 19:58:02.292746', 'File Modified': '2023-05-03 19:58:02.293103', 'File Accessed': '2023-05-05 18:26:55.862897'}
{'Size Bytes': 42536, 'Size Kilobytes': 41.539, 'Size Megabytes': 0.041, 'Size Gigabytes': 0.0}
{'Mime Type': 'application/pdf', 'File Type': '.pdf'}
{'MD5 Hash': '57acb200b179afc2be02b77336cad041'}
{'FQDN': 'salavat.home', 'IP Address': '192.168.1.33'}
```
