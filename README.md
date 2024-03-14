# 2024-dj5ecom-francis
Membuat aplikasi eccommerce menggunakan django versi 5
Github: https://github.com/gurnitha/2024-dj5ecom-francis


## 1. SETUP

#### 1. Inisial setup - clone remote repositori


#### 2. Create venv, install django, upgrade pip


#### 3. Create venv, install django, upgrade pip



## 2. PROYEK DJANGO


#### 1. Membuat proyek django dengan nama config

        modified:   README.md
        new file:   config/config/__init__.py
        new file:   config/config/asgi.py
        new file:   config/config/settings.py
        new file:   config/config/urls.py
        new file:   config/config/wsgi.py
        new file:   config/manage.py


#### 2. Merubh struktur proyek

        modified:   README.md
        renamed:    config/config/__init__.py -> config/__init__.py
        renamed:    config/config/asgi.py -> config/asgi.py
        renamed:    config/config/settings.py -> config/settings.py
        renamed:    config/config/urls.py -> config/urls.py
        renamed:    config/config/wsgi.py -> config/wsgi.py
        renamed:    config/manage.py -> manage.py
        deleted:    venv312503/Scripts/Activate.ps1
        deleted:    venv312503/Scripts/activate
        deleted:    venv312503/Scripts/activate.bat
        deleted:    venv312503/Scripts/deactivate.bat
        deleted:    venv312503/Scripts/django-admin.exe
        deleted:    venv312503/Scripts/pip.exe
        deleted:    venv312503/Scripts/pip3.12.exe
        deleted:    venv312503/Scripts/pip3.exe
        deleted:    venv312503/Scripts/python.exe
        deleted:    venv312503/Scripts/pythonw.exe
        deleted:    venv312503/Scripts/sqlformat.exe
        deleted:    venv312503/pyvenv.cfg



## 3. APP DJANGO


#### 1. Membuat app 'shop' di dalam folder app

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5ecom-francis\src(main -> origin)
        (francis) λ REM: Membuat app 'shop' di dalam folder app

        (francis) λ mkdir app\shop

        (francis) λ django-admin startapp shop app\shop

        (francis) λ ls
        app/  config/  manage.py*  README.md

        (francis) λ tree app/shop /f
        Folder PATH listing
        Volume serial number is C0000100 1A60:D2FA
        C:\USERS\ING\DESKTOP\2024-DEVSPACE\2024-DJ5ECOM-FRANCIS\SRC\APP\SHOP
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   views.py
        │   __init__.py
        │
        └───migrations
                __init__.py

        modified:   README.md
        new file:   app/shop/__init__.py
        new file:   app/shop/admin.py
        new file:   app/shop/apps.py
        new file:   app/shop/migrations/__init__.py
        new file:   app/shop/models.py
        new file:   app/shop/tests.py
        new file:   app/shop/views.py


#### 2. Register app 'shop' pada config/settings.py

        modified:   README.md
        modified:   app/shop/apps.py
        modified:   config/settings.py



## 4. URLS, VIEWS, TEMPLATES


#### 1. Hallo World dari ulrs dan views

        modified:   README.md
        new file:   app/shop/urls.py
        modified:   app/shop/views.py
        modified:   config/urls.py


#### 2. Mengaktifkan django templates

        modified:   README.md
        modified:   config/settings.py


#### 3. Membuat home page menampilkan Hallo World menggunakan ulrs, views dan templates

        modified:   README.md
        modified:   app/shop/views.py
        new file:   templates/shop/index.html


#### 4. Menggunakan template inheritance pada home page

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/shop/index.html


#### 5. Mengisi html template pada home page

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/partials/footer.html
        new file:   templates/partials/header.html
        modified:   templates/shop/index.html


#### 6. Membuat path untuk static files

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py


#### 7. Add dan load static files

        new file:   static/assets/images/products/shorts/short_9/5.webp
        ...
        modified:   templates/partials/header.html
        modified:   templates/shop/index.html



## 5. DATABASE


#### 1. Create MySQL database

        mysql> show databases;
        ...

        mysql> CREATE DATABASE 2024_djecom_francis;
        Query OK, 1 row affected (0.09 sec)

        mysql> USE 2024_djecom_francis;
        Database changed


#### 2. Connect database with the project

        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'xx',
            'USER': 'root',
            'PASSWORD': 'xx',
            'HOST':'localhost',
            'PORT':'3306',
            }
        }

        (francis) λ pip install mysqlclient
        ...
        Successfully installed mysqlclient-2.2.4

        (francis) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   config/settings.py
