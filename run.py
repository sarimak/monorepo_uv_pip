#!/usr/bin/env python

import argparse
import importlib
import os


def run_service(service_name: str | None = None) -> None:
    service_module = importlib.import_module(f"svc.{service_name}")
    service_module.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Run given service")
    parser.add_argument("service_name", nargs="?", default=os.environ.get("SERVICE_NAME"))
    args = parser.parse_args()

    run_service(args.service_name)
