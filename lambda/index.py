def lambda_handler(event, context):
    # Obtener datos del evento
    user_id = event['user_id']
    accepted = event['accepted']

    # Registrar la aceptación del usuario en DynamoDB
    table.put_item(
        Item={
            'user_id': user_id,
            'accepted': accepted,
            'timestamp': datetime.datetime.utcnow().isoformat()
        }
    )

    # Enviar respuesta
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Aceptación de datos registrada correctamente.'
        })
    }
