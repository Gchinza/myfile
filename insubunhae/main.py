b, c = input().split()
b = int(b)
c = int(c)
if c > 0:
    for i in range (-c, c):
        if i != 0:
            if c % i == 0:
                 if c // i + i == b:
                      if c//i > 0 and i > 0:
                          print("x", "+", f"{int(c/i)}", ",", "x", "+", f"{i}")
                      elif c // i < 0 and i > 0:
                          print("x", f"{int(c / i)}", ",", "x", "+", f"{i}")
                      elif c // i > 0 and i < 0:
                          print("x", "+", f"{int(c / i)}", ",", "x", f"{i}")
                      else:
                          print("x", f"{int(c / i)}", ",", "x", f"{i}")
if c < 0:
    for i in range (c, -c):
        if i != 0:
            if c % i == 0:
                 if c // i + i == b:
                      if c//i > 0 and i > 0:
                          print("x", "+", f"{int(c/i)}", ",", "x", "+", f"{i}")
                      elif c // i < 0 and i > 0:
                          print("x", f"{int(c / i)}", ",", "x", "+", f"{i}")
                      elif c // i > 0 and i < 0:
                          print("x", "+", f"{int(c / i)}", ",", "x", f"{i}")
                      else:
                          print("x", f"{int(c / i)}", ",", "x", f"{i}")
