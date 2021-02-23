## While Loops

Repeat a set of statements as long as a condition is True

### DRY: Don't Repeats Yourself

### Formula
```python
while (Condition):
  # Body

else: # Optional
  # Body
```

*Ex.*
```python
while(True):
  print ("This statements prints forever")
```

### Rule

A loop becomes an infinite loop if a condition never becomes __FALSE__

To avoid an infinite loop, make sure to use a variable and keep tracks of its value.

*Ex.*

```python
counter = 0

while (counter < 3):
  print("Inside loop")
  counter += 1 # counter = counter + 1

print("Outside loop")
```

> Inside loop
> Inside loop
> Inside loop
> Outside loop