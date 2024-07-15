def add(a, b):
    return(a + b)

def sub(a, b):
    return(a - b)

def times(a, b):
    return(a * b)

def div(a, b):
    return(a / b)

def allInOne(x, y):
  return("add"+":"+ str(add(x, y))+" ,"+"sub"+":"+ str(sub(x, y))+" ,"+"mult"+":"+ str(times(x, y))+" ,"+"div"+":"+ str(div(x, y)))

print(allInOne(1, 6))