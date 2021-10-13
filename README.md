# ** НИЧЕГО НЕТ ** 
### *Содержание проекта*
* О чём?
* Какие техники использованы?
* Можно лучше?
* Установка

## **О чём**

*идея пришла совсем случайно, когда мы с Ваней углубились в электронную музыку. мы оказались на одной волне и создали общий плейлист с польскими, немецкими, иногда вообще паслестинскими пластинками, на которых чаще всего звучало техно, либо что-то родственное ему по ритмике. чуть позже, мне настолько сильно захотелось делиться вайбом этой музыки, что было решено производить кепки. каждую вещь нужно полюбить и вложить в нее что-то мы очень хотели бы чтобы вы ее получили после того, как послушаете наш плейлист, и создали из нее особую вещь с глубокими асоциациями.*

## **Какие техники использованы**

*В данном проекте применяется адаптивная верстка для экранов с размерами: 320px, 768px, 1024px, 1220px.*
*Написан на языке языке Python с помощью Django с использованием ООП*

## **Можно лучше**

**Можно и нужно лучше!**

## **Установка**
*(для пользователей операционных систем семейства MacOs/Linux):*
  Открыть терминал или консоль и перейти в нужную Вам директорию
  Прописать команду git clone https://gitlab.com/catsoup1337/capage.git

  Прописать следующие команды:


  python3 -m venv venv
  source venv/bin/activate
  Перейти в директорию capage

  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  
  Запустить сервер - python manage.py runserver

