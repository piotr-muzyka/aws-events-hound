import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class SNSClient:
    def __init__(self):
        self.sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
        if not self.sns_topic_arn:
            logger.error("SNS_TOPIC_ARN environment variable is not set")
            raise ValueError("SNS_TOPIC_ARN environment variable is not set")
        self.sns = boto3.client('sns')
    
    def publish(self, message, subject):
        try:
            response = self.sns.publish(
                TopicArn=self.sns_topic_arn,
                Subject=subject,
                Message=message
            )
            logger.info(f"Notification sent to {self.sns_topic_arn}")
            return response
        except Exception as e:
            raise Exception(f"Failed to publish to SNS: {str(e)}")
