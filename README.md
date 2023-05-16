# Playlist Django - PostgreSQL

## Description

API using Django Rest FrameWork using Generic View and Model Serializer with connection to PostgreSQL. Allows management of users, albums and songs.

## Documentation

Access the application documentation using the following endpoint:

```shell
/api/docs/
```

## Endpoints

| HTTP Method | Description    | Endpoint                      | User Types      | Authentication Required |
| ----------- | -------------- | ----------------------------- | --------------- | ----------------------- |
| POST        | Register album | `/api/albums/`                | Admin           | Authenticated           |
| GET         | List albums    | `/api/albums/`                | Users and Admin | No Authentication       |
| POST        | Register song  | `/api/albums/<int:pk>/songs/` | Admin           | Authenticated           |
| GET         | List songs     | `/api/albums/<int:pk>/songs/` | Users and Admin | No Authentication       |
| POST        | Register user  | `/api/users/`                 | Users and Admin | No Authentication       |
| GET         | List users     | `/api/users/`                 | Admin           | Authenticated           |
| POST        | Login          | `/api/users/login/`           | Users and Admin | No Authentication       |
| GET         | List user      | `/api/users/<int:pk>/`        | Users and Admin | Authenticated           |
| PATCH       | Update user    | `/api/users/<int:pk>/`        | Users and Admin | Authenticated           |
| DELETE      | Update user    | `/api/users/<int:pk>/`        | Users and Admin | Authenticated           |

## Run the tests for each task

Example:

- Task 1

```shell
pytest --testdox -vvs tests/users/
```

- Task 2

```shell
pytest --testdox -vvs tests/albums/
```

- Task 3

```shell
pytest --testdox -vvs tests/songs/
```
