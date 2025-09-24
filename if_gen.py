with open('if.py', 'w') as f:
    for _ in range(1000000):
        f.write('if True:\n    pass\n')
    f.write('print("Hello World")\n')


    