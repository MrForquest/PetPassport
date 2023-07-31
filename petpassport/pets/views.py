import rest_framework.generics
import rest_framework.permissions
import rest_framework.response
import rest_framework.views

import pets.models
from pets.serializers import PetDetailSerializer, PetListSerializer


class PetList(rest_framework.generics.ListCreateAPIView):
    permission_classes = [rest_framework.permissions.IsAuthenticated]
    queryset = pets.models.Pet.objects.pet_list()
    swagger_tags = ["pets"]

    def get_serializer_class(
        self, instance=None, data=None, many=False, partial=False
    ):
        method = self.request.method
        if method == "POST":
            return PetDetailSerializer
        else:
            return PetListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return rest_framework.response.Response(data={"pets": serializer.data})


class PetDetail(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [rest_framework.permissions.IsAuthenticated]
    queryset = pets.models.Pet.objects.all()
    serializer_class = PetDetailSerializer
    swagger_tags = ["pets"]
