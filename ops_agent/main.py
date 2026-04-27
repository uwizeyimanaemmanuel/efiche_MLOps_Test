from fastapi import FastAPI, Depends
import redis.asyncio as redis
import datetime
from replication import compute_trend, is_degraded

app = FastAPI()
r = redis.from_url("redis://localhost")

KEY = "replication:lag"

@app.get("/replication-health")
async def replication_health():
    now = datetime.datetime.utcnow().isoformat()

    # fake lag from DB (replace with real query)
    lag = 4.2

    await r.lpush(KEY, f"{lag}:{now}")
    await r.ltrim(KEY, 0, 4)

    raw = await r.lrange(KEY, 0, -1)

    history = []
    values = []

    for item in reversed(raw):
        lag_s, ts = item.decode().split(":")
        lag_s = float(lag_s)
        values.append(lag_s)
        history.append({
            "lag_seconds": lag_s,
            "recorded_at": ts
        })

    return {
        "lag_seconds": lag,
        "trend": compute_trend(values),
        "degraded": is_degraded(values),
        "last_checked": now,
        "history": history
    }