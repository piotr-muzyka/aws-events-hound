import json
from event_processor import process_event

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Lambda function invoked with event: %s", json.dumps(event))
    
    try:
        result = process_event(event)
        logger.info("Event processing completed successfully: %s", result)
        return result
    except Exception as e:
        logger.error("Error processing event: %s", str(e), exc_info=True)
        logger.error("Event that caused the error: %s", json.dumps(event))
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }