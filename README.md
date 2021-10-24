# Reverse Proxying using Nginx

* Managing your service logs
* Put your application servers behind a nginx reverse proxy

## Logs
```bash
docker-compose logs -f backend
docker-compose logs -f webserver
```

## Docker Compose
- use '--reload' only during development. Not in deployment at all
