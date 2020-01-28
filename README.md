# redirect

A simple server to redirect to the current PyGotham site

## Usage

```
$ python3 redirect.py
```

or

```
$ pip3 install -r requirements.txt
$ uwsgi uwsgi.ini
```

## Configuration

* `PYGOTHAM_YEAR`: The year is the subdomain to which the application will
  redirect. If no value is provided, the current year will be used.

* `PORT`: The port to which the application should bind. If no value is
  provided, `8000` will be used.
