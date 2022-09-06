from django.utils import timezone
from datacenter.models import Visit
from django.shortcuts import render

from .passcard_info_view import format_duration, get_duration


def storage_information_view(request):

    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in visits:

        visit_element = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
        }
        non_closed_visits.append(visit_element)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
