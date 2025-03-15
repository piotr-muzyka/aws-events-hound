import boto3
import os

class SNSClient:
    def __init__(self):
        self.sns_topic_arn = os.environ.get('SNS_TOPIC_ARN')
        self.sns = boto3.client('sns')
    
    def publish(self, message, subject='Alert: New IAM User Created'):
        try:
            response = self.sns.publish(
                TopicArn=self.sns_topic_arn,
                Subject=subject,
                Message=message
            )
            return response
        except Exception as e:
            raise Exception(f"Failed to publish to SNS: {str(e)}")
