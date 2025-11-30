from typing import List
from app.data.models import NewsItem
from app.core.duck import query_df


def get_latest_news(limit: int = 20) -> List[NewsItem]:
    df = query_df(f"""
        SELECT *
        FROM 'data/raw/**/*.parquet'
        ORDER BY timestamp DESC
        LIMIT {limit}
    """)

    # Convert rows to NewsItem models
    return [NewsItem(**row) for row in df.to_dict(orient="records")]  # type: ignore


def get_latest():
    latest = [
        {
            "id": 4,
            "title": "Async programming in Python: A comprehensive guide.",
            "timestamp": "2025-06-01T09:00:00Z",
            "url": "https://example.com/async-programming-python",
            "summary": "Learn how to leverage async programming in Python for better performance.",
            "image_url": "https://images.unsplash.com/photo-1659084622165-6391a99e5ae8?w=1160",
            "category": "Technology",
        },
        {
            "id": 1,
            "title": "Breaking News: FastAPI is awesome!",
            "timestamp": "2024-09-01T12:00:00Z",
            "url": "https://example.com/breaking-news-fastapi",
            "summary": "FastAPI has been voted the most loved web framework in 2024.",
            "image_url": "https://picsum.photos/id/20/773/1160",
            "category": "Technology",
        },
        {
            "id": 2,
            "title": "Newz.day API reaches 1 million requests!",
            "timestamp": "2024-03-01T11:00:00Z",
            "url": "https://example.com/newzday-1-million-requests",
            "summary": "The Newz.day API has successfully handled over 1 million requests since launch.",
            "image_url": "https://images.unsplash.com/photo-1444653614773-995cb1ef9efa?w=1160",
            "category": "Business",
        },
        {
            "id": 3,
            "title": "Python remains the most popular programming language.",
            "timestamp": "2025-02-01T10:00:00Z",
            "url": "https://example.com/python-most-popular-language",
            "summary": "According to the latest surveys, Python continues to dominate the programming world.",
            "image_url": "https://images.unsplash.com/photo-1476242906366-d8eb64c2f661?w=1160",
            "category": "Programming",
        },
        {
            "id": 5,
            "title": "Understanding FastAPI's dependency injection system.",
            "timestamp": "2024-06-01T08:00:00Z",
            "url": "https://example.com/fastapi-dependency-injection",
            "summary": "A deep dive into how FastAPI's dependency injection works and how to use it effectively.",
            "image_url": "https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7?w=1160",
            "category": "Programming",
        },
    ]
    return latest


def get_hottest():
    hottest = [
        {
            "id": 11,
            "title": "Top 10 FastAPI tips and tricks.",
            "timestamp": "2024-05-31T15:00:00Z",
            "url": "https://example.com/top-10-fastapi-tips",
            "summary": "Discover the top 10 tips and tricks to enhance your FastAPI applications.",
            "image_url": "https://picsum.photos/id/237/773/1160",
            "hotness_score": 95,
        },
        {
            "id": 102,
            "title": "How to scale your FastAPI application.",
            "timestamp": "2024-05-31T14:00:00Z",
            "url": "https://example.com/scale-fastapi-application",
            "summary": "Learn strategies and best practices for scaling FastAPI applications effectively.",
            "image_url": "https://picsum.photos/id/237/773/1160",
            "hotness_score": 90,
        },
        {
            "id": 43,
            "title": "Deploying FastAPI with Docker and Kubernetes.",
            "timestamp": "2024-05-31T13:00:00Z",
            "url": "https://example.com/deploy-fastapi-docker-kubernetes",
            "summary": "A step-by-step guide to deploying FastAPI applications using Docker and Kubernetes.",
            "image_url": "https://picsum.photos/id/237/773/1160",
            "hotness_score": 88,
        },
        {
            "id": 14,
            "title": "Building real-time applications with FastAPI and WebSockets.",
            "timestamp": "2024-05-31T12:00:00Z",
            "url": "https://example.com/fastapi-websockets",
            "summary": "Learn how to create real-time applications using FastAPI and WebSockets.",
            "image_url": "https://picsum.photos/id/237/773/1160",
            "hotness_score": 85,
        },
        {
            "id": 51,
            "title": "FastAPI vs Flask: A detailed comparison.",
            "timestamp": "2024-05-31T11:00:00Z",
            "url": "https://example.com/fastapi-vs-flask",
            "summary": "An in-depth comparison between FastAPI and Flask to help you choose the right framework.",
            "image_url": "https://picsum.photos/id/237/773/1160",
            "hotness_score": 80,
        },
    ]
    return hottest
