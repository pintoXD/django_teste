from django import forms
from .choices import *


class ShuffleForm(forms.Form):
    max_speed = forms.IntegerField(label="Velocidade máxima (Km/h)", initial=80)
    min_speed = forms.IntegerField(label="Velocidade mínima (Km/h)", initial=30)
     
    capture_distance = forms.IntegerField(label="Distância de captura (m)", initial=40)

    approximation = forms.BooleanField(label="Aproximação", required=False)
    serial_port = forms.CharField(label="Porta Serial", initial = '/dev/ttyUSB0')

    gap = forms.IntegerField(label="Intervalo entre passagens (s)", initial=15 )
    gap_mode = forms.ChoiceField(choices= GAP_CHOICES, label="Modo do intervalo de envio", initial="1")

    repeat = forms.IntegerField(label="Número de repetições de envio", initial=999)
    #  = forms.CharField(label='Enter your name', max_length=100)
    # email = forms.EmailField(label='Enter your email', max_length=100)
    # feedback = forms.CharField(widget=forms.Textarea(
    #     attrs={'width': "100%", 'cols': "80", 'rows': "20", }))


class ManualForm(forms.Form):

    max_speed = forms.IntegerField(label="Velocidade desejada", initial=50)
    
    capture_distance = forms.IntegerField(label="Distância de captura", initial=40)

    approximation = forms.BooleanField(label="Aproximação", required=False)
    serial_port = forms.CharField(label="Porta Serial", initial = '/dev/ttyUSB0')

    gap = forms.IntegerField(label="Tempo em segundos entre envio de passagens", initial=15 )
    gap_mode = forms.ChoiceField(choices= GAP_CHOICES, label="Modo do intervalo de envio", initial="shuffle")
    
    file_input = forms.FileField(label="Arquivo de velocidades",
                                 required=False, max_length=500)
    repeat = forms.IntegerField(
        label="Número de repetições de envio", initial=999)


# class SerialForm(forms.Form):
#     serial_port = forms.CharField(label="Porta Serial")
#     baudrate = forms.IntegerField(label="Baudrate")



