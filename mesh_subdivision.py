import numpy as np
import matplotlib.pyplot as plt


def subdivide(vertices, faces):
    new_vertices = []
    new_faces = []
    for face in faces:
        v0, v1, v2 = vertices[face[0]], vertices[face[1]], vertices[face[2]]
        e0 = (v0 + v1) / 2
        e1 = (v1 + v2) / 2
        e2 = (v2 + v0) / 2
        new_vertices.append(v0)
        new_vertices.append(e0)
        new_vertices.append(e2)
        new_vertices.append(v1)
        new_vertices.append(e1)
        new_vertices.append(e0)
        new_vertices.append(v2)
        new_vertices.append(e2)
        new_vertices.append(e1)
        new_vertices.append(e0)
        new_vertices.append(e1)
        new_vertices.append(e2)
    for i in range(len(faces)):
        new_faces.append((3*i, 3*i+1, 3*i+2))
        new_faces.append((3*i+1, 3*i+4, 3*i+2))
        new_faces.append((3*i+2, 3*i+4, 3*i+5))
        new_faces.append((3*i+2, 3*i+5, 3*i+3))
    return new_vertices, new_faces
