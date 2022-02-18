from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import  render_to_string

montly_challenges = {
    "january": "Don't eat sugar!",
    "february": "Don't eat carbs!",
    "march": "Stay in keto",
    "april": "Read about flexible keto",
    "may": "increase carbs",
    "june": "leave keto",
}

def index(request):
    challenge_text = render_to_string("challenges/challenge.html")
    return render(request, "challenges/challenge.html")


def test(request, var):
    return HttpResponse(f"What we got {var}")



def montly_challenge_by_number(request, month):

    months= list(montly_challenges.keys())
    forwarded_month = months[month-1] if len(months) >= month else "Not supported"
    print(months, (len(months)-1) > month , month, forwarded_month)
    return HttpResponseRedirect("/challenges/" + forwarded_month)


def montly_challenge(request, month):
    # challenge_text = montly_challenges.get(month, HttpResponseNotFound("This month is not supported"))
    return render(request, "challenges/challenge.html")
