import boto3
import json
import uuid



dynamo = boto3.client('dynamodb')


TABLE_NAME = 'todolist'



def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps({'error': err}) if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
    }


def lambda_handler(event, context):
    operation = event['httpMethod']

    
    operations = {
        'GET': handle_get_tasks,
        'POST': handle_add_task,
        'DELETE': handle_delete_task
    }

    if operation in operations:
        return operations[operation](event)
    else:
        return respond(f'Unsupported method "{operation}"')



def handle_get_tasks(event):
    try:
        response = dynamo.scan(TableName=TABLE_NAME)
        tasks = response.get('Items', [])
        return respond(None, tasks)
    except Exception as e:
        return respond(str(e))



def handle_add_task(event):
    try:
        body = json.loads(event['body'])
        task_title = body.get('title')

        if not task_title:
            return respond("Missing task title")

       
        task_id = str(uuid.uuid4())

       
        dynamo.put_item(
            TableName=TABLE_NAME,
            Item={
                'task_id': {'S': task_id},
                'title': {'S': task_title}
            }
        )

        return respond(None, {'message': 'Task added successfully', 'task_id': task_id})
    except Exception as e:
        return respond(str(e))



def handle_delete_task(event):
    try:
        body = json.loads(event['body'])
        task_id = body.get('task_id')

        if not task_id:
            return respond("Missing task ID")

        
        dynamo.delete_item(
            TableName=TABLE_NAME,
            Key={
                'task_id': {'S': task_id}
            }
        )

        return respond(None, {'message': 'Task deleted successfully'})
    except Exception as e:
        return respond(str(e))