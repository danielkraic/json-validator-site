# json-validator-site

[![Build Status](https://travis-ci.org/danielkraic/json-validator-site.svg?branch=master)](https://travis-ci.org/danielkraic/json-validator-site)
[![Coverage Status](https://coveralls.io/repos/github/danielkraic/json-validator-site/badge.svg?branch=code-coverage)](https://coveralls.io/github/danielkraic/json-validator-site?branch=code-coverage)

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
./web/web.py
# open url http://0.0.0.0:5000
```
