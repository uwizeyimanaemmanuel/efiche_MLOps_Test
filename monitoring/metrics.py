import time
import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_system_metrics():
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "timestamp": time.time()
    }

if __name__ == "__main__":
    print(get_system_metrics())