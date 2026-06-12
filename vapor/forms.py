from django import forms

BANNED_WORDS=[
    'spam','advertisement','offensive',
    'free money','click here',
]

class ConfessionForm(forms.Form):
    text=forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder':"Pitch your problem and let the strangers help you ...",
            'rows':4,
        }),
        max_length=1000,
        min_length=2,
    )

    def clean_text(self):
        text=self.cleaned_data['text']
        lower_text=text.lower()
        for word in BANNED_WORDS:
            if word in lower_text:
                raise forms.ValidationError(f"Your confession contains a banned word: {word}")
        return text