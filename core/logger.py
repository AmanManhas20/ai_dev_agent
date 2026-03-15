import logging
import os


LOG_DIR = "logs"
LOG_FILE = "agent.log"


def setup_logger():
    """
    Configure logging system for the AI agent project
    """

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    log_path = os.path.join(LOG_DIR, LOG_FILE)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


def log_info(message: str):
    """
    Log informational messages
    """

    logging.info(message)


def log_warning(message: str):
    """
    Log warning messages
    """

    logging.warning(message)


def log_error(message: str):
    """
    Log error messages
    """

    logging.error(message)