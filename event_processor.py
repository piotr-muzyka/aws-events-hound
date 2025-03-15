import json
from sns_client import SNSClient
from utils import format_message

def process_event(event):
    # Extract relevant information from the event
    event_time = event.get('time', '')
    event_name = event.get('detail', {}).get('eventName')
    
    # Check if this is an IAM user creation event
    if event_name != 'CreateUser':
        print(f"Event {event_name} is not a user creation event. Skipping.")
        return {
            'statusCode': 200,
            'body': 'Event ignored - not a user creation event'
        }
    
    # Extract user details
    user_identity = event.get('detail', {}).get('userIdentity', {})
    request_parameters = event.get('detail', {}).get('requestParameters', {})
    
    # Get the IAM user that was created
    created_user_name = request_parameters.get('userName', 'Unknown')
    
    # Get the identity that performed the action
    actor = user_identity.get('userName', user_identity.get('principalId', 'Unknown'))
    
     # Extract the account ID 
    account = event.get('account', 'Unknown')

    # Construct the resource ARN for the IAM user
    resource_arn = f"arn:aws:iam::{account}:user/{created_user_name}"

    # Extract the action (event name) from the event
    action = event.get('detail', {}).get('eventName', 'Unknown')

    # Format the message
    message = format_message(event_time, created_user_name, actor, event, resource_arn, action)
    
    # Publish to SNS topic
    sns_client = SNSClient()
    sns_client.publish(message)
    
    print(f"Alert sent to SNS topic")
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully sent alert for IAM user creation')
    }
