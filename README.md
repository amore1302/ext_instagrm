# Космический Инстаграм

[TODO: Учебный проект. Проект учит разбираться в get запросах к  api ресурсам,
вторая группа get запросов  позволяяет скачивать файлы из двух интернет ресурсов.
Далее с помощью специализированного Бота полученные файлы выкладываются в Instagram
 ]

### Как установить

[TODO: Для размещения файлов в Instagram надо иметь логин и пароль.
Логин и пароль инстаграмм необходимо поместить в файл .env
Файл .env должен содержать две строки :
INTGR_LOGIN=<ВашЛогин>
INTGR_PASSWD=<ВашПароль>

проект написан на языке python  3 и состоит из файлов
main.py            - содержит основной модуль программы
fetch_hubble.py - содержит get обращения 
к ресурсу = http://hubblesite.org/api/v3   Телескоп Hubble 

fetch_spacex.py содержит get обращения запуска SpaceX
к ресурсу https://api.spacexdata.com/v3

load_image.py содержит модуль для счтывания файла из интернет ресурса в файл на диске.

requirements.txt  стандартный файл зависимостей для установки  pethon окружения



Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
pip install -r requirements.txt

 ]


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
Ghjtrn  учит получать файлы из интернет ресурсов и далее размещеть файлы в Instagram