# PetPassport
PetPassport - сервис, который поможет владельцам домашних животных эффективно управлять информацией о своих питомцах, поддерживать их здоровье, а также легко находить клиники, которые предоставляют услуги лучшего качества. Этот сервис также может помочь людям, которые хотят присоединиться к сообществу владельцев домашних животных. (Возможен функционал общения)

##Запуск проекта

Первый шаг одинаковый, дальше разные для OC Windows/Linux  
**1** Клонируем себе репозиторий:  
```git clone https://github.com/MrForquest/petpassport.git ```  
и переходим в папку с проектом   
```cd petpassport ```

####Windows<br>
**2** Заводим виртуальное окружение и активируем его:<br>
```python -m venv venv ```<br>
```.\venv\Scripts\activate ```<br>
**3** Обновляем pip и качаем туда все что есть в requirements.txt:<br>
```python -m pip install --upgrade pip``` <br>
```pip install -r .\requirements\prod.txt ```<br>
**4** Переходим в папку <br>```cd petpassport``` <br>
**5** Загружаем миграции для базы данных <br>
```python manage.py migrate``` <br>
**6** Загружаем по желанию тестовую фикстуруе, чтобы в БД были какие-то данные <br>
```python manage.py loaddata data_example.json``` <br>
**7** Запускаем проект: <br> 
``` python .manage.py runserver ```