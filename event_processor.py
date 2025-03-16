from sns_client import SNSClient
from utils import format_message
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def process_event(event):
    event_time = event.get('time', '')
    event_name = event.get('detail', {}).get('eventName')
    logger.info(f"Processing event: {event_name}")

    actionable_events = [
        "CreateUser",
        "CreateAccessKey",
        "PutBucketPolicy",
        "DeleteBucketPolicy",
        "AuthorizeSecurityGroupIngress",
        "ModifySecurityGroupRules"
    ]
    
    if event_name in actionable_events:
        return prepare_notification(event, event_time,event_name)
    return {
            'statusCode': 200,
            'body': 'Event ignored - not in scope of actionable events'
    }

def prepare_notification(event, event_time, event_name):
    user_identity = event.get('detail', {}).get('userIdentity', {})
    actor = user_identity.get('userName', user_identity.get('principalId', 'Unknown'))
    
    request_params = event.get('detail', {}).get('requestParameters', {})
    
    account = event.get('account', 'Unknown')

    account = event.get('account', 'Unknown')
    region = event.get('region', 'Unknown')
    
    # Construct the resource ARN based on resource type
    if event_name in ["CreateUser","CreateAccessKey"]:
        resource_name = request_params.get('userName', 'Unknown')
        resource_arn = f"arn:aws:iam::{account}:user/{resource_name}"
    elif event_name in ["PutBucketPolicy","DeleteBucketPolicy"]:
        resource_name = request_params.get('bucketName', 'Unknown')
        resource_arn = f"arn:aws:s3:::{resource_name}"
    elif event_name in ["AuthorizeSecurityGroupIngress","ModifySecurityGroupRules"]:
        resource_arn = f"arn:aws:ec2:{region}:{account}:security-group/{resource_name}"
    else:
        resource_arn = "Unknown"

    logger.debug(f"Formatting message for {event_name}")
    message = format_message(
        event_time=event_time,
        resource_arn = f"{resource_arn}",
        actor=actor,
        action=event_name
    )
    
    logger.info(f"Sending security notification for {event_name}")
    sns_client = SNSClient()
    sns_client.publish(message, f"Alert: {event_name} triggered by {actor}")
    

    return {
        'statusCode': 200,
        'body': f"Successfully processed event {event_name}"
    }