# Object Challenge

![ci](https://github.com/mohammadmasoumi/object_challenge/workflows/ci/badge.svg)

This project is a technical challenge project which is powered by flask, docker and openresty.


# project structure

```
├── config.py
├── bucket
│   ├── fixtures
│   │   ├── user_prefixes.json
│   │   ├── users.json
│   │   └── prefixes.json
│   ├── services
│   │   ├── bucket.py
│   │   ├── __init__.py
│   ├── mongo_models
│   │   ├── user.py
│   │   ├── prefix.py
│   │   ├── user_prefix.py
│   │   ├── __init__.py
│   ├── views
│   │   ├── bucket.py
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── tests
│   │   ├── test_config.py
│   │   ├── test_bucket.py
│   │   ├── base.py
│   │   └── __init__.py
├── __init__.py
├── tree.py
├── base
│   ├── namedtuples.py
│   ├── mixins.py
│   ├── data_loader.py
│   ├── __init__.py
└── helper.py
```

# local setup

  - install requirements
     ```shell script
    pip install -r requirements/development.txt
     ```
  - load env
     ```shell script
    export  $(cat deployment/env_dir/flask.env | xargs)
     ```
  - runserver
     ```shell script
    python manage.py runserver
     ```
    

# server setup

 - install docker and setup github ssh keys
 - ```
   git clone git@github.com:mohammadmasoumi/object_challenge.git
   ``` 
 - ```
   cd /deployment
   ```
 - ```
   docker-compose up -d 
   ```

# flask shell

This project use `flask-shell-ipython` as an interactive flask shell.
```shell script
python manage.py shell
```

# Commands

- run server command
    ```shell script
    python manage.py runserver
    ``` 
- run server command
    ```shell script
    python manage.py shell
    ``` 
- load initial data command. `object_challenge/object_challenge/fixtures`
    ```shell script
    python manage.py init
    ``` 
    
   

# Resources

  - [How we reduced the CPU usage of our Lua code][1]
  - [tree structure in python][2]
  - [flask-script][3]
  - [flask][4]
  - [lua-nginx][5]
  
[1]: https://medium.com/@fabricebaumann/how-we-reduced-the-cpu-usage-of-our-lua-code-cc30d001a328
[2]: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
[3]: https://flask-script.readthedocs.io/en/latest/
[4]: https://flask.palletsprojects.com/en/1.1.x/
[5]: https://www.nginx.com/resources/wiki/modules/lua/