from django.shortcuts import render
from rest_framework import generics, permissions
from cis.models import Land, Shop, Faq
from cis.serializers import LandSerializer, ShopSerializer, FaqSerializer
from rest_framework.response import Response


class CombineListView(generics.ListAPIView):
    serializer_class_Land = LandSerializer
    serializer_class_Shop = ShopSerializer
    serializer_class_Faq = FaqSerializer

    def get_queryset_Land(self):
        return Land.objects.all()

    def get_queryset_Shop(self):
        return Shop.objects.all()

    def get_queryset_Faq(self):
        return Faq.objects.all()

    def list(self, request, *args, **kwargs):
        land = self.serializer_class_Land(self.get_queryset_Land(), many=True, context=self.get_serializer_context())
        shop = self.serializer_class_Shop(self.get_queryset_Shop(), many=True, context=self.get_serializer_context())
        faq = self.serializer_class_Faq(self.get_queryset_Faq(), many=True, context=self.get_serializer_context())
        return Response({
            "LAND": land.data,
            "SHOP": shop.data,
            "FAQ": faq.data
        })
# Create your views here.
