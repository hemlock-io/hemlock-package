import requests
import codecs
import pickle

def push_model(model_object, model_name, model_description, variables, auth_token, version):
    pickled = codecs.encode(pickle.dumps(model_object), "base64").decode()
    
    var_list = []
    for variable in variables:
        var_list.append(variable)
    var_list = str(var_list)
    
    r = requests.post('http://159.203.178.163/api/models/'
                        ,headers={'Authorization': 'Token ' + str(auth_token)}
                        ,data={
                                'description': model_description
                               ,'version': 1
                               ,'user': 'default'
                               ,'name': model_name
                               ,'model': pickled
                               ,'variables': var_list
                               ,'hits': 0
                               }
                        )
    return r
