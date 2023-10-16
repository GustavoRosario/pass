from django.shortcuts import render
from django.http import HttpResponse
from aplication.controles import turno, historico
from aplication.dto.historial import historial 

def turnos(request):
    
    hiobj = historial() #Objeto Historial
    x = turno.generar(7)
    hiobj.turno = x
    historico.registrar(hiobj)

    return HttpResponse(x)
    #return render(request,"Resultado:" + '', {})
