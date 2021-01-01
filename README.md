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
pip install flask-shell-ipython
flask shell
```

# Commands

 - management commands
    - for initializing fixtures you can use. `object_challenge/object_challenge/fixtures`
    ```shell script
    flask manage initial
    ``` 

# Resources

  - [How we reduced the CPU usage of our Lua code][1]
  
  
[1]: https://medium.com/@fabricebaumann/how-we-reduced-the-cpu-usage-of-our-lua-code-cc30d001a328