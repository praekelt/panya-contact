from django import forms
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage, mail_managers        

from captcha.fields import ReCaptchaField
from preferences import preferences

class SiteContactForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class':'required shift'}),
        error_messages={'required': 'Please enter your name.'}
    )
    email_address = forms.EmailField(
        max_length=150,
        widget=forms.TextInput(attrs={'class':'required email shift'}),
        error_messages={'required': 'Please enter your email address.'}
    )
    captcha = ReCaptchaField(
        error_messages={'required': 'Please enter the text.'}
    ) 
    message = forms.CharField(
        max_length=10000,
        widget=forms.Textarea(attrs={'class':'required shift'}),
        error_messages={'required':'Please enter a message.'}
    )
        
    def handle_valid(self, *args, **kwargs):
        """
        Send the email.
        """
        recipients = [recipient.email for recipient in preferences.ContactPreferences.email_recipients.all()]
        if not recipients:
            mail_managers('Error: No email address specified', 'Users are trying to contact the site for which no email address could be found.', fail_silently=False)
            return None
        
        else:
            name = self.cleaned_data['name']
            email = self.cleaned_data['email_address']
            current_site = Site.objects.get_current()
            message = self.cleaned_data['message']
            subject = "Contact Message from %s" % current_site.name
            from_address = "%s <%s>" % (name, email) 
            mail = EmailMessage(subject, message, from_address, recipients, headers={'From': from_address, 'Reply-To': from_address})
            mail.send(fail_silently=False)
