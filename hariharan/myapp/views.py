from django.shortcuts import render
def churn_rate(request):
    h = float(request.POST.get('inital', '0'))
    a = float(request.POST.get('lost', '0'))
    ChurnRate = (a / h) * 100 if request.method == 'POST' else 0
    print("inital =",h)
    print("lost =",a)
    print("Churn Rate=",ChurnRate)
    return render(request, 'myapp/math.html',{'h': h, 'a': a, 'ChurnRate': ChurnRate})
