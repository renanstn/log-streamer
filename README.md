# Log Streamer

## Objective

Allow to use my old phone as a "monitor" to show logs recorded in files.

## Stack

- Pipenv
- Flask

## Development

### Installing

```sh
pipenv install
```

### Start development server

```sh
export FILE_PATH="/your/log/file"
pipenv run flask run --host=0.0.0.0 --debug
```

## Accessing logs on the phone (using termux)

```sh
curl {your-local-ip}:5000/log
```
