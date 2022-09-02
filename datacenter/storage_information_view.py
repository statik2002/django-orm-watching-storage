from django.utils import timezone
from datacenter.models import Visit
from django.shortcuts import render

from .passcard_info_view import format_duration


def storage_information_view(request):

    visits = Visit.objects.all()
    time_now = timezone.localtime()

    non_closed_visits = []

    for visit in visits:
        if not visit.leaved_at:
            time_delta = (time_now - visit.entered_at).total_seconds()

            visit_element = {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(time_delta),
            }
            non_closed_visits.append(visit_element)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
