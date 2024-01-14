from rest_framework import generics
from motivator.models import Habit, HabitSubscription
from motivator.pagination import PagintaionFiveTwenty
from motivator.permissions import IsCreatorClass, IsPublicHabitClass, IsSuClass
from motivator.serializers import HabitCreateUpdateSerializer, HabitSerializer, HabitSubscriptionSerializer
from motivator import tasks


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = PagintaionFiveTwenty

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = PagintaionFiveTwenty

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsCreatorClass|IsPublicHabitClass|IsSuClass]


class HabitCreateAPIView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateUpdateSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateUpdateSerializer
    permission_classes = [IsCreatorClass]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsCreatorClass]


class HabitSubscriptionListAPIView(generics.ListAPIView):
    serializer_class = HabitSubscriptionSerializer
    pagination_class = PagintaionFiveTwenty

    def get_queryset(self):
        return HabitSubscription.objects.filter(user=self.request.user)


class HabitSubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = HabitSubscription.objects.all()
    serializer_class = HabitSubscriptionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitSubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = HabitSubscription.objects.all()
    serializer_class = HabitSubscriptionSerializer
    permission_classes = [IsCreatorClass]
