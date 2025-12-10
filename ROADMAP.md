<!-- ROADMAP.md -->

# ✅ **Newz.day Roadmap (Updated)**

## **1) 🔧 Data Layer (DuckDB)**

### **1.1 — Finalize schema + Parquet layout**

* `/data/news.parquet`
* Partitioning: `/data/news/category=tech/*.parquet`
* Create a persistent `duckdb.load()` helper:

  * `get_latest(limit=20)`
  * `get_by_category(category, limit=20)`
  * `get_top_sources()`
  * `get_summary_counts()`

### **1.2 — Ingestion improvements**

**To-Do:**

* Convert `NewsItem` to dict → DuckDB insert
* Deduplicate by `url` or `(title, source)`
* Normalize timestamps to UTC

---

## **2) 🖥 Frontend**

### **2.1 — Partial templates - keep `news.html` clean**

* `_header.html`
* `_footer.html`
* `_nav.html`
* `_news_card.html` (done)
* `_pagination_button.html` (for HTMX "load more")

### **2.2 — Dark mode (completed)**

* Uses Tailwind `dark:` classes (done)
* `dark-mode-toggle.js` (done)

---

## **3) 🔄 HTMX: Pagination (Load More)**

This is your next big feature and integrates beautifully with DuckDB.

### **3.1 — Strategy**

* Page loads latest 15 items
* Below the list: a button:

```html
<button 
  hx-get="/latest?page=2"
  hx-target="#item-list"
  hx-swap="afterend"
  class="load-more-button"
>
  Load more
</button>
```

### **3.2 — Backend**

In your FastAPI route:

```python
@router.get("/latest")
def latest(page: int = 1):
    limit = 15
    offset = (page - 1) * limit
    items = get_latest(limit=limit, offset=offset)
    return templates.TemplateResponse("_news_item_list.html", {"items": items})
```

### **3.3 — Partial fragment**

Return **only** new `<li>` rows, not the entire page.

---

## **4) 📊 Analytics Pages (DuckDB)**

This is where DuckDB shines.

---

### **4.1 — “Top Sources” Page**

Query:

```sql
SELECT source, COUNT(*) AS count
FROM news
GROUP BY source
ORDER BY count DESC;
```

FastAPI:

```python
@router.get("/top-sources")
def top_sources():
    rows = news_repo.get_top_sources()
    return templates.TemplateResponse("top_sources.html", {"rows": rows})
```

Template displays a simple table or cards.

---

### **4.2 — Summary Page (Protected)**

Compute:

* total articles
* articles per category
* articles per day (histogram)
* top sources
* earliest + latest timestamp
* maybe avg summary length

SQL:

```sql
SELECT COUNT(*) FROM news;
SELECT category, COUNT(*) FROM news GROUP BY category;
SELECT date_trunc('day', timestamp) AS day, COUNT(*) 
FROM news GROUP BY day ORDER BY day DESC;
```

This becomes one beautiful summary dashboard.

---

## **5) 🎨 UX Polish (optional but easy wins)**

* Make news card fully clickable
* Add hover elevation (`hover:scale-[1.01]`)
* Add lazy-load to images:

  ```html
  <img loading="lazy">
  ```

* Add skeleton loaders for HTMX transitions
* Add infinite scroll (optional upgrade from pagination)

---

## **6) 🚀 Deployment Prep**

Once MVP is working:

* Replace Tailwind CDN → Tailwind CLI
  (only needs a config + build script)
* Build `docker-compose.yml`
* uvicorn worker count tuning
* static file caching (long-lived)
* DuckDB file locking considerations (read-heavy, write-light = perfect)

---

# 🔥 Recommended Order of Work

1. **Pagination (“Load More”)**
2. **Top Sources page (easy DuckDB group-by)**
3. **Summary page (multiple DuckDB queries)**
4. **Footer/nav partials**
5. **Other UI polish (full-card clickable, image lazy loads)**

---

# 🎯 So — where do you want to continue?

Pick one:

1. Implement **HTMX Load More**
2. Add **Top Sources** DuckDB query + page
3. Build the **Summary Dashboard**
4. Start **partials (header/footer/nav)**
5. Or: “show me the file and refactor it with you”

Just tell me which direction you want to go.
