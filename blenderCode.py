import bpy
from random import randint
bpy.ops.mesh.primitive_cube_add()

def reset_blend():

    for scene in bpy.data.scenes:
        for obj in scene.objects:
            scene.objects.unlink(obj)

    # only worry about data in the startup scene
    for bpy_data_iter in (
            bpy.data.objects,
            bpy.data.meshes,
            bpy.data.lamps,
            bpy.data.cameras,
            ):
        for id_data in bpy_data_iter:
            bpy_data_iter.remove(id_data)


def add_cubes( count):

    for c in range(0,count):
        x = randint(-8,8)
        y = randint(-8,8)
        z = randint(1,3)
        bpy.ops.mesh.primitive_cube_add(location=(x,y,z))

def add_base():
    bpy.ops.mesh.primitive_plane_add(location=(0,0,-0.01), radius = 9)


def mesher():
    import bpy
    import math
     
    # mesh arrays
    verts = []
    faces = []
     
    # mesh variables
    numX = 10
    numY = 10
     
    # wave variables
    freq = 1
    amp = 1
    scale = 1
     
    #fill verts array
    for i in range (0, numX):
        for j in range(0,numY):
     
            x = scale * i
            y = scale * j
            z = scale*((amp*math.cos(i*freq))+(amp*math.sin(j*freq)))
     
            vert = (x,y,z) 
            verts.append(vert)
     
    #fill faces array
    count = 0
    for i in range (0, numY *(numX-1)):
        if count < numY-1:
            A = i
            B = i+1
            C = (i+numY)+1
            D = (i+numY)
     
            face = (A,B,C,D)
            faces.append(face)
            count = count + 1
        else:
            count = 0
     
    #create mesh and object
    mesh = bpy.data.meshes.new("wave")
    object = bpy.data.objects.new("wave",mesh)
     
    #set mesh location
    object.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(object)
     
    #create mesh from python data
    mesh.from_pydata(verts,[],faces)
    mesh.update(calc_edges=True)

reset_blend()
add_base()
add_cubes( 100)
