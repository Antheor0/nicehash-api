NOT WORKING YET

## NiceHash-Api
Many thanks to shiggid for providing a working nicehash api client https://github.com/nicehash/rest-clients-demo/tree/master/python

### Goal
The goal was to use the nicehash api to monitor statistics and expose them with the simplest web server possible.
This must remain in a private environement.

### Description
The server is intended to work in a docker environement.
it exposes json data on *.*.*.*:12323/rig.json

### Prometheus configuration
Set up a scrape job in prometheus

## Docker-Compose

```docker-compose
version: "3.9"
services:
  nicehash-api:
    container_name: Nicehash-API
    image: antheor0/nicehash-api:latest
    environment:
        - api_key=<nicehash api key>
        - api_secret=<nicehash api secret>
        - organization_id=<nicehash organization id>
    ports:
      - "12323:12323"
```
