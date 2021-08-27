#Specific heat capacity
c_water = 4.187
c_ice = 2.220
c_list = [c_water, c_ice]
#Specific latent heats
water_vaporization_SLH = 2264.705
water_fusion_SLH = 334


first_material_code = input("what is your first material?\n1.water\n2.ice\n")
first_material_temperature = input("\nwhat is the temperature(kelvin)?\n")
first_material_mass = input("\nwhat is the mass(kilogramm)?\n")

second_material_code = input("\nwhat is your second material?\n1.water\n2.ice\n")
second_material_temperature = input("\nwhat is the temperature(kelvin)?\n")
second_material_mass = input("\nwhat is the mass(kilogramm)?\n")

if first_material_code == 1 :
    q_water = first_material_mass * c_list[first_material_code - 1] * (first_material_temperature - 273.15)
elif first_material_code == 2 :
    q_ice = first_material_mass * c_list[first_material_code - 1] * (273.15 - first_material_temperature)
    q_convert = first_material_mass * water_fusion_SLH