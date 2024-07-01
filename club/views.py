import calendar
from datetime import date, datetime, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from .models import Schedule, Dashboard, Post
from django.urls import reverse_lazy
from .forms import ScheduleForm, DashboardForm, PostForm


# 일정 뷰
def schedule_list(request, year=None, month=None):
    if year is None:
        year = date.today().year
    if month is None:
        month = date.today().month

    cal = calendar.Calendar()
    month_days = [[date(year, month, day) if day != 0 else None for day in week] for week in
                  cal.monthdayscalendar(year, month)]

    schedules = Schedule.objects.filter(date__year=year, date__month=month)

    previous_month = (datetime(year, month, 1) - timedelta(days=1)).month
    previous_year = (datetime(year, month, 1) - timedelta(days=1)).year
    next_month = (datetime(year, month, 28) + timedelta(days=4)).month
    next_year = (datetime(year, month, 28) + timedelta(days=4)).year

    context = {
        'calendar': month_days,
        'schedules': schedules,
        'year': year,
        'month': month,
        'previous_month': previous_month,
        'previous_year': previous_year,
        'next_month': next_month,
        'next_year': next_year,
    }
    return render(request, 'club/schedule_list.html', context)


def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'club/schedule_form.html', {'form': form})


def schedule_update(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'club/schedule_form.html', {'form': form})


def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')
    return render(request, 'club/schedule_confirm_delete.html', {'object': schedule})


# 대시보드 뷰
def dashboard_view(request):
    dashboards = Dashboard.objects.all()
    return render(request, 'club/dashboard.html', {'object_list': dashboards})


def dashboard_create(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DashboardForm()
    return render(request, 'club/dashboard_form.html', {'form': form})


def dashboard_update(request, pk):
    dashboard = get_object_or_404(Dashboard, pk=pk)
    if request.method == 'POST':
        form = DashboardForm(request.POST, instance=dashboard)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DashboardForm(instance=dashboard)
    return render(request, 'club/dashboard_form.html', {'form': form})


def dashboard_delete(request, pk):
    dashboard = get_object_or_404(Dashboard, pk=pk)
    if request.method == 'POST':
        dashboard.delete()
        return redirect('dashboard')
    return render(request, 'club/dashboard_confirm_delete.html', {'object': dashboard})


# 게시글 뷰
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'club/post_list.html', {'object_list': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'club/post_detail.html', {'object': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'club/post_form.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'club/post_form.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'club/post_confirm_delete.html', {'object': post})
