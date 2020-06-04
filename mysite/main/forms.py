

class ProfileUpdateForm1(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['img1']

class ProfileUpdateForm2(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['img2']
