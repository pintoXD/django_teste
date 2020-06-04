from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .forms import MyForm
from multiprocessing import Process
from .teste_1 import print_data
import requests
import sys
# from subprocess import run, PIPE





def button(request):
    return render(request, 'home.html')


def output(request):
    
    data = requests.get("https://www.google.com/")
    print(data.text)
    data = data.text
    return render(request, 'home.html', {'data': data})

def external(request):
    inp = request.POST.get('param')

    out = run([sys.executable, 
              '/home/otto/Documentos/Mobit/simulador/djangofiles/ottoenv/test.py', inp], shell=False, stdout=PIPE)

    print(out)

    return render(request, 'home.html', {'data1':out.stdout.decode('UTF-8')})


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

            proc = Process(target=print_data, args=(input_data,))
            proc.start()

            

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

            proc.join()

            return HttpResponse(template.render(context, request))

            # return render(request, 'home.html' , context)



     else:
         form = MyForm()

     return render(request, 'home.html', {'form':form});





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


    
