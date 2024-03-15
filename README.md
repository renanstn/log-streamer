# Log Streamer

## Objective

This little app just set ups a Flask application to serve a log file across my local network. With this, I can repurpose my old smartphone as a "third monitor" to monitor logs from other apps I'm developing.

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
