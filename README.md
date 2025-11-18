# newz.day

### Efficient, Propaganda Resistant News.  Daily.


##### Can you get more efficient than HTMX + FastAPI?  Well and an great db of course.



## Start the server:
`API_KEY=a_super_secret_api_key uvicorn app.main:app --reload`

## Call an endpoint
`curl -H "x-api-key:a_super_secret_api_key" http://127.0.0.1:8000/api/v1/newz/`
