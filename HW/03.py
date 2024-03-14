import random  
def maximize():
    x = 0
    y = 0
    z = 0
    for i in range(10000):
        
        x2 = random.uniform(0,10)  
        y2 = random.uniform(0,10)  
        z2 = random.uniform(0,5.5)  
        if(x2+y2<=10 and 2*x2+z2<=9 and y2+2*z2<=11):
            if 3*x2+2*y2+5*z2>=3*x+2*y+5*z:
                x=x2
                y=y2
                z=z2
                print(x,y,z)
    ans=3*x+2*y+5*z
    return {"x": x, "y": y, "z": z}, ans


solution, ans = maximize()
print(solution,ans)
'''
{'x': 3.286626017620705, 'y': 6.559300871497943, 'z': 2.216186551178141} 34.05941255174871
'''
