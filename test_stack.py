#!/usr/bin/env python3
"""Smoke test: verify Docker services are running."""

import socket
import sys


def check_tcp(host, port, timeout=5):
    """Check if a TCP port is open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0


def main():
    services = [
        ("neo4j", 7474),
        ("grafana", 3001),
        ("postgres", 5432),
        ("redis", 6379),
        ("qdrant", 6333),
    ]

    all_ok = True
    for name, port in services:
        if check_tcp("localhost", port):
            print(f"OK {name}: port {port} open")
        else:
            print(f"FAIL {name}: port {port} closed")
            all_ok = False

    if all_ok:
        print("\nAll services are running!")
        sys.exit(0)
    else:
        print("\nSome services are not running!")
        sys.exit(1)


if __name__ == "__main__":
    main()
