from django import forms

class TextSummaryForm(forms.Form):
    text_input = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Paste your text here...',
            'rows': 10
        }),
        label='Input Text'
    )
    num_sentences = forms.IntegerField(
        initial=3,
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of sentences in summary'
        }),
        label='Summary Length'
    )
