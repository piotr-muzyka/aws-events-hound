import unittest

from utils import format_message

class TestUtils(unittest.TestCase):
    
    def test_format_message(self):
        # Arrange
        event_time = '2025-03-15T00:00:00Z'
        actor = 'admin'
        resource_arn = 'Resource ARN: arn:aws:iam::Unknown:user/doraemon'
        action = 'Action Performed: User creation'
        # Act
        message = format_message(event_time, actor, resource_arn, action)
        
        # Assert
        self.assertIn('Time: 2025-03-15T00:00:00Z', message)
        self.assertIn('Initiator: admin', message)
        self.assertIn('Resource ARN: arn:aws:iam::Unknown:user/doraemon', message)
        self.assertIn('Action Performed: User creation', message)


    def test_format_message_missing_fields(self):
        # Arrange
        event_time = '2025-03-15T00:00:00Z'
        actor = 'admin'
        resource_arn = 'Resource ARN: arn:aws:iam::Unknown:user/doraemon'
        action = 'User creation'

        # Act
        message = format_message(event_time, actor, resource_arn, action)
        
        # Assert
        self.assertIn('Time: 2025-03-15T00:00:00Z', message)
        self.assertIn('Initiator: admin', message)
        self.assertIn('Resource ARN: arn:aws:iam::Unknown:user/doraemon', message)
        self.assertIn('Action Performed: User creation', message)

if __name__ == '__main__':
    unittest.main()
