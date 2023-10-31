from aplication.models import ma_category as cat,sequence_control as cso
from aplication.models import generated_turn
from aplication.dto import dto_generated_turn
import datetime as dt

def generate(category_id:int):
    sequence:str
    INITIAL_SEQUENCE:int = 1
    prefix = get_prefix(category_id)
    sec =  get_sequence(category_id)
    system_date = dt.date.today()
    date_update = get_date_update(category_id)
    sequence = prefix + '-' + str(sec)
    
    if(system_date == date_update):
        update_sequence(category_id,sec)
        update_sequence_date(category_id)
    elif(system_date != date_update):
        sequence = prefix + '-' + str(INITIAL_SEQUENCE)
        update_sequence(category_id,INITIAL_SEQUENCE)
        update_sequence_date(category_id)
        
    return sequence

def register(_turn:dto_generated_turn):
    ON_HOLD:int = 1
    STATION_ID:int = 1
    turn = generated_turn()
    turn.registration_date = dt.date.today()
    turn.state_id = ON_HOLD
    turn.station_id = STATION_ID
    turn.registration_date = dt.date.today()
    turn.registration_time = dt.datetime.now().strftime('%H:%M:%S')
    turn.turn = _turn.turn
    turn.active = True
    turn.save()

def get_prefix(_category_id:int):
    query = cat.objects.get(category_id = _category_id)
    result =  query.prefix
    return result
 
def get_sequence(_category_id:int):
        qr = cso.objects.get(category_id = _category_id)
        sequence =  qr.current_sequence
        result = next_turn(sequence)
        return result

def get_date_update(_category_id:int):
        query = cso.objects.get(category_id = _category_id)
        date =  query.date_update
        return date

def update_sequence_date(_category_id:int,):
     query = cso.objects.get(category_id = _category_id)
     query.date_update = dt.datetime.today() 
     query.update_time  = dt.datetime.now().strftime('%H:%M:%S')
     query.save()
    
def update_sequence(_category_id:int,new_sequence:int):
     query = cso.objects.get(category_id = _category_id)
     query.current_sequence = new_sequence
     query.save()

def next_turn(sec:int):
    x:int = 1
    x = x + sec
    return x
