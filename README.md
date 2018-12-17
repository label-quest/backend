Create a `.env` file similar to the `env.example` file

# Docker compose
## Ports
- API listens on port 8000
- Picture server listens on port 8081
- DB admin interface listens on port 8080 (can't connect to the DB currently)

DB user is postgres, database name is postgres, password is mysecretpassword.
You can access it over localhost:5433.

## Migrations
Run `docker-compose run api python3 /backend/manage.py migrate` to run the DB migrations
