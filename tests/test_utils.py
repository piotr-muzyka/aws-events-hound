import unittest

from src.utils import format_message

class TestUtils(unittest.TestCase):
    
    def test_format_message(self):
        # Arrange
        event_time = '2025-03-15T00:00:00Z'
        created_user_name = 'doraemon'
        actor = 'admin'
        event = {
            'account': '123456789012',
            'region': 'eu-central-1'
        }
        
        resource_arn = 'Resource ARN: arn:aws:iam::Unknown:user/newuser'
        action = 'Action Performed: User creation'
        # Act
        message = format_message(event_time, created_user_name, actor, event, resource_arn, action)
        
        # Assert
        self.assertIn('Time of Event: 2025-03-15T00:00:00Z', message)
        self.assertIn('New User Created: doraemon', message)
        self.assertIn('Initiator: admin', message)
        self.assertIn('AWS Account: 123456789012', message)
        self.assertIn('Region: eu-central-1', message)
        self.assertIn('Resource ARN: arn:aws:iam::Unknown:user/newuser', message)
        self.assertIn('Action Performed: User creation', message)


    def test_format_message_missing_fields(self):
        # Arrange
        event_time = '2025-03-15T00:00:00Z'
        created_user_name = 'doraemon'
        actor = 'admin'
        event = {}  # Missing account and region
        resource_arn = 'Resource ARN: arn:aws:iam::Unknown:user/newuser'
        action = 'User creation'

        # Act
        message = format_message(event_time, created_user_name, actor, event, resource_arn, action)
        
        # Assert
        self.assertIn('Time of Event: 2025-03-15T00:00:00Z', message)
        self.assertIn('New User Created: doraemon', message)
        self.assertIn('Initiator: admin', message)
        self.assertIn('AWS Account: Unknown', message)
        self.assertIn('Region: Unknown', message)
        self.assertIn('Resource ARN: arn:aws:iam::Unknown:user/newuser', message)
        self.assertIn('Action Performed: User creation', message)

if __name__ == '__main__':
    unittest.main()
