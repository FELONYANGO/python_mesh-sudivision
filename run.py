import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the mesh data from the OBJ file
vertices = []
faces = []
with open('subdivided_mesh.obj', 'r') as f:
    for line in f:
        if line.startswith('v '):
            vertex = list(map(float, line.strip().split()[1:]))
            vertices.append(vertex)
        elif line.startswith('f '):
            face = list(map(int, line.strip().split()[1:]))
            faces.append(face)

# Plot the mesh in a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for face in faces:
    v0, v1, v2 = vertices[face[0]-1], vertices[face[1]-1], vertices[face[2]-1]
    ax.plot([v0[0], v1[0], v2[0], v0[0]], [v0[1], v1[1], v2[1], v0[1]], [v0[2], v1[2], v2[2], v0[2]], 'k-')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
