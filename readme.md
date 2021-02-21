#NiceHash-Api
Many thanks to shiggid for providing a working nicehash api client https://github.com/nicehash/rest-clients-demo/tree/master/python
##Goal
The goal was to use the nicehash api to monitor statistics and expose them with the simplest web server possible.
This must remain in a private environement.
##Docker-Compose
```docker-compose
version: "3.9"
services:
  nicehash-api:
    images: antheor0/nicehash-api:latest
    environement:
        api_key=<nicehash api key>
        api_secret=<nicehash api secret>
        organization_id=<nicehash organization id>
    ports:
      - "12323:12323"
```
