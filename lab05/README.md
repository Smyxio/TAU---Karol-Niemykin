# Sentry

## Krótko o tym czym jest:
Sentry jest narzędziem do śledzenia błędów kompatybilnym z popularnymi językami skryptowymi i ich frameworkami webowymi. Posiada między innymi następujące funkcje:

**Slack trace** – pokazuje kod źródłowy w Slack Trace, co oznacza, że nie musisz przekopywać się przez wersy kodów i wyszukiwać je samodzielnie.

***Local Stack*** – łatwiej jest debugować błąd, jeśli znasz wartość zmiennych. Funkcja lokalnych Stacków wykazuje wartości lokalnych zmiennych, ułatwiając tym samym debugowanie błędów.

***Kontekst środowiskowy*** – Sentry pomaga deweloperom filtrować komunikaty, zagadnienia i feedback od użytkowników ze środowiska. Narzędzie oferuje rozwijaną listę środowiskową, a deweloper ma możliwość wyświetlać dane dot. zagadnień, dane o komunikatach i feedback ze środowiska.

Oczywiście nie są to wszystkie funckje ,ale nie chce podczas tej krótkiej prezentacji nikogo zanudzać wklejaniem zbyt dużej ilości tekstu dlatego po więcej szczegółów
zapraszam na oficjalną strone:
[Sentry](https://choosealicense.com/licenses/mit/)

## Jak zainstalować Sentry?
Ten przykład pokazuje jak zainstalować i skonfigurować sentry w python django framework na systemie operacyjnym Ubuntu

##### Utwórz użytkownika sentry
```
adduser sentry
```
##### Utwórz bazę danych sentry
```
CREATE USER sentry WITH PASSWORD 'xxx'
CREATE DATABASE sentry;
GRANT ALL PRIVILEGES ON DATABASE sentry TO sentry;
```
#### Zainstaluj virtualenvwrapper
```
sudo apt-get install virtualenvwrapper
```
#### Zainstaluj virtualenvwrapper
```
sudo apt-get install virtualenvwrapper
```
#### Zaloguj się jako użytkownik sentry
```
sudo su sentry
```
#### Dodaj virtualenvwrapper do pliku .bashrc.
```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
#### Załaduj ponownie plik .bashrc.
```
source ~/.bashrc
```
#### Utwórz wirtualne środowisko
```
mkvirtualenv sentry
```
#### Zainstaluj sentry
```
pip install sentry
```
#### Utwórz plik konfiguracyjny sentry
```
sentry init
```
#### Dodaj konfiguracje bazy do /.sentry/sentry.conf.py
```
'default': {
  'ENGINE': 'sentry.db.postgres',
  'NAME': 'sentry',
  'USER': 'sentry',
  'PASSWORD': 'xxx',
  'HOST': '127.0.0.1',
  'PORT': '5432',
}
```
#### Załaduj wprowadzone zmiany
```
sentry upgrade
```
#### Utwórz plik startowe sentry w  /etc/init/
```
# sentry.conf
description "Sentry"

pre-start script
  mkdir -p /var/log/sentry
  chown -R sentry /var/log/sentry
end script

start on runlevel [2345]
stop on runlevel [016]

#sentry-web.conf

description "Sentry Web"

start on started sentry
stop on stopping sentry

respawn limit 10 5
chdir /home/sentry
setuid sentry

env VIRTUAL_ENV=/home/sentry/.virtualenvs/sentry/
env PYTHONUNBUFFERED=True
env SENTRY_CONF=/home/sentry/.sentry/sentry.conf.py

exec $VIRTUAL_ENV/bin/sentry start >> /var/log/sentry/web.log 2>&1

#sentry-celery.conf

description "Sentry Celery"

start on started sentry
stop on stopping sentry

respawn limit 10 5
chdir /home/sentry
setuid sentry

env VIRTUAL_ENV=/home/sentry/.virtualenvs/sentry/
env PYTHONUNBUFFERED=True
env SENTRY_CONF=/home/sentry/.sentry/sentry.conf.py

exec $VIRTUAL_ENV/bin/sentry celery worker -B --loglevel=info >> /var/log/sentry/celery.log
```

#### Uruchom sentry
```
start sentry
```

### Od teraz usługa jest dostępna na localhost:9000

# I to by było na tyle :)