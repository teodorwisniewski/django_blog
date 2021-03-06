from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.template.loader import  render_to_string

montly_challenges = {
    "january": "Don't eat sugar!",
    "february": "Don't eat carbs!",
    "march": "Stay in keto",
    "april": "Read about flexible keto",
    "may": "increase carbs",
    "june": "leave keto",
    "july": None,
    "August": None,
    "September": None,
    "October": None,
    "November": None,
    "December": None
}

def index(request):
    months = list(montly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def test(request, var):
    return HttpResponse(f"What we got {var}")



def montly_challenge_by_number(request, month):

    months= list(montly_challenges.keys())
    forwarded_month = months[month-1] if len(months) >= month else "Not supported"
    print(months, (len(months)-1) > month , month, forwarded_month)
    return HttpResponseRedirect("/challenges/" + forwarded_month)


def montly_challenge(request, month):
    try:
        challenge_text = montly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })
    except:
        raise Http404()
