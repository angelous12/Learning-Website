from django.contrib.auth.decorators import login_required
from page.models import InfoContact


def infocontact(request):          
        info = InfoContact.objects.first()
        return {'infocontact':info}
        