from rest_framework import serializers
from motivator.models import Habit, HabitSubscription
from motivator.validators import AdditionalHabitIsNiceValidator, IsPublicHabitHasPublicAddHabitValidator, NiceHabitNoRewardValidator, PeriodWeeklyOrLessValidator, RewardOrHabitValidator, TimeToDoLess120Validator, UserHasTelegramIDValidator


class HabitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Habit
        exclude = ['user']
        validators = [
            RewardOrHabitValidator(
                add_habit_field='related_habit',
                reward_field='reward',
                is_nice_field='is_nice'),
            TimeToDoLess120Validator(time_to_do_field='time_to_do'),
            AdditionalHabitIsNiceValidator(habit_field='related_habit'),
            NiceHabitNoRewardValidator(
                is_nice_field='is_nice',
                add_habit_field='related_habit',
                reward_field='reward'),
            PeriodWeeklyOrLessValidator(period_field='period'),
            IsPublicHabitHasPublicAddHabitValidator(
                is_public_fied='is_public',
                add_habit_field='related_habit')
        ]


class HabitSubscriptionSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Проверка есть ли у пользователя telegram id
        """
        if not self.context['request'].user.telegram_id:
            raise serializers.ValidationError("Вы должны добавить Telegram ID в профиль для подписки.")
        return data
    
    class Meta:
        model = HabitSubscription
        fields = ['id', 'user', 'habit']
        extra_kwargs = {
            'user' : {'read_only' : True}
        }