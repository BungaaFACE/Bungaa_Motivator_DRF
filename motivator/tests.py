from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from motivator.models import Habit
from users.models import User


class HabitSubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user_with_telegram_id = User.objects.create(
            email='withid@example.com',
            first_name='withid',
            last_name='withid',
            password='testpassword123',
            telegram_id='1234567890',
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

        self.user_with_telegram_id.set_password('user')
        self.user_with_telegram_id.save()
        self.token_with_id = str(RefreshToken.for_user(self.user_with_telegram_id).access_token)


        self.user_without_telegram_id = User.objects.create(
            email='noid@example.com',
            first_name='noid',
            last_name='noid',
            password='testpassword123',
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )
        self.user_without_telegram_id.set_password('user')
        self.user_without_telegram_id.save()
        self.token_without_id = str(RefreshToken.for_user(self.user_without_telegram_id).access_token)
        
        
        self.habit = Habit.objects.create(
            user=self.user_with_telegram_id,
            place="home",
            time="13:00",
            action="do something",
            is_nice=False,
            period=5,
            reward="do another thing",
            time_to_do=60,
            is_public=True
        )
        self.habit.save()


    def test_create_habit(self):
        data = {
            "place": "home",
            "time": "13:00",
            "action": "do something",
            "is_nice": False,
            "period": 5,
            "reward": "do another thing",
            "time_to_do": 60,
            "is_public": True
            }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token_with_id}')
        
        response = self.client.post('/motivator/habits/create/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscription_with_tg(self):
        data = {'habit': self.habit.pk}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token_with_id}')
        
        response = self.client.post('/motivator/habits/subscribe/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscription_without_tg(self):
        data = {'habit': self.habit.pk}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token_without_id}')
        
        response = self.client.post('/motivator/habits/subscribe/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destroy_habit(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token_without_id}')
        
        response = self.client.delete(f'/motivator/habits/{self.habit.pk}/delete/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        pass