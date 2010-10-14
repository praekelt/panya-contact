from panya.generic.views import GenericForm
from contact.forms import SiteContactForm

class SiteContact(GenericForm):
    def get_form_class(self, *args, **kwargs):
        return SiteContactForm
    
    def get_template_name(self, *args, **kwargs):
        return 'contact/site_contact.html'
    
    def get_success_message(self, *args, **kwargs):
        """
        Returns user message to display after successful submition.
        """
        return "Thanks for getting in touch. We'll get back to you as soon as possible."
    
site_contact = SiteContact()
