from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from .models import Contact
from .forms import ContactForm

from .utils import send_mail_admin


def contactPage(request, template="contacts/contact.html"):
	import ipdb; ipdb.set_trace()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			message = form.cleaned_data['message']
			email = form.cleaned_data['email']
			send_mail_admin(message, email)
			return redirect('thank_page')
			
	else:
		form = ContactForm()
	kwvars = {'form': form}
    
	return render_to_response(
		template, kwvars, RequestContext(request))
