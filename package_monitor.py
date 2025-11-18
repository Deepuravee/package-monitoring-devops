import subprocess
import json
import logging
from prometheus_client import start_http_server, Gauge
import time

# Logging setup
logging.basicConfig(
    filename='package_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Prometheus Metric
g_outdated_packages = Gauge(
    'outdated_python_packages',
    'Number of outdated Python packages'
)


def get_outdated_pip_packages():
    """Return a list of outdated Python packages using pip."""
    try:
        result = subprocess.run(
            ['pip', 'list', '--outdated', '--format=json'],
            capture_output=True,
            text=True
        )
        packages = json.loads(result.stdout)
        return packages
    except Exception as e:
        logging.error(f"Error fetching outdated pip packages: {e}")
        return []


def update_packages():
    """Attempt to update all outdated Python packages."""
    outdated = get_outdated_pip_packages()

    for pkg in outdated:
        pkg_name = pkg['name']
        try:
            subprocess.run(['pip', 'install', '--upgrade', pkg_name])
            logging.info(f"Upgraded: {pkg_name}")
        except Exception as e:
            logging.error(f"Failed to upgrade {pkg_name}: {e}")


def monitor():
    """Monitor outdated packages and update Prometheus metrics."""
    logging.info("Starting package monitoring")

    outdated = get_outdated_pip_packages()
    count = len(outdated)

    g_outdated_packages.set(count)
    logging.info(f"Found {count} outdated package(s)")


if __name__ == "__main__":
    # Prometheus metrics available at: http://localhost:8000/metrics
    start_http_server(8000)

    while True:
        monitor()
        time.sleep(3600)  # Run every hour

