from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

montly_challenges = {
    1: "Don't eat sugar!",
    2: "Don't eat carbs!",
    3: "Stay in keto",
    4: "Read about flexible keto",
    5: "increase carbs",
    6: "leave keto",
}

def index(request):
    return HttpResponse("Choose your month challenge!")


def test(request, var):
    return HttpResponse(f"What we got {var}")



def montly_challenge_by_number(request, month):

    challenge_text = montly_challenges.get(month, HttpResponseNotFound("This month is not supported"))
    return HttpResponse(challenge_text)


def montly_challenge(request, month):
    challenge_text = montly_challenges.get(month, HttpResponseNotFound("This month is not supported"))
    return HttpResponse(challenge_text)