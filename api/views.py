from django.http import Http404
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from viewer.models import Media

from .serializers import MediaSerializer


class MediaView(APIView, LimitOffsetPagination):
    parser_class = (FileUploadParser,)
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=-1, *args, **kwargs):
        if pk == -1:
            page = self.paginate_queryset(self.queryset, request)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return self.get_paginated_response(serializer.data)
        try:
            media = Media.objects.get(pk=pk)
        except Media.DoesNotExist:
            raise Http404
        serializer = self.serializer_class(media)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        raise NotImplementedError

    def patch(self, request, *args, **kwargs):
        raise NotImplementedError

    def delete(self, request, *args, **kwargs):
        raise NotImplementedError
