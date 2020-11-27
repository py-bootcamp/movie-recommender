# A (Random) movie recommender running as GCP Cloud Function

## To deploy this function on GCP

```bash
gcloud functions deploy movie-recommender \
    --entry-point recommend_movie \
    --runtime python38 \
    --trigger-http \
    --allow-unauthenticated \
    --region=europe-west1
```
