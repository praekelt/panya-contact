from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(
        max_length=100,
        label='Name:',
        help_text="First Name and Last.",
        widget=forms.TextInput(attrs={'class':'required'}),
        error_messages={'required': 'Please enter your name.'}
    )
    lastname = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'class':'required'}),
        error_messages={'required': 'Please enter your surname.'}
    )
    email_address = forms.EmailField(
        max_length=100,
        label='Email:',
        help_text='We will send you account notices here - so make sure its good.',
        widget=forms.TextInput(attrs={'class':'required email'}),
        error_messages={'required': 'Please enter your email address.'}
    )
    '''
    recaptcha_response_field = forms.CharField(
        max_length=100,
        label='Human?',
        help_text='Spam prevention code. Enter the words above.',
        widget=forms.TextInput(attrs={'class':'required', 'id': 'recaptcha_response_field', 'autocomplete': 'off'}),
        error_messages={'required': 'Please enter the words above.'}
    )
    '''
    message = forms.CharField(
        max_length=10000,
        label='Message:',
        widget=forms.Textarea(),
        error_messages={'required':'Please enter a message.'}
    )
        
    def is_valid(self, request):
        valid = super(ContactForm, self).is_valid()

        # Validate Captcha
        if not self._errors.has_key('recaptcha_response_field'):
            if not ReCaptcha().verify(request):
                self._errors['recaptcha_response_field'] = ['Incorrect, please try again.',]
                valid = False
        return valid
    
    def get_recipients(self):
        recipients = []
        
        settings = Settings.objects.all()
        if settings:
            contact_email_recipients = settings[0].contact_email_recipients
            if contact_email_recipients:
                split_recipients = [recipient.replace('\r', '') for recipient in contact_email_recipients.split('\n')]
                for recipient in split_recipients:
                    if recipient:
                        recipients.append(recipient)

        if not recipients:
            mail_managers('Error: No email address specified', 'Users are trying to contact style Intern for which no contact email recipients are specified.', fail_silently=False)
        return recipients
    
    def send_message(self, recipients):
        
        name = "%s %s" % (self.cleaned_data['firstname'], self.cleaned_data['lastname'])
        email = self.cleaned_data['email_address']
        subject = "Contact Message from Style Intern"
        message = self.cleaned_data['message']
        recipients = recipients
        from_address = "%s <%s>" % (name, email)
        
        mail = EmailMessage(subject, message, from_address, recipients, headers={'From': from_address, 'Reply-To': from_address})
        mail.send(fail_silently=False)