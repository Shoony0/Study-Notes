from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
fake = Faker()
from home.models import Student
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity, SearchHeadline
from django.db.models import Q, F





# Create your views here.

def index(request):
    # for _ in range(10000):

    #     Student.objects.create(
    #         name=fake.name(),
    #         email=fake.email(),
    #         subject=fake.name(),
    #         father_name=fake.name(),
    #         mother_name=fake.name(),
    #         address=fake.address()
    #     )

    search = request.GET.get("search")
    # query = SearchQuery(search)
    # vector = SearchVector(
    #     "name",
    #     "email",
    #     "subject",
    #     "father_name",
    #     "mother_name",
    #     "address",
    # )

    # rank = SearchRank(vector, query)

    # similarity = TrigramSimilarity("email", search) + TrigramSimilarity("email", search) + TrigramSimilarity("subject", search) + TrigramSimilarity("father_name", search) + TrigramSimilarity("mother_name", search)+ TrigramSimilarity("address", search)
                
                

    # result = Student.objects.annotate(
    #     rank=rank,
    #     similarity=similarity,
    # ).filter(
    #    Q(rank__gte=0.3) | Q(similarity__gte=0.3)
    # ).distinct().order_by(
    #    "-rank", "-similarity"
    # )

    # if search is not None:
    #     query = SearchQuery(search)
    #     vector = (
    #         SearchVector("name", weight="A")
    #         + SearchVector("email", weight="B")
    #         + SearchVector("subject", weight="C")
    #         + SearchVector("address", weight="C")
    #     )
    #     rank = SearchRank(vector, query)
    #     result = Student.objects.annotate(
    #         rank=rank
    #     ).filter(rank__gte=0.1).order_by("-rank")
    if search is not None:
        split_seach = search.split(' ')
        # query = SearchQuery(search, search_type="phrase")
        query = SearchQuery(split_seach[0]) | SearchQuery(split_seach[1]) | SearchQuery(split_seach[2])
        vector = (
            SearchVector("name", weight="A")
            + SearchVector("email", weight="B")
            + SearchVector("subject", weight="C")
            + SearchVector("address", weight="C")
        )
        rank = SearchRank(vector, query)
        result = Student.objects.annotate(
            rank = rank
        ).filter(rank__gte=0.1).order_by("-rank")
        
    if search is not None:
        split_seach = search.split(' ')
        # query = SearchQuery(search, search_type="phrase")
        query = SearchQuery(split_seach[0]) | SearchQuery(split_seach[1]) | SearchQuery(split_seach[2])
        vector = (
            SearchVector("name", weight="A")
            + SearchVector("email", weight="B")
            + SearchVector("subject", weight="C")
            + SearchVector("address", weight="C")
        )
        rank = SearchRank(vector, query)
        result = Student.objects.annotate(
            rank = rank
        ).filter(rank__gte=0.1).order_by("-rank")
    else:
        result = Student.objects.all() 

    context = {
        "result": result,
        "search": search,
    }
    return render(request, 'index.html', context=context)

def dynamic_route(request, number):
    return HttpResponse(f"Reponse from Dynamic Route {number}")
