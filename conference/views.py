from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Speakers, Reports
from .forms import ReportsForm


def Main_view(request):
    speakers = Speakers.objects.order_by('speakers_name')
    return render(request, 'conference/main.html', {
        'speakers': speakers,
    })


def speakers_do(request, pk):
    speakers = Speakers.objects.filter(pk=pk)
    reports = Reports.objects.filter(speakers=speakers)
    return render(request, 'conference/speakersdo.html', {
        'speakers': speakers,
        'reports': reports,
    })


def reports_info(request, pk):
    reports = get_object_or_404(Reports, pk=pk)
    return render(request, 'conference/info.html', {
        'reports': reports,
    })


def reports_new(request):
    if request.method == "POST":
        form = ReportsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = ReportsForm()
            return render(request, 'conference/post_edit.html', {'form': form, 'ans': 'Добавлено!'})
        else:
            return render(request, 'conference/post_edit.html', {'form': form, 'ans': 'Форма не валидна'})
    else:
        form = ReportsForm()
        return render(request, 'conference/post_edit.html', {'form': form})


def reports_edit(request, pk):
    reports = get_object_or_404(Reports, pk=pk)
    if request.method == "POST":
        form = ReportsForm(request.POST, instance=reports)
        if form.is_valid():
            reports = form.save(commit=False)
            reports.save()
            return redirect('reports_info', pk=reports.pk)
    else:
        form = ReportsForm(instance=reports)
    return render(request, 'conference/post_edit.html', {'form': form})


def post_draft_list(request):
    reports = Reports.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'conference/post_draft_list.html', {'reports': reports})


def reports_publish(request, pk):
    reports = get_object_or_404(Reports, pk=pk)
    reports.publish()
    return redirect('reports_info', pk=pk)


def reports_remove(request, pk):
    reports = get_object_or_404(Reports, pk=pk)
    reports.delete()
    return redirect('Main_view')
