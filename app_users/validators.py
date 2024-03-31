from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from app_users.models import User


class TrueInviteCodeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value_dict):
        if active_invite_code := value_dict.get(self.field):
            try:
                get_object_or_404(User, invite_code=active_invite_code)
            except Http404:
                raise serializers.ValidationError({'detail': 'invite code не существует'})
