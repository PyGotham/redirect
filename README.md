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

## Contributing

Install the development requirements and enable
[pre-commit](https://pre-commit.com). This will cause the code to be formatted
automatically before you commit it.

```
$ pip3 install -r dev-requirements.txt
$ pre-commit install
```

While linting and fixing will happen as part of pre-commit hooks, there is a
test suite that can be run as well.

```
$ tox
```
