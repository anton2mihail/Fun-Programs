import math
print("This is a program that uses the cosine law")
print("a is the unknown side length");
print("Don't Enter a...");
b = float(input("Please enter b: "));
c = float(input("Please enter c: "));
theta = float(input("Please enter the angle opposite to side a in degrees : "));
radian = theta*(math.pi/180.000000000000);
angle = math.cos(radian);
result = math.sqrt(math.pow(b, 2)+ math.pow(c, 2)-((2*b*c)*angle));
print ("This is the length of side a: "+str(result));
