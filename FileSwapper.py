def fileSwapper():

    fileName1 = input(" Enter File First Name ")
    fileName2 = input(" Enter File Second Name ")

    with open(fileName1, 'r') as f:
        text1 = f.read()
    with open(fileName2, 'r') as t:
        text2 = t.read()

    with open (fileName1, 'w') as w:
        w.write(text2)
    with open (fileName2, 'w') as r:
        r.write(text1)

fileSwapper()