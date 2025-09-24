with open('for.py', 'w') as f:
    for _ in range(1000000):
        f.write('for i in range(1):\n    pass\n')
    f.write('print("Done!")\n')


