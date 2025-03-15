import unittest
from unittest.mock import patch, MagicMock
import os

from sns_client import SNSClient

class TestSNSClient(unittest.TestCase):
    
    @patch('boto3.client')
    @patch.dict(os.environ, {'SNS_TOPIC_ARN': 'arn:aws:sns:eu-central-1:123456789012:test-topic'})
    def test_init(self, mock_boto3_client):
        # Act
        client = SNSClient()
        
        # Assert
        self.assertEqual(client.sns_topic_arn, 'arn:aws:sns:eu-central-1:123456789012:test-topic')
        mock_boto3_client.assert_called_once_with('sns')
    
    @patch('boto3.client')
    @patch.dict(os.environ, {'SNS_TOPIC_ARN': 'arn:aws:sns:eu-central-1:123456789012:test-topic'})
    def test_publish_success(self, mock_boto3_client):
        # Arrange
        mock_sns = MagicMock()
        mock_boto3_client.return_value = mock_sns
        mock_sns.publish.return_value = {'MessageId': 'test-message-id'}
        
        client = SNSClient()
        message = "Test message"
        subject = "Test subject"
        
        # Act
        response = client.publish(message, subject)
        
        # Assert
        self.assertEqual(response, {'MessageId': 'test-message-id'})
        mock_sns.publish.assert_called_once_with(
            TopicArn='arn:aws:sns:eu-central-1:123456789012:test-topic',
            Subject='Test subject',
            Message='Test message'
        )
    
    @patch('boto3.client')
    @patch.dict(os.environ, {'SNS_TOPIC_ARN': 'arn:aws:sns:eu-central-1:123456789012:test-topic'})
    def test_publish_error(self, mock_boto3_client):
        # Arrange
        mock_sns = MagicMock()
        mock_boto3_client.return_value = mock_sns
        mock_sns.publish.side_effect = Exception("SNS error")
        
        client = SNSClient()
        message = "Test message"
        
        # Act/Assert
        with self.assertRaises(Exception) as context:
            client.publish(message)
        
        self.assertIn('Failed to publish to SNS', str(context.exception))

if __name__ == '__main__':
    unittest.main()
