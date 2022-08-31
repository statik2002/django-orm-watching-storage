import datetime
from django.utils import timezone
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def active_passcards_view(request):
    # Программируем здесь

    visits = Visit.objects.all()
    time_now = timezone.localtime()
    print(f"{time_now.isoformat(sep=' ', timespec='seconds')}")

    for visit in visits:
        if not visit.leaved_at:
            print(f"{visit} Находится в хранилище: {time_now-visit.entered_at}")

    active_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active_passcards,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
