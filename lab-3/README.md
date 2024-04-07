### Лабараторная №3

1. #### Установим CouchDB на локальный пк с помощью команд:

    ```cmd
    sudo apt update && sudo apt install -y curl apt-transport-https gnupg

    curl https://couchdb.apache.org/repo/keys.asc | gpg --dearmor | sudo tee /usr/share/keyrings/couchdb-archive-keyring.gpg >/dev/null 2>&1

    source /etc/os-release

    echo "deb [signed-by=/usr/share/keyrings/couchdb-archive-keyring.gpg] https://apache.jfrog.io/artifactory/couchdb-deb/ ${VERSION_CODENAME} main"     | sudo tee /etc/apt/sources.list.d/couchdb.list >/dev/null

    sudo apt update

    sudo apt install -y couchdb
    ```

2. #### Перейдем на http://127.0.0.1:5984/_utils/, зайдем через админа и создадим там базу данных "mydatabase"

    ![](./screens/Screenshot%20from%202024-04-07%2017-02-43.png)

3. #### Внутри нашей БД создадим документ с полем "name": "Уразов"

    ![](./screens/Screenshot%20from%202024-04-07%2017-02-51.png)
    ![](./screens/Screenshot%20from%202024-04-07%2017-02-56.png)

4. #### Скачаем html файл и поправим в нем ссылку на нашу базу данных
    Изменим следующие строки:
    
    ```js
    const DBS = {
    // Создаем локальную БД и коннектимся к удаленной 
      Local: new PouchDB('docs'),
      Remote: new PouchDB('http://admin:1213@localhost:5984/mydatabase')
    }
    ```

    Разрешим CORS через Configuration -> CORS -> Enable CORS -> All domains (*):

    ![](./screens/Screenshot%20from%202024-04-07%2018-11-37.png)

    Откроем наш html в браузере и нажмем кнопку "sync" чтобы проверить все ли работает:
    
    ![](./screens/Screenshot%20from%202024-04-07%2017-03-17.png)

5. #### Остановим CouchDB сервер и проверим фигурирует ли фамилия в html:
    
    Остановим сервер командой:
    
    ```cmd
    sudo service couchdb stop
    ```
    Откроем html файл в браузере опять и убедимся что фамилия все еще отображается в нем
    
    ![](./screens/Screenshot%20from%202024-04-07%2017-06-00.png)

6. #### Сохраним html файл из браузера:
    
    Полученный файл:

      [ДЗ_2.html](hw2.html)
