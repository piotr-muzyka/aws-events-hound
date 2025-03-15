def format_message(event_time, created_user_name, actor, event, resource_arn, action):
    return f"""
    IAM User Creation Alert
    
    Time of Event: {event_time}
    New User Created: {created_user_name}
    Initiator: {actor}
    AWS Account: {event.get('account', 'Unknown')}
    Region: {event.get('region', 'Unknown')}
    Resource ARN: {resource_arn}
    Action Performed: {action}

    """
