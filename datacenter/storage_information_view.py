from django.utils import timezone
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь

    visits = Visit.objects.all()
    time_now = timezone.localtime()

    non_closed_visits = []

    for visit in visits:
        visit_element = {}
        if not visit.leaved_at:
            time_delta = (time_now - visit.entered_at).total_seconds()
            string_timedelta = "{:02}:{:02}:{:02}".format(int(time_delta // 3600), int(time_delta % 3600 // 60),
                                                          int(time_delta % 60))
            visit_element['who_entered'] = visit.passcard
            visit_element['entered_at'] = visit.entered_at
            visit_element['duration'] = string_timedelta
            non_closed_visits.append(visit_element)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
