# json-validator-site

simple web for validating JSONs

## run

### run with docker

```bash
docker run -d -p 5000:5000 danielkraic/json-validator-site
# open url http://0.0.0.0:5000
```

### run locally with docker-compose

```bash
# start service
docker-compose up -d
# open url http://0.0.0.0:5000

# stop service
docker-compose kill
```

### run standalone app locally

```bash
./web/app.py
# open url http://0.0.0.0:5000
```
