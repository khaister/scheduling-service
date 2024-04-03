from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class RequestViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['get'], detail=False, url_path='next-available', url_name='next-available')
    def next_available(self, request):
        return Response({'message': 'Next available appointment'})
