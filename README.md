# rumorend

## How to use the service
First, install all the dependencies by

```
pip install -r requirements.txt
``` 

Then, run the service by

```
FLASK_APP=rumorend_service.py flask run
```

## The interfaces
You can call the detection interface by POSTing a json query. An example is in statac/example.html