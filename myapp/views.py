from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .forms import MyForm, SerialForm
# from .teste_1 import print_data
import requests
import multiprocessing
import sys
sys.path.append("/home/pinto/Documentos/repos/LTIs200simulator/")
import runSensor

# from subprocess import run, PIPE


id_queue = multiprocessing.Queue(1)
content_queue = multiprocessing.Queue(1)





def home(request):
    return render(request, 'home.html')

def callSensor(input_data):

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

        proc = multiprocessing.Process(target=runSensor.VirtualSensor, args=(id_queue,content_queue,), daemon=True)
        proc.start()

    else:

        content_queue.put(input_data)



    

def responseform(request):
     #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            
            
            
            
            max_speed = myForm.cleaned_data['max_speed']
            min_speed = myForm.cleaned_data['min_speed']
            max_capture_distance = myForm.cleaned_data['max_capture_distance']
            min_capture_distance = myForm.cleaned_data['min_capture_distance']
            approximation = myForm.cleaned_data['approximation']
        
            input_data = [max_speed,min_speed,max_capture_distance,min_capture_distance,approximation]

            callSensor(input_data)           

            # name = myForm.cleaned_data['name']
            # email = myForm.cleaned_data['email']
            # feedback = myForm.cleaned_data['feedback']

            context = {

                'max_speed': max_speed,
                'min_speed': min_speed,
                'max_capture_distance': max_capture_distance,
                'min_capture_distance': min_capture_distance,
                'approximation': approximation


            }

            template = loader.get_template('thankyou.html')

            # proc.join()

            return HttpResponse(template.render(context, request))

            # return render(request, 'home.html' , context)



     else:
         form = MyForm()

     return render(request, 'param.html', {'form':form});


def serialform(request):
    #if form is submitted
    if request.method == 'POST':
        myForm = SerialForm(request.POST)

        if myForm.is_valid():

            serial_port = myForm.cleaned_data['serial_port']
            baudrate = myForm.cleaned_data['baudrate']

            serial_config = [serial_port, baudrate]
            f = open("serial.cfg","w+")

            f.write(serial_config)

            f.close()

            
            context = {

                'serial_port': serial_port,
                'baudrate': baudrate
            }

            template = loader.get_template('serialstatus.html')

            # proc.join()

            return HttpResponse(template.render(context, request))

            # return render(request, 'home.html' , context)


    else:
         form2 = SerialForm()

    return render(request, 'ser.html', {'serial': form2});


# from django.http import HttpResponse
# from .forms import ContactForm

# # Create your views here.


# def contact(request):

#     # return HttpResponse('contact view')

#     if request.method == 'POST':
#         form  = ContactForm(request.POST)
#         if form.is_valid():

#             print("Teste")
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             print(name, email)
           


#     form = ContactForm()
#     return render(request, 'form.html', {'form':form})


    
