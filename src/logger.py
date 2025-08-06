
# src/logger.py
from loguru import logger
import sys
import os
from pathlib import Path

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time} | {level} | {message}")
logger.add(
    LOGS_DIR / "pipeline.log",
    level="DEBUG",
    rotation="1 MB",
    compression="zip",
    enqueue=True,
    serialize=True,
    backtrace=True,
    diagnose=True
)


