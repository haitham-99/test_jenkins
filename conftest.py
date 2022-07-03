import pytest

import argparse


# def pytest_addoption(parser):
#
#     parser.addoption("--pytest", action="store")
def pytest_addopts(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run driver in headless mode."
    )
