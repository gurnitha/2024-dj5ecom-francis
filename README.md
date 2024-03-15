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


#### 3. Melindungi sensitif file

        new file:   .env-example
        modified:   .gitignore
        modified:   README.md
        modified:   config/settings.py



## 6. DJANGO ADMIN


#### 1. Mengaktifkan django admin

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5ecom-francis\src(main -> origin)
        (francis) λ REM: Mengaktifkan django admin

        (francis) λ python manage.py makemigrations
        No changes detected

        (francis) λ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying sessions.0001_initial... OK

        mysql> SHOW TABLES;
        +-------------------------------+
        | Tables_in_2024_djecom_francis |
        +-------------------------------+
        | auth_group                    |
        | auth_group_permissions        |
        | auth_permission               |
        | auth_user                     |
        | auth_user_groups              |
        | auth_user_user_permissions    |
        | django_admin_log              |
        | django_content_type           |
        | django_migrations             |
        | django_session                |
        +-------------------------------+
        10 rows in set (0.00 sec)


#### 2. Membuat superuser

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5ecom-francis\src(main -> origin)
        (francis) λ REM: Membuat superuser

        (francis) λ python manage.py createsuperuser
        Username (leave blank to use 'ing'): superuser
        Email address: superuser@mail.com
        Password:
        Password (again):
        The password is too similar to the email address.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.



## 7. DJANGO MODEL


#### 1. Membua Slider model dan jalankan migrasi

        C:\Users\ING\Desktop\2024-DEVSPACE\2024-dj5ecom-francis\src(main -> origin)
        (francis) λ python manage.py makemigrations
        Migrations for 'shop':
          app\shop\migrations\0001_initial.py
            - Create model Slider

        (francis) λ python manage.py migrate
        Operations to perform:
          Apply all migrations: admin, auth, contenttypes, sessions, shop
        Running migrations:
          Applying shop.0001_initial... OK

        (francis) λ python manage.py sqlmigrate shop 0001
        --
        -- Create model Slider
        --
        CREATE TABLE `shop_slider` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `title` varchar(60) NOT NULL, 
                `description` varchar(120) NOT NULL, 
                `button_text` varchar(60) NOT NULL, 
                `button_link` varchar(255) NOT NULL, 
                `image` varchar(100) NOT NULL, 
                `created_at` datetime(6) NOT NULL, 
                `updated_at` datetime(6) NOT NULL
        );

        mysql> SHOW TABLES;
        +-------------------------------+
        | Tables_in_2024_djecom_francis |
        +-------------------------------+
        | auth_group                    |
        | auth_group_permissions        |
        | auth_permission               |
        | auth_user                     |
        | auth_user_groups              |
        | auth_user_user_permissions    |
        | django_admin_log              |
        | django_content_type           |
        | django_migrations             |
        | django_session                |
        | shop_slider                   | <---- baru
        +-------------------------------+
        11 rows in set (0.00 sec)



#### 2. Merancang tampilan Slider model pada admain panel dan insert beberapa sliders

        modified:   app/shop/admin.py
        new file:   media/sliders/2024/03/14/banner1.png
        new file:   media/sliders/2024/03/14/banner3.png
        new file:   media/sliders/2024/03/14/banner7.png


#### 3. Load slider dari db dan fetch slider pada home page

        modified:   app/shop/views.py
        modified:   templates/shop/index.html


#### 4. Include slider pada partials

        modified:   README.md
        new file:   templates/partials/slider.html
        modified:   templates/shop/index.html


#### 5. Membua Collection model dan jalankan migrasi

        modified:   README.md
        new file:   app/shop/migrations/0002_collection.py
        modified:   app/shop/models.py

        (francis) λ python manage.py sqlmigrate shop 0002
        --
        -- Create model Collection
        --
        CREATE TABLE `shop_collection` (
                `id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, 
                `title` varchar(60) NOT NULL, 
                `description` varchar(60) NOT NULL, 
                `button_text` varchar(60) NOT NULL, 
                `button_link` varchar(255) NOT NULL, 
                `image` varchar(100) NOT NULL, 
                `created_at` datetime(6) NOT NULL, 
                `updated_at` datetime(6) NOT NULL
        );


#### 6. Merubah struktur proyek: struktur proyek didasarkan pada francis punya

        modified:   .gitignore
        modified:   README.md
        modified:   app/shop/admin.py
        modified:   app/shop/apps.py
        modified:   app/shop/migrations/0001_initial.py
        modified:   app/shop/migrations/0002_collection.py
        deleted:    app/shop/models.py
        modified:   app/shop/urls.py
        deleted:    app/shop/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   databases/categories.json
        new file:   databases/collections.json
        new file:   databases/products.json
        new file:   databases/sliders.json
        new file:   jstore_ecommerce.db
        new file:   loader.py
        deleted:    media/sliders/2024/03/14/banner1.png
        deleted:    media/sliders/2024/03/14/banner3.png
        deleted:    media/sliders/2024/03/14/banner7.png
        new file:   shop/__init__.py
        new file:   shop/admin.py
        new file:   shop/apps.py
        new file:   shop/migrations/0001_initial.py
        new file:   shop/migrations/__init__.py
        new file:   shop/models/Category.py
        new file:   shop/models/Collection.py
        new file:   shop/models/Image.py
        new file:   shop/models/Product.py
        new file:   shop/models/Slider.py
        new file:   shop/models/__init__.py
        new file:   shop/tests.py
        new file:   shop/urls.py
        new file:   shop/views/shop_view.py
        modified:   templates/shop/index.html

        NOTE:

        1. Db baru.
        2. Inserted Sliders, Collecitons, Categories, Images, dan Products pada db


#### 7. Load dan display new arrival products

        modified:   README.md
        modified:   jstore_ecommerce.db
        modified:   shop/views/shop_view.py
        modified:   templates/shop/index.html


#### 8. Memindahkan code new arrival product ke file templates/partials/product.html

        modified:   README.md
        new file:   templates/partials/product.html
        modified:   templates/shop/index.html


#### 9. Load dan display new best sellers products

        modified:   README.md
        modified:   jstore_ecommerce.db
        modified:   templates/shop/index.html