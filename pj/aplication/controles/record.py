from aplication.models import historical_record
from aplication.dto.dto_record import dto_record 
import datetime as dt

def register(_record:dto_record):
    historical = historical_record()
    historical.registration_date = dt.date.today()
    historical.registration_time = dt.datetime.now().strftime('%H:%M:%S')
    historical.turn = _record.turn
    historical.active = True
    historical.save()
