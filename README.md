# Космический Инстаграм

 Учебный проект. Проект учит 
 * По API описанию интернет ресурсов находит в этих ресурсах конкретные файлы
 * Конкретный файлы по url crfxbdfnm yf kjrfkmysq lbcr
 * С помощью специального бота размещать локальные файлы в Инстаграм


### Как установить

 Для размещения файлов в Instagram надо иметь логин и пароль.
Логин и пароль инстаграмм необходимо поместить в файл .env
Файл .env должен содержать две строки :
INTGR_LOGIN=<ВашЛогин>
INTGR_PASSWD=<ВашПароль>

проект написан на языке python  3 и состоит из файлов
`main.py`            - содержит основной модуль программы
`fetch_hubble.py - содержит get обращения 
к ресурсу = http://hubblesite.org/api/v3   Телескоп Hubble 

`fetch_spacex.py` содержит get обращения запуска SpaceX
к ресурсу https://api.spacexdata.com/v3

`load_image.py` содержит модуль для счтывания файла из интернет ресурса в файл на диске.

`requirements.txt`  стандартный файл зависимостей для установки  pethon окружения

`.env` Описывает среду выполнения. Файл содержил логин и пароль для инстаграмма


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
pip install -r requirements.txt




### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
Проект  учит получать файлы из интернет ресурсов и далее размещеть файлы в Instagram