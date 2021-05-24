# Autocompleter API

This is a simple autocomplete API that, when given a partial word, returns a list of autocomplete suggestions.

## Overview

The Autocompleter API has two routes:
 * `/` - returns a simple JSON `{"ping": "pong"}` response
 * `/words/{word}` - returns a JSON response list of suggested autocompletes, based on `{word}`
   ```json
   {"words":[..]}
   ```

## Running the API

The API can be run in several ways:
 * Docker
   
   ```bash
   docker build -t autocompleter-api:0.1.1 .
   docker run -dp 8000:80 autocompleter-api
   ```

 * Docker compose
   
   ```bash
   docker-compose up -d
   ```

 * Helm Chart
   **If using minikube**, run the following prior to running helm install:
   
   ```bash
   docker build -t autocompleter-api:0.1.1 .
   minikube cache add autocompleter-api:0.1.2
   ```
   
   To install the helm chart and deploy autocompleter-api
   
   ```bash
   helm install autocompleter-api charts/autocompleter-api
   ```

## Using the API

The API path for retrieving autocomplete suggestions is `/words/{word}` where `{word}` can be a partial (or whole) word, such as `scho` or `school`.

Two easy ways of testing responses with the API are using curl or using the interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)) in the browser.

### Using curl
If using `docker` or `docker-compose`
```bash
$ curl http://localhost:8000/words/school
```

If using Helm Chart (minikube/kubernetes)
```bash
$ curl http://<endpoint>/words/school
```

**Results**
```json
{"words":["schoolmate","schoolboy","schoolgirlish","schoolhouse","schoolyard","schoolmaster","schoolbook","school","schoolroom","schoolwork","schoolmarm","schoolgirl","schoolteacher"]}
```


### Using Swagger UI

Autocompleter API uses FastAPI, which includes interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)).  Open in the browser by visiting http://localhost:8000/docs (or http://\<endpoint\>/docs)

### Alternatively

You could also visit http://localhost:8000/words/school (or http://\<endpoint\>/words/school) in your browser.

