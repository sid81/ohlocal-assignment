from django.shortcuts import render
from core.models import Country, States, Districts,City


def index(request):
    countryid = request.GET.get('country', None)
    stateid = request.GET.get('states', None)
    districtid= request.GET.get('districts', None)
    states = None
    districts = None
    if countryid:
        getcountry = Country.objects.get(id=countryid)
        state = States.objects.filter(country=getcountry)
    if stateid:
        getstate = States.objects.get(id=stateid)
        district = Districts.objects.filter(state=getstate)
    if districtid:
        getdistrict=Districts.objects.get(id=districtid)
        city=City.objects.filter(district=getdistrict)
    country = Country.objects.all()
    return render(request, 'index.html', locals())