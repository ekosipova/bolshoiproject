from django.shortcuts import render
from dicts import persons,eng_rus_dict,cast

def all_cast(request):
    subdivisions = list(cast)
    subdivision_dict = {}
    for subdivion in subdivisions:
        subdivision_dict[subdivion] = eng_rus_dict[subdivion]
    data = {
        'subdivision': subdivision_dict
    }
    return render(request,'bolshoi_cast/mane_page.html',context=data)

def get_info_about_subdivision(request,subdivision:str):
    page = cast.get(subdivision)
    positions = {}
    for position in page:
        positions[position] = eng_rus_dict[position]
    data = {
        'positions':positions,
        'subdivision':subdivision,
        'rus_sub':eng_rus_dict[subdivision]
    }
    return render(request,'bolshoi_cast/info_subdivision.html', context=data)


def show_information_about_position(request,subdivision:str,position:str):
    for one_position in persons:
        if position in one_position:
            artists = persons[position]
            data = {
                'artists':artists,
                'position':eng_rus_dict[position]
                    }
            return render(request,'bolshoi_cast/info_position.html',context=data )

