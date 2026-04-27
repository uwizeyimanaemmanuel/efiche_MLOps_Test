import time
import requests

def check_replication_lag(source_url, replica_url):
    start = time.time()

    source = requests.get(source_url)
    replica = requests.get(replica_url)

    end = time.time()

    return {
        "source_status": source.status_code,
        "replica_status": replica.status_code,
        "replication_lag_seconds": round(end - start, 4)
    }

if __name__ == "__main__":
    result = check_replication_lag(
        "https://example.com",
        "https://example.com"
    )
    print(result)