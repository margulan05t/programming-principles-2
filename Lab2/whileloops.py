i = 2
while i < 6:
  print(i)
  i += 1

#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
