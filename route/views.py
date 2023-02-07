import folium
from django.shortcuts import render,redirect
from . import getroute
from django.db.models import Q
from .models import AIS_data_routes


def showmap(request):
    return render(request,'showmap.html')

def home(request):
    results = AIS_data_routes.objects.all()[:500].values();
    context = {'mydata':results}
    return render(request,'index.html', context)

def reports(request):
    return render(request,'index.html')
def showroute(request):
    figure = folium.Figure()
    # lat1,long1,lat2,long2=float(lat1),float(long1),float(lat2),float(long2)
    # route=getroute.get_route(long1,lat1,long2,lat2)

    lat1 = request.POST['selected_id']
    print(lat1)
    query = lat1
    results = AIS_data_routes.objects.filter(Ship_id=query)

    coordinates_list = []
    start_point = []
    # coordinates_list = []
    for  index,obj in enumerate(results):
        if(index==1):
            column01= float(obj.Latitude)
            column02 = float(obj.Logitude)
            start_point.append(column01)
            start_point.append(column02)
        column1 = float(obj.Latitude)
        column2 = float(obj.Logitude)

        t = (column1, column2)
        coordinates_list.append(t)
    print(start_point)
    
    m = folium.Map(location=start_point,
                       zoom_start=10)
    m.add_to(figure)
    # print("route",route['route'])
    # print("route",route)


    folium.PolyLine(coordinates_list,weight=8,color='blue',opacity=0.6).add_to(m)
    folium.Marker(location=coordinates_list[0],icon=folium.Icon(icon='play', color='blue')).add_to(m)
    folium.Marker(location=coordinates_list[-1],icon=folium.Icon(icon='stop', color='red')).add_to(m)
#     folium.Marker(
#     location=start_point,
#     icon=folium.Icon(color="red",icon="sailboat", prefix='fa')
# ).add_to(m)
    figure.render()
    context={'map':figure}
    return render(request,'showroute.html',context)
