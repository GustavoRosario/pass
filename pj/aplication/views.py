from django.shortcuts import render
from django.http import HttpResponse
from aplication.controles import turn, record
from aplication.dto.dto_record import dto_record
from aplication.dto.dto_generated_turn import dto_generated_turn

def next(request):
    
    _record = dto_record() #Objeto Historial
    _generated_turnn = dto_generated_turn()
    _turn = turn.generate(2)
    _record.turn = _turn
    _generated_turnn.turn = _turn
    turn.register(_generated_turnn)
    record.register(_record)
    html:str = '<html><body> <p><h1> <center><br>' + _turn +'</br></center><h1></p> </body></html>'
    return HttpResponse(html)
    #return render(request,"Resultado:" + '', {})
