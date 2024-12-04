from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'login.html', {'user': request.user})

def login_by_telegram(request):
    bot_username = 'bday_present_bot'
    token = request.user.username if request.user.is_authenticated else 'unique_login_token'
    telegram_login_url = f'https://t.me/{bot_username}?start={token}'
    return render(request, 'login.html', {'telegram_login_url': telegram_login_url})


def check_auth_status(request):
    if request.user.is_authenticated:
        return JsonResponse({'is_authenticated': True, 'username': request.user.username})
    return JsonResponse({'is_authenticated': False})
