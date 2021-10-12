Репозиторий интернет-магазина кепок на Django
Установка (для пользователей операционных систем семейства MacOs/Linux):

Открыть терминал или консоль и перейти в нужную Вам директорию
Прописать команду git clone https://gitlab.com/catsoup1337/capage.git

Прописать следующие команды:


python3 -m venv venv
source venv/bin/activate
Перейти в директорию capage

pip install -r requirements.txt
python manage.py migrate


Запустить сервер - python manage.py runserver

