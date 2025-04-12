# SpamAI

Dockerized WebAPI for [RUSpam/spam_deberta_v4](https://huggingface.co/RUSpam/spam_deberta_v4)

# How to run

Create container in one row:

```bash
docker run -d -p 8080:8080 --name spamai ghcr.io/bvdcode/spamai
```

Send test request:

```bash
curl -X POST http://localhost:8080 -H "Content-Type: application/json" -d 'Привет! Ищешь заработок в интернете?'
```

Response:

```json
{
  "result": true
}
```
