weight = input('Weight in kg or lbs: ')
weight_in_lbs = int(weight) * 2.20462
weight_in_kg = int(weight) * 0.453592
unit_pref = input('Which do you want to convet to?: (L)bs or (K)g? ')
if unit_pref in ['L', 'l']:
    print(f'You are {round(weight_in_lbs)} pounds')
elif unit_pref in ['K', 'k']:
    print(f'You are {round(weight_in_kg)} kilograms')
input()


