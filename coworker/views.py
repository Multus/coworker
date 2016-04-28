from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    current_user = request.user
    id = current_user.id
    print(current_user.id)
    return render(request, 'coworker/profile.html', {'id': id})  # Create your views here.
