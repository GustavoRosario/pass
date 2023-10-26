from django.shortcuts import render
from django.http import HttpResponse
from aplication.controles import turn, record
from aplication.dto.dto_record import dto_record
from aplication.dto.dto_generated_turn import dto_generated_turn

def turn(request):
    
    _record = dto_record() #Objeto Historial
    _generated_turnn = dto_generated_turn()
    _turno = turn.generate(1)
    _record.turn = _turno
    _generated_turnn.turn = _turno
    turn.register(_generated_turnn)
    record.register(_record)
    html:str = '<html><body> <p><h1> <center><br>' + _turno +'</br></center><h1></p> </body></html>'
    return HttpResponse(html)
    #return render(request,"Resultado:" + '', {})
