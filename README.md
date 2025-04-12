# SpamAI

Dockerized WebAPI for RUSpam/spam_deberta_v4

# How to run

2 rows:

```bash
docker run -p 8080:8080 --name spamai ghcr.io/bvdcode/spamai
curl -X POST http://localhost:8080 -H "Content-Type: application/json" -d 'Привет! Ищешь заработок в интернете?'
```

Response:

```json
{
  "result": true
}
```
