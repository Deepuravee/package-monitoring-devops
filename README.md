# Package Monitoring Script with DevOps

This project is a Python-based package monitoring tool that detects outdated `pip` packages,
logs the results, and exposes a Prometheus metric endpoint for monitoring.

## Features
- Logs outdated Python packages.
- Prometheus exporter (on port 8000).
- Optional auto-update mode.
- Can be scheduled using cron or automated via Ansible.
- Docker-compatible.

## Prometheus Metric
- `outdated_python_packages`: Tracks the number of outdated pip packages.

## Usage
```bash
python package_monitor.py
```

## Docker Usage
```bash
docker build -t package-monitor .
docker run -p 8000:8000 package-monitor
```

## Cron Setup
```bash
0 * * * * /usr/bin/python3 /path/to/package_monitor.py
```

OUTPUT: 
![image](https://github.com/user-attachments/assets/4c22befe-335d-4c69-90b5-4c8f60f8f4d8)

