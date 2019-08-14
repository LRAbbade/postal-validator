# Postal Validator

This project is made to validate brazilian postal codes.

## Execution

To execute, all you need is [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

Then, just run:

```sh
docker-compose up
```

This will start a web server, you can access it by [clicking here once it's running](http://localhost/).

To stop, just `ctrl+D`.

## Tests

To run the tests, you can either run `python -m unittest` if you have Python 3 installed (no dependencies are required for the tests), or, while the server is running, access the container by:

+ Find out the container ID by running `docker container ls -a`, then:

```sh
docker exec -it <container_ID> sh
```

This will get you inside the container, then:

```sh
cd /usr/src/app
python -m unittest
```

Once you are happy, just type `exit` to quit the container.

---
