def format_message(event_time, actor, resource_arn, action):
    return f"""
    AWS Security Alert: {action}
    
    Time: {event_time}
    Resource ARN: {resource_arn}
    Initiator: {actor}
    Action Performed: {action}
   
    """