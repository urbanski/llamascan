import requests
import json

def get_installed_models(server):
    """returns a list of installed models"""
    url = server + '/api/tags'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def test_generation(server, model):
    """tests generation with a model"""
    url = server + '/api/generate'
    postBody = {
        'model': model,
        'prompt': 'What is water made of?',
        'length': 100
    }
    response = requests.post(url, data=json.dumps(postBody))
    if response.status_code == 200:
        return response.text
    else:
        return None

def main():
    addr = ''
    port = str(11434)
    uri = 'http://' + addr + ':' + port

    models = get_installed_models(uri)
    print("Found %s models" % len(models['models']))
    if len(models) > 0:
        for model in models['models']:
            print(" - ", model['name'])
        
        generation = test_generation(uri, 'smollm2:135m')
        for tok in generation.split('\n'):
            if tok is not None and tok != '':
                tokJson = json.loads(tok)
                if tokJson['done'] is True:
                    break
                #print(tokJson['response'], end='')

if __name__ == '__main__':
    main()

