# Object Challenge

![ci](https://github.com/mohammadmasoumi/object_challenge/workflows/ci/badge.svg)

This project is a technical challenge project which is powered by flask, docker and openresty.

# local setup

  - install requirements
  ```shell script
    pip install -r requirements/development.txt
  ```
  - load env
  ```shell script
    export  $(cat deployment/env_dir/flask.env | xargs)
  ```
