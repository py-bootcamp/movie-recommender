# A (Random) movie recommender

## To run the app

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## To build the docker image

```bash
docker build -t movie-recommender .
```

## To run the docker image

```bash
docker run --rm -p 8888:8888 movie-recommender python app.py
```
