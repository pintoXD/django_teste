from django import forms


class MyForm(forms.Form):
    max_speed = forms.IntegerField(label="Velocidade máxima")
    min_speed = forms.IntegerField(label="Velocidade mínima")
    
    max_capture_distance = forms.IntegerField(
        label="Máxima distância de captura")
    min_capture_distance = forms.IntegerField(label="Minima distância de captura")

    approximation = forms.BooleanField(label="Aproximação", required=False)

    #  = forms.CharField(label='Enter your name', max_length=100)
    # email = forms.EmailField(label='Enter your email', max_length=100)
    # feedback = forms.CharField(widget=forms.Textarea(
    #     attrs={'width': "100%", 'cols': "80", 'rows': "20", }))


class manualForm(forms.Form):
    max_speed = forms.IntegerField(label="Velocidade máxima")
    min_speed = forms.IntegerField(label="Velocidade mínima")

    max_capture_distance = forms.IntegerField(
        label="Máxima distância de captura")
    min_capture_distance = forms.IntegerField(
        label="Minima distância de captura")

    approximation = forms.BooleanField(label="Aproximação", required=False)


class SerialForm(forms.Form):
    serial_port = forms.CharField(label="Porta Serial")
    baudrate = forms.IntegerField(label="Baudrate")



