from beauty_salon.forms import AuthenticationForm


def get_context_data(request):
    context = {
        'auth': AuthenticationForm()
    }
    return context
