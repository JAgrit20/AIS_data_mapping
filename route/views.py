import folium
from django.shortcuts import render,redirect
from . import getroute
from django.db.models import Q
from .models import AIS_data_routes,AIS_data_report
import asyncio
import websockets
import json
from datetime import datetime, timezone
import time
from django.http import HttpResponse

coordinates_list = []
async def connect_ais_stream(request):
    figure = folium.Figure()
    start_time = time.time()
    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        subscribe_message = {"APIKey": "e767a56991a5d8bc14141f59c68a29e02f1c5c19", "BoundingBoxes":  [[[25.835302, -80.207729], [25.602700, -79.879297]], [[33.772292, -118.356139], [33.673490, -118.095731]] ]}

        subscribe_message_json = json.dumps(subscribe_message)
        await websocket.send(subscribe_message_json)

        async for message_json in websocket:
            message = json.loads(message_json)
            message_type = message["MessageType"]

            if message_type == "PositionReport":
                # the message parameter contains a key of the message type which contains the message itself
                ais_message = message['Message']['PositionReport']
                print(f"[{datetime.now(timezone.utc)}] ShipId: {ais_message['UserID']} Latitude: {ais_message['Latitude']} Longitude: {ais_message['Longitude']}")
                print("time.time()",time.time(),"ss", start_time)
                column1 = float(ais_message['Latitude'])
                column2 = float(ais_message['Longitude'])
                t = (column1, column2)
                coordinates_list.append(t)
                ans = (float(time.time())-float(start_time))>5
                if(ans):
                    m = folium.Map(location=coordinates_list[1],
                        zoom_start=10)
                    m.add_to(figure)
                    folium.Marker(location=coordinates_list[1], tooltip = f'location: {coordinates_list[1]} ',icon=folium.Icon(icon='stop', color='red')).add_to(m)
                    folium.Marker(location=coordinates_list[2], tooltip = f'location: {coordinates_list[2]} ',icon=folium.Icon(icon='stop', color='blue')).add_to(m)
                    folium.Marker(location=coordinates_list[4], tooltip = f'location: {coordinates_list[3]} ',icon=folium.Icon(icon='stop', color='cyan')).add_to(m)
                    folium.Marker(location=coordinates_list[3], tooltip = f'location: {coordinates_list[4]} ',icon=folium.Icon(icon='stop', color='green')).add_to(m)
                    figure.render()
                    context={'map':figure}
                    return render(request,'showroute.html',context)
                    # return HttpResponse(f' Done 5 sec{ans}')
                # if(time.time()- start_time > 5):
                #     return HttpResponse("Done 5 sec")

def showmap(request): 
    return render(request,'showmap.html')
def showreport(request):
    ans = AIS_data_report.objects.all()
    context = {'mydata':ans}
 

    return render(request,'report.html',context)

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


    folium.PolyLine(coordinates_list,weight=5,color='blue',opacity=0.6).add_to(m)
    folium.Marker(location=coordinates_list[0],icon=folium.Icon(icon='play', color='blue')).add_to(m)
    folium.Marker(location=coordinates_list[-1],icon=folium.Icon(icon='stop', color='red')).add_to(m)
#     folium.Marker(
#     location=start_point,
#     icon=folium.Icon(color="red",icon="sailboat", prefix='fa')
# ).add_to(m)
    figure.render()
    context={'map':figure}
    return render(request,'showroute.html',context)
