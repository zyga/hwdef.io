from tastypie.resources import ModelResource

from hwdefio.hwdef.models import Hardware


class HardwareResource(ModelResource):

    class Meta:
        queryset = Hardware.objects.all()
