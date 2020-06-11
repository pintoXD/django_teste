from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .forms import MyForm, ManualForm
# from .teste_1 import print_data
import requests
import multiprocessing
import sys
sys.path.append("../laser_simulator/")
import runSensor
import configparser
import os

# from subprocess import run, PIPE


id_queue = multiprocessing.Queue(1)
config_queue = multiprocessing.Queue(1)
content_queue = multiprocessing.Queue(1)





def home(request):
    return render(request, 'home.html')


def callSensor(input_data, config_data):

    global id_queue
    global content_queue

    #Faz isso pra não limpar a queue. Que se limpar, perde
    # todos os dados de fila
    #
    

    aux_queue = id_queue
    #id_queue recebe como elemento uma lista contendo dois parametros
    #O primeiro é o id do processo pai
    #O segundo é o id do processo filho
    #
    #Se o segundo parametro num tiver nada, processo não tem filh, mas o processo
    #de chamada do sensor virtual já foi feito alguma vez

    #Se id_queue num tiver nada, quer dizer que nunca se foi
    # chamado o sensor virtual.
    # 
    # sdfasdf
    #  

    if(id_queue.empty()):

        id_queue.put([multiprocessing.current_process().pid, 
                      None])
        
        content_queue.put(input_data)
        config_queue.put(config_data)

        proc = multiprocessing.Process(target=runSensor.VirtualSensor, 
                        args=(id_queue,content_queue, config_queue,), daemon=True)
       
        proc.start()

    else:

        content_queue.put(input_data)
        config_queue.put(config_data)


    

def responseform(request):
     #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            
            
            
            mode = 'shuffle'

            max_speed = myForm.cleaned_data['max_speed']
            min_speed = myForm.cleaned_data['min_speed']

            capture_distance = myForm.cleaned_data['capture_distance']
            
            approximation = myForm.cleaned_data['approximation']
            serial_port = myForm.cleaned_data['serial_port']

            gap = myForm.cleaned_data['gap']
            gap_mode = myForm.cleaned_data['gap_mode'] 
            repeat = myForm.cleaned_data['repeat']

            input_data = [max_speed,min_speed,
            capture_distance,approximation,serial_port]



            config_data = [mode, gap, gap_mode, repeat]

            callSensor(input_data, config_data)

            # callSensor(input_data)           

            # name = myForm.cleaned_data['name']
            # email = myForm.cleaned_data['email']
            # feedback = myForm.cleaned_data['feedback']

            context = {

                'max_speed': max_speed,
                'min_speed': min_speed,
                'capture_distance': capture_distance,
                'approximation': approximation,
                'serial_port': serial_port,
                'gap': gap,
                'gap_mode': gap_mode,
                'repeat': repeat



            }

            template = loader.get_template('thankyou.html')

            # proc.join()

            return HttpResponse(template.render(context, request))

            # return render(request, 'home.html' , context)



     else:
         form = MyForm()

     return render(request, 'param.html', {'form':form});


def manualForm(request):
    #Form pra lidar com a entrada manual de dados de velocidade
    #if form is submitted
    if request.method == 'POST':
        myForm = ManualForm(request.POST, request.FILES)

        if myForm.is_valid():

            mode = 'manual'

            print("Form is valid")

            max_speed = myForm.cleaned_data['max_speed']

            #Este valor não será usado, mas é necessário para
            #o funcionamento do código
            min_speed = 45

            capture_distance = myForm.cleaned_data['capture_distance']

            approximation = myForm.cleaned_data['approximation']
            serial_port = myForm.cleaned_data['serial_port']

            gap = myForm.cleaned_data['gap']
            gap_mode = myForm.cleaned_data['gap_mode']
            gap_mode = dict(myForm.fields['gap_mode'].choices)[gap_mode]
            repeat = myForm.cleaned_data['repeat']

            if('file_input' in request.FILES):
                file_input = request.FILES['file_input']
                max_speed = handle_uploaded_file(file_input)
                speeds = "Coleção de velocidades"
                print("Tem arquivo")
                # print(teste)
            else:
                print("Não foi enviado arquivo algum")
                speeds = max_speed
                


            



            input_data = [max_speed, min_speed,
                          capture_distance, approximation, serial_port]
            # callSensor(input_data)

            config_data = [mode, gap, gap_mode, repeat]


            callSensor(input_data, config_data)

            print("Input:", input_data)
            print("Condig:", config_data)
            # name = myForm.cleaned_data['name']
            # email = myForm.cleaned_data['email']
            # feedback = myForm.cleaned_data['feedback']

            context = {

                'max_speed': speeds,
                'capture_distance': capture_distance,
                'approximation': approximation,
                'serial_port': serial_port,
                'gap': gap,
                'gap_mode': gap_mode,
                'repeat': repeat


            }


            template = loader.get_template('manualok.html')

            # proc.join()

            return HttpResponse(template.render(context, request))

            # return render(request, 'home.html' , context)


    else:
         form = ManualForm()

    return render(request, 'manual.html', {'manual': form});


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    if(os.path.exists(f.name)):
        input_file = configparser.ConfigParser()

        input_file.read(f.name)

        speed_data = input_file['data']['speed']

        speed_data = speed_data.strip('[]').split(',')

        for i in range(len(speed_data)):

            speed_data[i] = int(speed_data[i])

        
        return speed_data

    else:
        print("Arquivo não encontrado")
        raise FileNotFoundError



# def serialform(request):
#     #if form is submitted
#     if request.method == 'POST':
#         myForm = SerialForm(request.POST)

#         if myForm.is_valid():

#             serial_port = myForm.cleaned_data['serial_port']
#             baudrate = myForm.cleaned_data['baudrate']

#             serial_config = [serial_port, baudrate]
#             f = open("serial.cfg","w+")

#             f.write(serial_config)

#             f.close()

            
#             context = {

#                 'serial_port': serial_port,
#                 'baudrate': baudrate
#             }

#             template = loader.get_template('serialstatus.html')

#             # proc.join()

#             return HttpResponse(template.render(context, request))

#             # return render(request, 'home.html' , context)


#     else:
#          form2 = SerialForm()

#     return render(request, 'ser.html', {'serial': form2});


# # from django.http import HttpResponse
# # from .forms import ContactForm

# # # Create your views here.


# # def contact(request):

# #     # return HttpResponse('contact view')

# #     if request.method == 'POST':
# #         form  = ContactForm(request.POST)
# #         if form.is_valid():

# #             print("Teste")
# #             name = form.cleaned_data['name']
# #             email = form.cleaned_data['email']
# #             print(name, email)
           


# #     form = ContactForm()
# #     return render(request, 'form.html', {'form':form})


    
