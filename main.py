import math
import argparse
from geopy.geocoders import Nominatim
from haversine import haversine
import folium
from geopy.extra.rate_limiter import RateLimiter
from random import uniform


def tass_points(list:list, index_to_tass):
    """
    Randomly tass points
    """
    move=0.008
    for i in index_to_tass:
        x_coef=uniform(-1,1)
        y_coef=uniform(-1,1)
        current_location=list[i][0]
        new_location=[0,0]
        new_location[0]=current_location[0]+x_coef*move
        new_location[1]=current_location[1]+y_coef*move
        list[i][0]=tuple(new_location)


parser = argparse.ArgumentParser()
parser.add_argument('year')           # positional argument
parser.add_argument('latitude')      # option that takes a value
parser.add_argument('longitude')
parser.add_argument('path_to_dataset')
args = parser.parse_args()
year_chose=args.year
latitude=float(args.latitude)
longitude=float(args.longitude)
path_to_dataset=args.path_to_dataset

geolocator = Nominatim(user_agent="film_points.py")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

with open(path_to_dataset,"r",encoding="utf-8") as film_spots:
    dictionary=[]
    counter=0
    # Gets location of certain year films spots
    while True:
        counter+=1
        line=film_spots.readline()
        if line:
            line_splited=line.split("\t")
            year=line_splited[0].split(" ")[-1]
            film_name=" ".join(line_splited[0].split(" ")[:-1])
            place_name=line_splited[-1].strip()
            if year_chose in year:
                try:
                    location = geocode(place_name)
                    print(counter)
                    coordinate = (location.latitude, location.longitude)
                    distance_to_cooedinate=haversine(coordinate,(latitude,longitude))
                    dictionary.append([coordinate,film_name,place_name,distance_to_cooedinate])
                except AttributeError:
                    pass
            else:
                continue
        else:
            break
    # Sorts and get the nearest film spots
    dictionary=sorted(dictionary,key=lambda film: film[-1])
    map = folium.Map(location=[latitude, longitude], zoom_start=3)
    fg_near_film_spot = folium.FeatureGroup(name="Near film spots")
    nearest=dictionary[:10]
    # Finds locations in the same place
    used_location=[]
    index_to_tass=[]
    for index,value in enumerate(nearest):
        if value[0] not in used_location:
            used_location.append(value[0])
        else:
            index_to_tass.append(index)
    # Tass points if they in the same place
    tass_points(dictionary,index_to_tass)
    # Add markers
    for film in dictionary[:10]:
        fg_near_film_spot.add_child(folium.Marker(location=[film[0][0], film[0][1]],
                            popup=f"Назва фільму:\n {film[1]}\n Назва місця:\n {film[2]}",
                            icon=folium.Icon()))
    print(nearest[-1][-1]+50)
    fg_near_film_area = folium.FeatureGroup(name="Near film Area")
    fg_near_film_area.add_child(folium.Circle(location=[latitude, longitude],
                                    popup=f'Area of close film spots of {year_chose} year',
                                    fill_color='#040',
                                    radius=(nearest[-1][-1]+100)*1000, weight=1, color="#004"))
    map.add_child(fg_near_film_spot)
    map.add_child(fg_near_film_area)
    map.add_child(folium.LayerControl())
    map.save('Map_Default.html')
