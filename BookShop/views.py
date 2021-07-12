from django.http import HttpResponse

def home(request):
  return HttpResponse("<br/><center><h1 style='background-color'=red>Reza Rezaee></h1><br/><p>This website programed by django drf for practice API web</p></center")
