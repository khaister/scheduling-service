from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from core.services import scheduling_service


class RequestViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(
        methods=["get"],
        detail=False,
        url_path="next-available",
        url_name="next-available",
    )
    def next_available(self, request):
        latitude = request.query_params.get("lat")
        longitude = request.query_params.get("lon")
        if not latitude or not longitude:
            return Response(
                {"message": "Missing latitude or longitude"},
                status=HTTP_400_BAD_REQUEST,
            )

        appointment = scheduling_service.get_next_available_appointment(
            latitude, longitude
        )

        return Response(appointment or {"message": "No appointments available"})
