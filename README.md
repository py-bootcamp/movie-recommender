# A (Random) movie recommender running on GCP App Engine

## To run the app

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## How to deploy it to GCP App Engine

If it's the first time you need to `create` the app
```bash
gcloud app create
```

After you created the app you can `deploy` (same thing if you need to deploy changes)

```bash
gcloud app deploy
```
