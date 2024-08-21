# docker-compose-assignment

## running all services

```shell
docker compose -f docker-compose-dev.yaml -p spdx-api up --build -d
```

```shell
docker compose -f docker-compose-test.yaml -p spdx-test up --build -d 