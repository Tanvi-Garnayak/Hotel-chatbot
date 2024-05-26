import json


def validate(slots):

    
    
    if not slots['Location']:
        print("Inside Empty Location")
        return {
        'isValid': False,
        'violatedSlot': 'Location'
        }        
        
    
        
    if not slots['CheckInDate']:
        
        return {
        'isValid': False,
        'violatedSlot': 'CheckInDate',
    }
        
    if not slots['Nights']:
        return {
        'isValid': False,
        'violatedSlot': 'Nights'
    }
        
    if not slots['RoomType']:
        return {
        'isValid': False,
        'violatedSlot': 'RoomType'
    }

    return {'isValid': True}
    
def lambda_handler(event, context):