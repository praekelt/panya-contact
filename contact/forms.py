from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        label='Name:',
        widget=forms.TextInput(attrs={'class':'required shift'}),
        error_messages={'required': 'Please enter your name.'}
    )
    email_address = forms.EmailField(
        max_length=150,
        label='Email:',
        widget=forms.TextInput(attrs={'class':'required email shift'}),
        error_messages={'required': 'Please enter your email address.'}
    )
    message = forms.CharField(
        max_length=10000,
        label='Message:',
        widget=forms.Textarea(attrs={'class':'required shift'}),
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
    
    def send_message(self, recipients):
        
        name = "%s %s" % (self.cleaned_data['firstname'], self.cleaned_data['lastname'])
        email = self.cleaned_data['email_address']
        subject = "Contact Message from Style Intern"
        message = self.cleaned_data['message']
        recipients = recipients
        from_address = "%s <%s>" % (name, email)
        
        mail = EmailMessage(subject, message, from_address, recipients, headers={'From': from_address, 'Reply-To': from_address})
        mail.send(fail_silently=False)