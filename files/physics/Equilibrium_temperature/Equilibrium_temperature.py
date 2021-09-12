#define elements
#Specific heat capacity
c_water = 4.187
c_ice = 2.220
c_list = [c_water, c_ice]
#Specific latent heats
water_vaporization_SLH = 2264.705
water_fusion_SLH = 334

equ_temp = None
equ_phase = None

def heat (m, c, theta):
    if theta < 273.15:
        return m * c * (273.15 - theta)
    else :
        return m * c * (theta - 273.15)

def converter (q_water, q_ice, q_convert, m_ice, m_water, c_ice, c_water, equ_temp, equ_phase):
    if q_water > q_ice + q_convert :
        re_heat = q_water - (q_ice + q_convert)
        equ_temp = (re_heat/(m_ice * c_water)) + 273.15
        equ_phase = "water"

    elif q_water == q_ice + q_convert :
        equ_temp = 0
        equ_phase = "water"
        return equ_temp, equ_phase

    elif q_ice > q_water + q_convert:
        re_heat = q_ice - (q_water + q_convert)
        equ_temp = 273.15 - (re_heat/(m_water * c_ice))
        equ_phase = "water"

    elif q_ice == q_water + q_convert:
        equ_temp = 0
        equ_phase = "ice"
    
    elif q_water < q_ice + q_convert and q_ice < q_water + q_convert:
        equ_temp = 0
        equ_phase ="mixture ice and water"
    else:
        equ_temp = 0
        equ_phase =0


#get inputs
material001_code = int(input("what is your first material?\n1.water\n2.ice\n"))
material001_temp = float(input("\nwhat is the temperature(kelvin)?\n"))
material001_mass = float(input("\nwhat is the mass(kilogramm)?\n"))

material002_code = int(input("\nwhat is your second material?\n1.water\n2.ice\n"))
material002_temp = float(input("\nwhat is the temperature(kelvin)?\n"))
material002_mass = float(input("\nwhat is the mass(kilogramm)?\n"))

#procedural code
if material001_code == 2 and material002_code == 1 :
    material001_code, material002_code = material002_code, material001_code
    material001_mass, material002_mass = material002_mass, material001_mass
    material001_temp, material002_temp = material002_temp, material001_temp

if material001_code == 1 and material002_code == 2 :
    q_water = heat(material001_mass, c_list[material001_code - 1], material001_temp)
    q_ice = heat(material002_mass, c_list[material002_code - 1], material002_temp)
    q_convert = material002_mass * water_fusion_SLH
    
    converter(q_water, q_ice, q_convert, material002_mass, material001_mass, +\
        c_list[material002_code - 1], c_list[material001_code - 1], equ_temp, equ_phase)
            
elif material001_code == 1 and material002_code == 1 :
    heats = material001_mass * c_list[material001_code - 1] * material001_temp +\
        material002_mass * c_list[material002_code -1] * material002_temp

    equ_temp = heats/(material001_mass*c_list[material001_code - 1] +\
        material002_mass*c_list[material002_code - 1])
    equ_phase = "water"

elif material001_code == 2 and material002_code == 2 :
    heats = material001_mass * c_list[material001_code - 1] * material001_temp +\
        material002_mass * c_list[material002_code -1] * material002_temp

    equ_temp = heats/(material001_mass*c_list[material001_code - 1] +\
        material002_mass*c_list[material002_code - 1])
    equ_phase = "ice"

else:
    print(4)

print("the final phase is \"",equ_phase, "\", and the final temperature is \"", equ_temp,"\"")