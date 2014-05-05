from numpy import zeros, linalg, vstack, reshape, matrix, array






unit = [(0,0),(1,0),(0,1),(1,1)]

camera = [(0,0),(1,0),(0,1),(1,1)]

A = Homography(camera, unit)
print A*matrix([0,0,1]).T