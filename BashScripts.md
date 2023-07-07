# Bash Scripts

## Скрипт используемые для отправки писем с вложениями:
```bash
#!/bin/bash
for i in `ls -dt /tmp/malware-samples/*`;
  do
    echo "Do not download attachment!!!" | mailx -v \
    -r "deadpool@example.org" \
    -s "Test Send Malware Files" \
    -S smtp="172.31.0.7" \
    -a $i \
    tmuller@ns-lab.com
  done
```

---

## Websense WSBackup Scripts
```bash
#!/bin/bash

mkdir /var/WSBackup/
cd /opt/Websense/
./WebsenseTools -b -b -d /var/WSBackup/
echo; echo "Create WSBackup stated: $(date)" >> /var/WSBackup/WSBackup_status.txt; echo
```

Описание скрипта
1. создать каталог /var/WSBackup
2. Перейти в каталог /opt/Websense/
3. Запустить утилиту WebsenseTools.
  3.1. C опцией WebsenseTools -b это тоже самое что и wsbackup
  3.2. Вторая опция WebsenseTools -b -b - это запуск к backup, аналог wsbackup -b
4. "Create WSBackup stated: $(date)" - Сделать своего рода отчет в текстовый файл
​
​crontab:​
```sh
​10 19 * * * /home/user_websense/scripts/wsbackup.sh​
```

---

## Получить Category Name на основе URL адресов

1. Подключаемся на веб-шлюз, где установлены службы фильтрации
2. Сохраняем содержимое script.txt как скрипт в каталог /home/script.sh
3. Выполнить команду chmod +x /home/script.sh
4. Сохарняем список URL адресов в /home/URL.txt
5. Запускаем скрипт указав текстовый файл с адресами /home/script.sh URL.txt


```bash
#!/bin/bash

Number=0
LastURL=$(grep -v "^$" $1 | tail -n 1)
LastNumber=$(grep -v "^$" $1 | cat -n |  grep "$LastURL"  | awk '{print $1}')

# Welcome
echo;
echo "+--------------------------------------------+"
echo "|   Delete http(s) prefix from addresses     |"
echo "+--------------------------------------------+"
echo;

sleep 1;


mkdir /home/Websense
rm -fr /home/Websense/URL-for-script.txt
touch /home/Websense/URL-for-script.txt
cat $1 | sed 's/https:\/\// /g' | sed 's/http:\/\// /g'  > /home/Websense/URL-for-script.txt




echo;
echo "+--------------------------------------------+"
echo "|         Count of URL is $LastNumber                  |"
echo "+--------------------------------------------+"
echo;

sleep 1




for (( i=1; i <= $LastNumber; i++ ))
do
        Number=$[$Number + 1]
        MyURL=$(grep -v "^$" '/home/Websense/URL-for-script.txt'| cat  -n | grep -w $Number | awk '{print $2}')
        Category=$(/opt/Websense/WebsenseTools -p -url $MyURL -m 18 | grep -w "Category =" |  awk '{for(i=1;i<3;i++) $i="";print}')

        StringAll="$MyURL  -  $Category"
        echo $StringAll >> /home/Websense/URL-Categories.txt
        echo "      search for $MyURL "

#       sleep 0.05
#       leep 1

done

echo
echo "+------------------------------------------------+"
echo "|   Finish! You can use next command fo view:    |"
echo "|   less /home/Websense/URL-Categories.txt       |"
echo "+------------------------------------------------+"
echo
```

```
www.obrnadzor.gov.ru - Government
stat.edu.ru - Educational Institutions
www.nica.ru - Government
www.lexed.ru - Educational Institutions
www.ru - Search Engines and Portals
www.edu.ru - Educational Institutions
ege.edu.ru - Educational Institutions
www.ecsocman.edu.ru - Educational Institutions
www.law.edu.ru - Educational Institutions
www.ict.edu.ru - Educational Institutions
www.monrb.ru - Uncategorized
minedu.karelia.ru - Search Engines and Portals
www.stavminobr.ru - Government
```

---
##  Scripts for download malware samples
```bash
#!/bin/bash

mkdir /tmp/samples/

wget "http://malshare.com/api.php?api_key=1d59302e8e4cd8263c8373c36eddb6752fc1a9a5a3cdfa581c1330b18ca5e4a7&action=getsourcesraw" -O /tmp/malware.txt

http_proxy=172.31.0.6:8080 wget -i /tmp/malware.txt -P /tmp/samples/ --proxy-user=user1 --proxy-password=qaz123Z
```

---
Scripts for fishtank samples
```bash
mkdir /tmp/samples/
cd /tmp/samples/

wget http://data.phishtank.com/data/online-valid.csv

awk -F "\"*,\"*" '{print $2}' online-valid.csv > phishtank.txt

http_proxy=10.0.0.101:8080 wget -i /tmp/samples/phishtank.txt -P /tmp/samples/
```

## Combo Scripts for Websense
### 1 Script for WEB
- Скачивание malware без сохранения файла на диск
- file: web-download-malware.sh

```bash
#!/bin/bash
wget "http://malshare.com/api.php?api_key=1d59302e8e4cd8263c8373c36eddb6752fc1a9a5a3cdfa581c1330b18ca5e4a7&action=getsourcesraw" \
	-nv \
	-O /tmp/malware-URLs.txt
http_proxy=172.31.0.6:8080 \
	wget -nv \
	-i /tmp/malware-URLs.txt \
	--delete-after \
	--proxy-user=administrator \
	--proxy-password=Pa$$w0rd
```



### 2 Scripts for EMAIL
- Отправка писем на внутренний домен с malware 
- file: email-config.sh 😨

```bash
#!/bin/bash
echo "Sending malware from outside" | mailx \
	-s "malware sample" \
	-S smtp="172.31.0.7" \
	-r "neo@example.org" \
	-a $1 \
	tmuller@ns-lab.com
echo Sending File:   $1
sleep 0.1
```


- file: email-send-malware.sh 😰
```bash
#!/bin/bash
DATE=$(date '+%Y-%m-%d')
ls -d /tmp/malware-samples_$DATE/* | xargs -L 1 ./email-config.sh
```


### 3 Save malware
- Скачивать без проксирования malware, ежедневно сохраняя в новую папку по датам
- file: download-malware.sh 😵
```bash
#!/bin/bash
DATE=$(date '+%Y-%m-%d')
echo Create directory /tmp/malware-samples_$DATE
mkdir /tmp/malware-samples_$DATE
wget "http://malshare.com/api.php?api_key=1d59302e8e4cd8263c8373c36eddb6752fc1a9a5a3cdfa581c1330b18ca5e4a7&action=getsourcesraw" \
	-O /tmp/malware-URLs.txt \
	-nv
wget -i /tmp/malware-URLs.txt \
	-nv \
	-P /tmp/malware-samples_$DATE/
```
