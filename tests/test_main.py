import unittest
from unittest.mock import patch, MagicMock

from src.main import lambda_handler

class TestLambdaHandler(unittest.TestCase):
    
    @patch('src.main.process_event')
    def test_lambda_handler_success(self, mock_process_event):
        # Arrange
        mock_process_event.return_value = {'statusCode': 200, 'body': 'Success'}
        event = {'detail': {'eventName': 'CreateUser'}}
        context = MagicMock()
        
        # Act
        result = lambda_handler(event, context)
        
        # Assert
        self.assertEqual(result['statusCode'], 200)
        mock_process_event.assert_called_once_with(event)
    
    @patch('src.main.process_event')
    def test_lambda_handler_exception(self, mock_process_event):
        # Arrange
        mock_process_event.side_effect = Exception("Test error")
        event = {'detail': {'eventName': 'CreateUser'}}
        context = MagicMock()
        
        # Act
        result = lambda_handler(event, context)
        
        # Assert
        self.assertEqual(result['statusCode'], 500)
        self.assertIn('Test error', result['body'])
        mock_process_event.assert_called_once_with(event)

if __name__ == '__main__':
    unittest.main()
