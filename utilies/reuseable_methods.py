import random
import json

#medsta method reuseablity

def generate_six_length_random_number():
    random_otp = random.SystemRandom().randint(100000,999999)
    return str(random_otp)

def get_request_obj(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except:
        try:
            data = json.loads(request.body.decode())
        except:
            data = request.POST
    return data