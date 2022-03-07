import math
def part1():
 
  n = 42
  tau = (math.pi) * 2
  tau = round(tau, 4)
  school = "Sault College"
  print(str(n) + ", " + str(tau) + ", " + school)

part1()

def part2():
  college_class = "CSD110"   #class is a keyword in python
  desired_grade = 100        #can't use a dash in a variable name
  two_hot = "hothot"  #cant start a variable with an integer
  pi = 3.14159  #wrong order
  print(college_class + ", " + str(desired_grade) + ", " + two_hot  + ", " + str(pi))

part2()

def part3():
  repeat_hot = "Hot" * 3
  print("Feeling..." + repeat_hot + "!")

part3()
  
def part4():
  base = 3000    # in cm
  height = 1000  # in cm
  volume = 1/3 * pow(base, 2) * height
  print("The volume of a square pyramid with base " + str(base) + "cm and height " + str(height) + "cm is " + str(volume) + "cm^3")

# Ignore this for now; you will learn what this is later

if __name__ == "__main__":
    part4()

