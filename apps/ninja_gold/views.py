from django.shortcuts import render, redirect, HttpResponse
import arrow
import random
# Create your views here.
# This is the Django controller
def index(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
        request.session['log'] = []
    return render(request, 'ninja_gold/index.html')

def move(request):
    print '-' * 65 + ' move'
    if request.method == 'POST':
        move = request.POST['building']
        localTime = arrow.utcnow().to('US/Pacific')
        now = localTime.strftime('(%Y/%m/%d %I:%M %p)')
        building = {
            'farm':random.randrange(10,21),
            'cave':random.randrange(5,11),
            'house':random.randrange(2,6),
            'casino':random.randrange(-50,51)
        }
        if move in building:
            request.session['gold'] += building[move]
            request.session['log'].append((('red','green')[building[move] > 0],('Went to the {} and {} {} gold.{}').format(move,('lost', 'made')[building[move] > 0], building[move], now)))
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
