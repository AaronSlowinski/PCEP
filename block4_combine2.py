def combine (width, height=2, depth=0, is_3D=False):
    return [is_3D, width, height, depth]

print(combine(1)[2])

#prints to 2