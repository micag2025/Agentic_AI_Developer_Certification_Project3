
# src/logger.py
from loguru import logger
import sys
from pathlib import Path

# Central log directory
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Remove default logger to avoid duplicate logs
logger.remove()

# Console logging (INFO+)
logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
    enqueue=True,
    backtrace=False,   # keep console cleaner
    diagnose=False     # only detailed in file logs
)

# File logging (DEBUG+) with JSON structured logs
logger.add(
    LOGS_DIR / "pipeline.log",
    level="DEBUG",
    rotation="5 MB",        # allow larger file before rotation
    retention="30 days",    # keep logs for 30 days
    compression="zip",
    enqueue=True,
    serialize=True,         # structured JSON logs
    backtrace=True,
    diagnose=True           # detailed stack traces for debugging
)

# Separate error log file
logger.add(
    LOGS_DIR / "errors.log",
    level="ERROR",
    rotation="1 MB",
    retention="14 days",
    compression="zip",
    enqueue=True,
    serialize=True
)

# 🔥 Capture uncaught exceptions globally
def exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Allow Ctrl+C to behave normally
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.opt(exception=(exc_type, exc_value, exc_traceback)).error("Uncaught exception")

sys.excepthook = exception_handler

