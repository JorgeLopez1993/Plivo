# -*- coding: utf-8 -*-
from flask import Flask, Response, request, url_for
import plivoxml

#Mensaje de alerta
IVR_MESSAGE='Tiene que atender un evento activo,pulse 5 para aceptar el evento. Pulse 9 para repetir el mensaje'

#Si el llamado pulsa 9
IVR_MESSAGE

#Si no introduce uno de los dos numeros
NO_INPUT_MESSAGE='Vuelva a introducir el digito'

app=Flask(__name__)

@app.route('response/ivr',methods=['GET','POST'])

def ivr():
    response=plivoxml.Response()
    if request.method =='GET':
        getdigits_action = "https://raw.githubusercontent.com/JorgeLopez1993/Plivo/master/IVR.xml"
        getdigits = plivoxml.GetDigits(action=getdigits_action, method='POST', timeout=7, numDigits=1)
        getdigits.addSpeak(IVR_MESSAGE)
        response.add(getdigits)
        response.addSpeak(NO_INPUT_MESSAGE)
        print response.to_xml()
        return Response(str(response),mimetype='text/xml')

    elif request.method == 'POST':
        digit=request.form.get('Digits')
        print digit
        if digit == "5":
            get.digits_url = "https://ugyn9ecx0a.execute-api.eu-west-1.amazonaws.com/prod/plivonumber5"
            getDigits5 = plivoxml.GetDigits(action=get.digits_url, method='POST', numDigits=1)
            
        elif digit == "9" :
            response.addSpeak(IVR_MESSAGE)
        
        else:
            response.addSpeak(NO_INPUT_MESSAGE)

        print response.to_xml()
            return Response(str(response),mimetype='text/xml')

            
