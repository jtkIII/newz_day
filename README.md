# newz.day

## Efficient, Propaganda Resistant News.  Daily

### Start the server

`API_KEY=a_super_secret_api_key uvicorn app.main:app --reload`

#### Call an endpoint

`curl -H "x-api-key:a_super_secret_api_key" http://127.0.0.1:8000/api/v1/newz/`

--------------------------------------------------------------------------

#### You'll need to make a .env file that has contents similar to

API_KEY=some_super_secret_api_key
DEBUG=true
HOST=127.0.0.1
PORT=8000
ALLOWED_IPS=127.0.0.1,10.0.0.0/8
CACHE_TTL_SECONDS=5
