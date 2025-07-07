# Flask App 2 – Random Quote Generator

Returns a new motivational quote every time you refresh.

## Run Locally

```bash
docker build -t flask-app-2 .
docker run --rm -p 5001:5000 --env-file .env flask-app-2
Example Output
{
  "quote": "You're doing better than you think.",
  "source": "flask-app-2"
}


---

## 🧪 Test It

docker build -t flask-app-2 .
docker run --rm -p 5001:5000 --env-file .env flask-app-2
Then go to:
http://127.0.0.1:5001/


Each refresh should show a different quote.
http://127.0.0.1:5001/