import datetime

def get_current_year(request):
    current_year = datetime.datetime.now().year
    current_seconds = datetime.datetime.now().second
#los valores de current_year y current_seconds son globales en todos los templates
    return {
        "current_year": current_year, "current_seconds":current_seconds
    }