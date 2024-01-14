from motivator.views import HabitCreateAPIView, HabitDestroyAPIView, HabitListAPIView, HabitPublicListAPIView, HabitRetrieveAPIView, HabitSubscriptionCreateAPIView, HabitSubscriptionDestroyAPIView, HabitSubscriptionListAPIView, HabitUpdateAPIView
from users.apps import UsersConfig
from django.urls import path
app_name = UsersConfig.name


urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habit_list'),
    path('habits/public/', HabitPublicListAPIView.as_view(), name='habit_public_list'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habits/<int:pk>/retrieve/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habits/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habits/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habits/subscribe_list/', HabitSubscriptionListAPIView.as_view(), name='habit_sub_list'),
    path('habits/subscribe/', HabitSubscriptionCreateAPIView.as_view(), name='habit_sub_create'),
    path('habits/<int:pk>/unsubscribe/', HabitSubscriptionDestroyAPIView.as_view(), name='habit_sub_delete'),
]
