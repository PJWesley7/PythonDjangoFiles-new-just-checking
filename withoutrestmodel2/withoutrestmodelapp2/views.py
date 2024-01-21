from django.shortcuts import render
from django.views.generic import View
from withoutrestmodelapp2.utils import is_json
from withoutrestmodelapp2.mixins import HttpResponseMixin,SerializeMixin
from withoutrestmodelapp2.models import Student
import json


# Create your views here.
class StudentCRUDCBV(View,HttpResponseMixin,SerializeMixin):
    def get_object_by_id(self,id):
        try:
            s=Student.objects.get(id=id)
        except:
            s=None
        return s
    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Please provide a valid json'}),status=400)
        pdata=json.loads(data)
        id = pdata.get('id',None)
        if id is not None:
            std=self.get_object_by_id(id)
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'No matched record found with that id'}),status=400)
            json_data = self.serialize(['std',])
            return self.render_to_http_response(json_data)
        qs=Student.objects.all
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)


