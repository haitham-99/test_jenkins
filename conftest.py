import pytest

import argparse

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run driver in headless mode."
    )
