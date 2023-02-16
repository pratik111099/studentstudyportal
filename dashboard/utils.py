# Mass Conversion Method!!!!!!!!!!!!!!!!!!!!!!!!!!
def conversion_g_kg(value):
    return value * 0.001

def conversion_g_lbs(value):
    return value * 0.00220462

def conversion_g_oz(value):
    return value * 0.0352739200000000003

def conversion_kg_g(value):
    return value * 1000

def conversion_kg_lbs(value):
    return value * 2.20462

def conversion_kg_oz(value):
    return value * 35.274

def conversion_lbs_g(value):
    return value * 453.592

def conversion_lbs_kg(value):
    return value * 0.453592

def conversion_lbs_oz(value):
    return value * 16

def conversion_oz_g(value):
    return value * 28.3495

def conversion_oz_kg(value):
    return value * 0.0283495

def conversion_oz_lbs(value):
    return value * 0.0625


# Temperature Conversion Method!!!!!!!!!!!!!!!!!!!!!!!!!!
def conversion_d_f(value):
    return (value * 9/5) + 32

def conversion_d_k(value):
    return value + 273.15

def conversion_f_d(value):
    return (value - 32) * 5/9

def conversion_f_k(value):
    return (value - 32) * 5/9 + 273.15

def conversion_k_d(value):
    return (value - 273.15)

def conversion_k_f(value):
    return (value - 273.15) * 9/5 + 32



def convert(value, from_unit, to_unit):
    func_name = 'conversion'+'_'+from_unit+"_"+to_unit

    try: 
        return globals()[func_name](value)
    
    except:
        return -1

