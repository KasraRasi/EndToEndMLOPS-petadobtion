import logging
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler

# Set up Google Cloud logging
client = google.cloud.logging.Client()
handler = CloudLoggingHandler(client)

# Set up a standard logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

# Example logging
logger.info("Model prediction started.")
