import time
import requests

def check_api_latency(url):
    start = time.time()
    response = requests.get(url)
    end = time.time()

    latency = end - start

    return {
        "status_code": response.status_code,
        "latency_seconds": latency
    }

if __name__ == "__main__":
    result = check_api_latency("https://google.com")
    print(result)