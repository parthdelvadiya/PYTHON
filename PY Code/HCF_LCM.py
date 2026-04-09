def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = 12
b = 18

hcf = find_hcf(a, b)
lcm = (a * b) // hcf

print("HCF:", hcf)
print("LCM:", lcm)


#######################
import math

a = 12
b = 18

hcf = math.gcd(a, b)
lcm = (a * b) // hcf

print("HCF:", hcf)
print("LCM:", lcm)