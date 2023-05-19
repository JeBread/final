from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests,random
from django.core import serializers

# Create your views here.
@api_view(['GET',])
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieListSerializer(movies,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie=Movie.objects.get(pk=movie_pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_data_extract(request):
    titles=[]
    ostList=[]
    videos=[]

    with open("./movies/movieList.txt", "r",encoding='UTF8') as f:
        for line in f:
            #print(line.strip())
            idx=line.find('.')
            titles.append(line.strip()[idx+2:])
    #print(titles)

    with open("./movies/ostList.txt", "r",encoding='UTF8') as f:
        for line in f:
            #print(line.strip())
            idx=line.find('.')
            ostList.append(line.strip()[idx+2:])
    #print(ostList)

    with open("./movies/videoList.txt", "r",encoding='UTF8') as f:
        for line in f:
            #print(line.strip())
            idx=line.find('.')
            videos.append(line.strip()[idx+2:])
    #print(videos)

    i=0
    for title in titles:
        url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=ko-kor&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NDUzMDhmZTI1NGVmMTAzZDlhMGU3YTQ1MWJjYTRiNSIsInN1YiI6IjYzZDMxNjhiZTcyZmU4MDBiMjA1NDA5MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1aBx6rOU9lnDeivuTxsmDYNg8zz4zvRWyGGwPAWobzI"
        }

        response = requests.get(url, headers=headers).json()
        print(i+1,end=' ')
        i+=1
        for res in response["results"]:
            if res["title"]==title and res['vote_average']>0:
                print(res["title"])
                print(ostList[i-1])
                print(videos[i-1])
                print(res['release_date'])
                movie=Movie.objects.create(
                    title=res.get('title'),
                    release_date=res.get('release_date'),
                    vote_average=res.get('vote_average'),
                    overview=res.get('overview'),
                    poster_path=res.get('poster_path'),
                    ost=ostList[i-1],
                    video=videos[i-1],
                )
                movie.save()    
                break
        print("----------------------------------------")
    return Response()

@api_view(['GET'])
def ostQuiz(request):
    ids=random.sample(range(1,51),3)
    movie1=Movie.objects.filter(pk=ids[0])
    movie2=Movie.objects.filter(pk=ids[1])
    movie3=Movie.objects.filter(pk=ids[2])
    print(ids)
    return Response(data={
        "correct":serializers.serialize('json', movie1),
        'uncorrect1':serializers.serialize('json', movie2),
        'uncorrect2':serializers.serialize('json', movie3),
    })
    
