from django.shortcuts import render

# Create your views here.
def count_view(request):
    count_str = request.COOKIES.get('count', '0')
    count = int(count_str)
    new_count = count + 1
    response = render(request, 'cookieapp/cookieapp.html', {'count': new_count})
    response.set_cookie('count', str(new_count), max_age=None)  # Convert new_count to a string
    return response
 