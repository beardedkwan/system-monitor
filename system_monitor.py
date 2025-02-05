import psutil

def monitor_system():
    while True:
        # Get system metrics
        cpu_usage = psutil.cpu_percent(interval=1)

        # Print system metrics
        print(f"CPU Usage: {cpu_usage}%")

monitor_system()
