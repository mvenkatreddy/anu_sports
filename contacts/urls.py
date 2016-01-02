from django.conf.urls import include, url
from django.views.generic import TemplateView


from .views import contactPage

urlpatterns = [
	url(r'^$', contactPage, name="contact_page"),
	url(r'^thanks/$', TemplateView.as_view(template_name="contacts/thankyou.html"),
		name="thank_page"),
]