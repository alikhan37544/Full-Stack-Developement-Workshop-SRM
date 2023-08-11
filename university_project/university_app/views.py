from django.shortcuts import render

def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'index.html', context)

def academics(request):
    return render(request, 'academics.html')

def research(request):
    return render(request, 'research.html')

def campus_life(request):
    return render(request, 'campus_life.html')

def international(request):
    return render(request, 'international.html')

def about(request):
    return render(request, 'about.html')

def controller_of_examinations(request):
    return render(request, 'controller_of_examinations.html')

def department_finder(request):
    return render(request, 'department_finder.html')

def staff_finder(request):
    return render(request, 'staff_finder.html')

def program_finder(request):
    return render(request, 'program_finder.html')

def news(request):
    return render(request, 'news.html')
