from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from main.serializers import UserSerializer
from main.tasks import open_tab


class EdstemTestViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['put'])
    def tab(self, request, pk=None):
        urls = [
            'https://www.edstem.com/',
            'https://www.edstem.com/contact-us/',
            'https://www.edstem.com/approach',
            'https://www.edstem.com/blogs',
            'https://www.edstem.com/',
        ]
        open_tab.delay(urls=urls)
        custom_data = {
            "status": True,
            "message": 'Your tabs will open soon.',
        }
        return Response(custom_data, status=status.HTTP_200_OK)
