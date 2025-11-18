from collections import defaultdict
from typing import Dict, List


request_log: Dict[str, List[Dict]] = defaultdict(list)


def get_total_web_requests() -> int:
    return sum(len(entries) for entries in request_log.values())


def log_request(ip: str, user_agent: str, path: str):
    """
    Call this in FastAPI middleware
    """
    request_log[ip].append({"user_agent": user_agent, "path": path})
    # Optional: limit history per IP
    if len(request_log[ip]) > 1000:
        request_log[ip] = request_log[ip][-1000:]
