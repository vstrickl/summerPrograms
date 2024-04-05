from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages

from .forms import ApplicantsForm


# Create your views here.
def the_program(request):
    title = 'Summer Programs | Physique Magnifique'
    context = {
        'title': title,
    }
    return render(request, 'martial_arts.html', context)

def apply(request):
    title = 'Summer Programs | Physique Magnifique'

    if request.method == 'POST':
        form = ApplicantsForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Application submitted successfully!')
                return redirect('apply')  # Redirect to a success page or another relevant page
            else:
                # If the form is not valid
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' error'  # Add error class or handle as needed
                messages.error(request, 'Please correct the errors below.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
    else:
        form = ApplicantsForm()

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'application.html', context)