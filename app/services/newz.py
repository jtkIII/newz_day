def get_latest():
    latest = [
        {
            "id": 1,
            "title": "Breaking News: FastAPI is awesome!",
            "timestamp": "2024-06-01T12:00:00Z",
        },
        {
            "id": 2,
            "title": "Newz.day API reaches 1 million requests!",
            "timestamp": "2024-06-01T11:00:00Z",
        },
        {
            "id": 3,
            "title": "Python remains the most popular programming language.",
            "timestamp": "2024-06-01T10:00:00Z",
        },
        {
            "id": 4,
            "title": "Async programming in Python: A comprehensive guide.",
            "timestamp": "2024-06-01T09:00:00Z",
        },
        {
            "id": 5,
            "title": "Understanding FastAPI's dependency injection system.",
            "timestamp": "2024-06-01T08:00:00Z",
        },
    ]
    return latest


def get_hottest():
    hottest = [
        {
            "id": 101,
            "title": "Top 10 FastAPI tips and tricks.",
            "hotness_score": 95,
        },
        {
            "id": 102,
            "title": "How to scale your FastAPI application.",
            "hotness_score": 90,
        },
        {
            "id": 103,
            "title": "Deploying FastAPI with Docker and Kubernetes.",
            "hotness_score": 88,
        },
        {
            "id": 104,
            "title": "Building real-time applications with FastAPI and WebSockets.",
            "hotness_score": 85,
        },
        {
            "id": 105,
            "title": "FastAPI vs Flask: A detailed comparison.",
            "hotness_score": 80,
        },
    ]
    return hottest
