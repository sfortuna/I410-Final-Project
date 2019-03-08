import random, string

def gen(length=12, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))
            

#main
gen()            
