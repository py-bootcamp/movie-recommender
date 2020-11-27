# A (Random) movie recommender running on GCP Cloud Run

## To run the app

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## To build the docker image

```bash
docker build -t movie-recommender .
```

## To run the docker image

```bash
docker run --rm -p 8000:8000 movie-recommender gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## How to deploy it to GCP Cloud Run

In case you want to use the GCP Container Registry:
```bash
gcloud builds submit --tag eu.gcr.io/{YOUR-PROJECT}/movie-recommender
```

To deploy the image to GCP Cloud Run:
```bash
gcloud run deploy movie-recommender \
    --image eu.gcr.io/{YOUR-PROJECT}/movie-recommender \
    --platform managed \
    --allow-unauthenticated \
    --region europe-west1 \
    --args=gunicorn,main:app,-w,4,-k,uvicorn.workers.UvicornWorker
```
