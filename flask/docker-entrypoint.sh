
#!/bin/bash


flask db upgrade

exec gunicorn -w 1 --bind 0.0.0.0:80 "app:create_app()" --log-level debug