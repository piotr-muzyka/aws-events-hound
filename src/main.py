import json
from src.event_processor import process_event

def lambda_handler(event, context):
    try:
        response = process_event(event)
        return response
    except Exception as e:
        print(f"Error processing event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
