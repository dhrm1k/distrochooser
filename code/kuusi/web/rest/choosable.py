"""
kuusi
Copyright (C) 2014-2024  Christoph Müller  <mail@chmr.eu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from web.models import Choosable
from rest_framework import serializers
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, OpenApiResponse
from rest_framework import status
from kuusi.settings import LANGUAGE_CODES
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from typing import Dict, Any

CHOOSABLE_SERIALIZER_BASE_FIELDS = ('id', 'name', 'description', 'bg_color', 'fg_color', 'meta')

class ChoosableSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    meta = serializers.SerializerMethodField()
    class Meta:
        model = Choosable
        fields = CHOOSABLE_SERIALIZER_BASE_FIELDS
    def get_description(self, obj: Choosable) -> str:
        return obj.__("description",   "en") # self.context['request'].query_params["lang"]) # FIXME: Decide how to inject this. Maybe get rid of this endpoint...
    def get_meta(self, obj: Choosable) -> Dict[str, Any]:
        meta_values = obj.meta
        for key, value in meta_values.items():
            meta_values[key] = value.meta_value
        return meta_values
    
class ChoosableViewSet(ListModelMixin, GenericViewSet):
    queryset = Choosable.objects.all()
    serializer_class = ChoosableSerializer

    @extend_schema(
        parameters=[
          OpenApiParameter("lang", OpenApiTypes.STR, OpenApiParameter.QUERY,description="The language code to translate this values", required=True),
        ],
        responses={
            status.HTTP_200_OK: OpenApiResponse(response=ChoosableSerializer, description="The list of Choosables available to use"),
            status.HTTP_412_PRECONDITION_FAILED: OpenApiResponse(description='Invalid language'),
        }
    )
    def list(self, request,  *args, **kwargs):
        lang = request.query_params.get('lang')
        if lang not in LANGUAGE_CODES:
            return Response(status=status.HTTP_412_PRECONDITION_FAILED)
        return super().list(request, *args, **kwargs)
