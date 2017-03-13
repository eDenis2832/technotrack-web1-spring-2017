from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request, post_id=None):
    arr = ["111", "222", "333"]
    return render(request, "core/file.html", {"post_id": post_id, "arr": arr})




