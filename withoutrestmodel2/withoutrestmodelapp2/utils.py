import json
def is_json(request):
    try:
        real_json=json.loads(request)
        valid=True
    except ValueError:
        valid=False
    return valid