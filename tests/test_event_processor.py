import unittest
from unittest.mock import patch, MagicMock

from src.event_processor import process_event

class TestEventProcessor(unittest.TestCase):
    
    @patch('src.event_processor.SNSClient')
    @patch('src.event_processor.format_message')
    def test_process_event_create_user(self, mock_format_message, mock_sns_client):
        # Arrange
        mock_format_message.return_value = "Test message"
        mock_sns_instance = MagicMock()
        mock_sns_client.return_value = mock_sns_instance
        
        event = {
            'time': '2023-01-01T00:00:00Z',
            'detail': {
                'eventName': 'CreateUser',
                'userIdentity': {'userName': 'admin'},
                'requestParameters': {'userName': 'newuser'}
            },
            'account': '123456789012',
            'region': 'us-east-1'
        }
        
        # Act
        result = process_event(event)
        
        # Assert
        self.assertEqual(result['statusCode'], 200)
        mock_format_message.assert_called_once()
        mock_sns_instance.publish.assert_called_once_with("Test message")
    
    def test_process_event_non_create_user(self):
        # Arrange
        event = {
            'time': '2023-01-01T00:00:00Z',
            'detail': {
                'eventName': 'DeleteUser',
                'userIdentity': {'userName': 'admin'},
                'requestParameters': {'userName': 'olduser'}
            },
            'account': '123456789012',
            'region': 'us-east-1'
        }
        
        # Act
        result = process_event(event)
        
        # Assert
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body'], 'Event ignored - not a user creation event')
    
    @patch('src.event_processor.SNSClient')
    @patch('src.event_processor.format_message')
    def test_process_event_sns_error(self, mock_format_message, mock_sns_client):
        # Arrange
        mock_format_message.return_value = "Test message"
        mock_sns_instance = MagicMock()
        mock_sns_instance.publish.side_effect = Exception("SNS error")
        mock_sns_client.return_value = mock_sns_instance
        
        event = {
            'time': '2023-01-01T00:00:00Z',
            'detail': {
                'eventName': 'CreateUser',
                'userIdentity': {'userName': 'admin'},
                'requestParameters': {'userName': 'newuser'}
            },
            'account': '123456789012',
            'region': 'us-east-1'
        }
        
        # Act/Assert
        with self.assertRaises(Exception):
            process_event(event)

if __name__ == '__main__':
    unittest.main()
