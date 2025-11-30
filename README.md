# newz.day

## Efficient, Propaganda Resistant, News.  Daily

### Fully wired FastAPI → DuckDB → Jinja HTMX system

**DuckDB → FastAPI → Jinja/HTMX** clean and idiomatic
production-quality routes that pulls from Parquet via DuckDB and render your template

---

#### Start the server

`API_KEY=a_super_secret_api_key uvicorn app.main:app --reload`

#### Call an endpoint

`curl -H "x-api-key:a_super_secret_api_key" http://127.0.0.1:8000/api/v1/newz/`

---

#### You'll need to make a .env file that has contents similar to

API_KEY=some_super_secret_api_key
DEBUG=true
HOST=127.0.0.1
PORT=8000
ALLOWED_IPS=127.0.0.1,10.0.0.0/8
CACHE_TTL_SECONDS=5

---

#### File Concepts

app/
  core/
    duck.py              ← connection + query_df
  services/
    news.py              ← high-level domain logic
  routes/
    latest.py            ← FastAPI endpoint
  templates/
    news.html            ← your Jinja list template

```

# ⚡ Keep DuckDB out of your routes...

* Routes stay thin
* Business logic stays centralized
* Easy to swap DuckDB/Postgres later if needed
* Very readable
* No long imports
* No DuckDB code in routes
* Cleanly return Jinja template

### ✔ True layered architecture

* DuckDB connection isolated
* Query helpers reusable
* Service layer clean
* Routes very short

### ✔ Extremely fast iteration

Could:

* drop in a new parquet file
* restart FastAPI (or even hot-reload)
* instantly see updated content

### ✔ Zero SQL boilerplate in your routes
Routes only deal with **input → output → templates**.

### ✔ Future-proof
Could move to Postgres later without touching routes/templates.

---



## TODOS:

🔹 Add category filters (HTMX swap)
🔹 Add pagination (HTMX: load more)
🔹 Make a proper `<article>` card partial → `{% include "partials/card.html" %}`
🔹 Add dark mode
🔹 Add a summary page powered by aggregate DuckDB queries
🔹 Add “Top Sources” analysis using DuckDB `GROUP BY`

