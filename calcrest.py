#!/usr/bin/python
import webapp
import socket
import random

def analize(ops):
    try:   
        if len(ops.split("+")) == 2:
            return (int(ops.split("+")[0]) + int(ops.split("+")[1]))
        elif len(ops.split("-")) == 2:
            return (int(ops.split("-")[0]) - int(ops.split("-")[1]))
        elif len(ops.split("*")) == 2:
            return (int(ops.split("*")[0]) * int(ops.split("*")[1]))
        elif len(ops.split("/")) == 2:
            return (int(ops.split("/")[0]) / int(ops.split("/")[1]))
        else:
            return "OpErr"
    except ValueError:
        return "ValueError"




class calcrest(webapp.webApp):  
    def parse(self,peticion):
        print peticion
        orden  = peticion.split()[0] 
        ops = peticion.split()[-1]
        return (orden,ops)

    def process(self,parsedRequest):
        (orden,ops) = parsedRequest
       
        if orden == "PUT":
            self.operacion = ops;
            return ("200 OK","<html><body><h1>" + "La operacion guardada es:" + 
                    str(ops) + "</body></html>")
        elif orden == "GET":
            
            try:
                resultado = analize(self.operacion)
            except AttributeError:
                return("400 Not Found", "<html>""<body><body><h1>ATRIBUTE ERROR</h1></body></html>")

            if resultado == "ValueError":
                return("400 Not Found", "<html>""<body><body><h1>Operando erroneo</h1></body></html>")
            elif resultado == "OpErr":
                return("400 Not Found", "<html>""<body><body><h1>Operacion incorrecta</h1></body></html>")
            else:
                return ("200 OK","<html><body><h1>" + "El resultado a la operacion " + str(self.operacion) +
                        " es:" + str(resultado) + "</body></html>")
        else:
            return("400 Not Found", "<html>""<body><body><h1>Orden incorrecta</h1></body></html>")


if __name__ == '__main__':
    serv = calcrest(socket.gethostname(), 1234) 