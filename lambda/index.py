import json

def lambda_handler(event, context):
    # Obtener datos del evento
    data = json.loads('event')
    user_id = data['user_id']
    accepted = data['accepted']


    # Enviar respuesta
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Aceptación de datos registrada correctamente.'
        })
    }
