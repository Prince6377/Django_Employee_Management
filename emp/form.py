from django import forms

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Your Email",max_length=200)
    name=forms.CharField(label="Your Name ",max_length=100)
    feedback=forms.CharField(label="your Feedback",widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'