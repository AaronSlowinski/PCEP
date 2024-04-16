def combine (width, height=10, depth=0, is_3D=False):
    return [is_3D, width, height, depth]

print(combine(height=1,width=2)[3])