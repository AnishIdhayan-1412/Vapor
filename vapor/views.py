from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from vapor.models import Confession
from vapor.forms import ConfessionForm

def feed(request):
    confessions=Confession.objects.filter(
        is_removed=False
    ).order_by('-created_at')

    context={
        'confessions': confessions
    }
    return render(request,'feed.html',context)
def submit(request):
    if request.method=='POST':
        form=ConfessionForm(request.POST)
        if form.is_valid():
            Confession.objects.create(
                text=form.cleaned_data['text']
            )
            return redirect('feed')
    else:
        form=ConfessionForm()
    return render(request,'submit.html',{'form':form})

def report(request,id):
    if request.method=="POST":
        confession=get_object_or_404(Confession,id=id)
        confession.report_count+=1
        if confession.report_count>=3:
            confession.is_removed=True
        confession.save()
    return redirect