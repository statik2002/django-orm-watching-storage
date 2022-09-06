from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone


def get_duration(visit):
    if not visit.leaved_at:
        return (timezone.localtime() - visit.entered_at).total_seconds()
    return (visit.leaved_at - visit.entered_at).total_seconds()


def is_visit_long(visit, minutes=60):
    return get_duration(visit) > minutes*60


def format_duration(time_delta):
    return '{:02}:{:02}:{:02}'.format(int(time_delta // 3600),
                                      int(time_delta % 3600 // 60),
                                      int(time_delta % 60),
                                      )


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)

    passcard_visits = get_list_or_404(Visit, passcard=passcard)

    this_passcard_visits = []

    for passcard_visit in passcard_visits:

        time_delta = get_duration(passcard_visit)

        visit = {
            'entered_at': passcard_visit.entered_at,
            'duration': format_duration(time_delta),
            'is_strange': is_visit_long(passcard_visit),
        }

        this_passcard_visits.append(visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
