from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

#from pagemenu.pagemenus import DateFieldIntervalPageMenu
from contact.forms import ContactForm
from contact.models import ContactOptions

class GenericContactPage(object):
    '''
    def get_pagemenu(self, request, queryset, *args, **kwargs):
        raise NotImplementedError('%s should implement get_pagemenu.' % self.__class__)
    '''
    def get_form_class(self):
        return ContactForm
        
    def get_template_name(self):
        return 'contact/contact-us.html'
    
    def get_object(self):
        return ContactOptions.objects.latest('id')
    
    def get_recipients(self, obj):
        obj = self.get_object()
        if obj:
            return [recipient.email for recipient in obj.email_recipients.all()]
        return []

        '''
        if settings:
            contact_email_recipients = settings[0].contact_email_recipients
            if contact_email_recipients:
                split_recipients = [recipient.replace('\r', '') for recipient in contact_email_recipients.split('\n')]
                for recipient in split_recipients:
                    if recipient:
                        recipients.append(recipient)
        '''
    
    def init_form(self, request, form_class, recipients):
        form = form_class()
        if request.POST:
            post_data = request.POST.copy()
            form = ContactForm(post_data)
            if form.is_valid():
                form.send_message(recipients)
        return form

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __call__(self, request, *args, **kwargs):
        
        #self.pagemenu = kwargs.get('pagemenu', getattr(self, 'pagemenu', self.get_pagemenu()))
        contact_object = self.get_object()
        form_class = kwargs.get('form_class', getattr(self, 'form_class', self.get_form_class()))
        recipients = kwargs.get('recipients', getattr(self, 'recipients', self.get_recipients(contact_object)))
        template_name = kwargs.get('template_name', getattr(self, 'template_name', self.get_template_name()))
        
        context = RequestContext(request, {})
        context.update({
            'object': contact_object,
            'form': self.init_form(request, form_class, recipients),
        })
        return render_to_response(template_name, context)

generic_contact_page = GenericContactPage()
