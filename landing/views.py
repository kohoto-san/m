from django.shortcuts import render
from django.views.generic import CreateView

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest

from landing.models import Person
from landing.forms import PersonForm

import json


class PersonCreate(CreateView):
    model = Person
    fields = ['email']
    template_name = 'test.html'

    def get_success_url(self):
        return '/thanks'


def person_create(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            p = Person.objects.create(email=form.cleaned_data['email'])
            p.save()
            return HttpResponse('valid')
        else:
            if request.is_ajax():
                # Prepare JSON for parsing
                errors_dict = {}
                if form.errors:
                    for error in form.errors:
                        e = form.errors[error]
                        errors_dict[error] = unicode(e)

                return HttpResponseBadRequest(json.dumps(errors_dict))

            # return HttpResponse('NO valid')


    # if a GET (or any other method) we'll create a blank form
    # else:
        # form = PersonForm()


    # return render(request, 'name.html', {'form': form})


def index(request):
    form = PersonForm(label_suffix='')
    return render(request, 'index.html', {'form': form})


def search(request):
    return render(request, 'search.html')


"""
class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = PersonForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
"""
