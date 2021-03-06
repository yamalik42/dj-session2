from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

# Create your views here.
@csrf_exempt
def file_op(request):
    
    def mod_file(file_name, op):

        with open(f'./app1/{file_name}', op) as f:
            nonlocal content
            if op in ('w', 'a'):
                nonlocal content
                f.write(content)
            elif op == 'r':
                content = f.read()
                return content

    

    if request.method == 'POST': 
        # import pdb;pdb.set_trace()
        body = json.loads(request.body)
        file_name = body['filename']
        print(body['content'])
        content = body['content']
        mod_file(file_name, 'w')
        return HttpResponse('created file')
    elif request.method == 'GET':    
        file_name = request.GET['filename']
        content = mod_file(file_name, 'r')
        return HttpResponse(content)
    elif request.method == 'PUT':
        file_name = request.GET['filename']
        content = request.body.decode('utf-8')
        mod_file(file_name, 'a')
        return HttpResponse('Appended to file')
    elif request.method == 'DELETE':
        file_name = request.GET['filename']
        os.remove(f'./app1/{file_name}')
        return HttpResponse('Deleted file')

        

    