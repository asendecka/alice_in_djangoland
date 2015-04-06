from django.shortcuts import get_object_or_404, render, redirect

from .forms import WorkDoneForm
from .models import WorkDone

def work_done_edit(request, pk=None):
    instance = get_object_or_404(WorkDone.objects, pk=pk) if pk else None
    if request.method == "POST":
        form = WorkDoneForm(request.POST, instance=instance, user=request.user)
        if form.is_valid():
            instance = form.save()
            return redirect('work_done_list')
    else:
        form = WorkDoneForm(instance=instance, user=request.user)
    return render(request, 'time_tracker/work_done_edit.html', {'form': form})


def work_done_list(request):
    work_done = WorkDone.objects.all()
    return render(request, 'time_tracker/work_done_list.html',
                  {'work_done': work_done})
