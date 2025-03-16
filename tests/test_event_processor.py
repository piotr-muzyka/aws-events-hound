# import unittest
# from unittest.mock import patch, MagicMock
# import json
# import os
# import sys

# # Add the parent directory to sys.path to import the application code
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from event_processor import process_event

# class TestEventProcessor(unittest.TestCase):
    
#     @patch.dict('os.environ', {'SNS_TOPIC_ARN': 'arn:aws:sns:us-east-1:123456789012:test-topic'})
#     @patch('event_processor.process_event')
#     def test_process_event_create_user(self, mock_process_iam_user_creation):
#         # Arrange
#         mock_process_iam_user_creation.return_value = {'statusCode': 200, 'body': 'Success'}
        
#         event = {
#             'time': '2025-03-15T00:00:00Z',
#             'detail': {
#                 'eventSource': 'iam.amazonaws.com',
#                 'eventName': 'CreateUser',
#                 'userIdentity': {'userName': 'admin'},
#                 'requestParameters': {'userName': 'newuser'}
#             },
#             'account': '123456789012',
#             'region': 'us-east-1'
#         }
        
#         # Act
#         result = process_event(event)
        
#         # Assert
#         self.assertEqual(result['statusCode'], 200)
#         mock_process_iam_user_creation.assert_called_once_with(event, '2025-03-15T00:00:00Z')
    
#     # @patch('event_processor.process_event')
#     # def test_process_event_create_access_key(self, mock_process_access_key_creation):
#     #     # Arrange
#     #     mock_process_access_key_creation.return_value = {'statusCode': 200, 'body': 'Success'}
        
#     #     event = {
#     #         'time': '2025-03-15T00:00:00Z',
#     #         'detail': {
#     #             'eventSource': 'iam.amazonaws.com',
#     #             'eventName': 'CreateAccessKey',
#     #             'userIdentity': {'userName': 'admin'},
#     #             'requestParameters': {'userName': 'targetuser'}
#     #         },
#     #         'account': '123456789012',
#     #         'region': 'us-east-1'
#     #     }
        
#     #     # Act
#     #     result = process_event(event)
        
#     #     # Assert
#     #     self.assertEqual(result['statusCode'], 200)
#     #     mock_process_access_key_creation.assert_called_once_with(event, '2025-03-15T00:00:00Z')
    
#     # def test_process_event_unhandled_event(self):
#     #     # Arrange
#     #     event = {
#     #         'time': '2025-03-15T00:00:00Z',
#     #         'detail': {
#     #             'eventSource': 'lambda.amazonaws.com',
#     #             'eventName': 'Invoke',
#     #             'userIdentity': {'userName': 'admin'}
#     #         },
#     #         'account': '123456789012',
#     #         'region': 'us-east-1'
#     #     }
        
#     #     # Act
#     #     result = process_event(event)
        
#     #     # Assert
#     #     self.assertEqual(result['statusCode'], 200)
#     #     self.assertIn('Event ignored', result['body'])
    
#     # @patch('event_processor.format_message')
#     # def test_process_iam_user_creation(self, mock_format_message, mock_send_notification):
#     #     # Arrange
#     #     mock_format_message.return_value = "Test message"
#     #     event = {
#     #         'time': '2025-03-15T00:00:00Z',
#     #         'detail': {
#     #             'eventSource': 'iam.amazonaws.com',
#     #             'eventName': 'CreateUser',
#     #             'userIdentity': {'userName': 'admin'},
#     #             'requestParameters': {'userName': 'newuser'}
#     #         },
#     #         'account': '123456789012',
#     #         'region': 'us-east-1'
#     #     }
        
#     #     # Act
#     #     result = process_event(event, '2025-03-15T00:00:00Z')
        
#     #     # Assert
#     #     self.assertEqual(result['statusCode'], 200)
#     #     mock_format_message.assert_called_once()
#     #     mock_send_notification.assert_called_once_with("Test message", "Alert: New IAM User Created")
    
#     # @patch('event_processor.format_message')
#     # def test_process_access_key_creation(self, mock_format_message, mock_send_notification):
#     #     # Arrange
#     #     mock_format_message.return_value = "Test message"
#     #     event = {
#     #         'time': '2025-03-15T00:00:00Z',
#     #         'detail': {
#     #             'eventSource': 'iam.amazonaws.com',
#     #             'eventName': 'CreateAccessKey',
#     #             'userIdentity': {'userName': 'admin'},
#     #             'requestParameters': {'userName': 'targetuser'}
#     #         },
#     #         'account': '123456789012',
#     #         'region': 'us-east-1'
#     #     }
        
#     #     # Act
#     #     result = process_event(event, '2025-03-15T00:00:00Z')
        
#     #     # Assert
#     #     self.assertEqual(result['statusCode'], 200)
#     #     mock_format_message.assert_called_once()
#     #     mock_send_notification.assert_called_once_with("Test message", "Alert: New IAM Access Key Created")
    
    
# if __name__ == '__main__':
#     unittest.main()
