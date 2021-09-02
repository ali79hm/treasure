#define elements
#Specific heat capacity
c_water = 4.187
c_ice = 2.220
c_list = [c_water, c_ice]
#Specific latent heats
water_vaporization_SLH = 2264.705
water_fusion_SLH = 334

def heat (m, c, theta):
    if theta < 273.15:
        return m * c * (273.15 - theta)
    else :
        return m * c * (theta - 273.15)

#get inputs
material001_code = input("what is your first material?\n1.water\n2.ice\n")
material001_temp = input("\nwhat is the temperature(kelvin)?\n")
material001_mass = input("\nwhat is the mass(kilogramm)?\n")

material002_code = input("\nwhat is your second material?\n1.water\n2.ice\n")
material002_temp = input("\nwhat is the temperature(kelvin)?\n")
material002_mass = input("\nwhat is the mass(kilogramm)?\n")

#procedural code
if material001_code == 1 and material002_code == 2 :

    q_water = heat(material001_mass, c_list[material001_code - 1], material001_temp)
    q_ice = heat(material002_mass, c_list[material002_code - 1], material002_temp)
    q_convert = material002_mass * water_fusion_SLH

elif material001_code == 2 and material002_code == 1 :

    q_water = heat(material002_mass, c_list[material002_code - 1], material002_temp)
    q_ice = heat(material001_mass, c_list[material001_code - 1], material001_temp)
    q_convert = material001_mass * water_fusion_SLH

elif material001_code == 1 and material002_code == 1 :
    if material001_temp < material002_temp :

        heats = heat(material001_mass, c_list[material001_code - 1], material001_temp) +\
            heat(material002_mass, c_list[material002_code -1], material002_temp)

        equ_temp = heats/(material001_mass*c_list[material001_code - 1] +\
            material002_mass*c_list[material002_code - 1])

elif material001_code == 2 and material002_code == 2 :

