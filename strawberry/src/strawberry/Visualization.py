
from strawberry import Rules_production
from openalea.mtg import *
from turtle import *
from openalea.core import *
from openalea.plantgl import all as pgl


#Visualization  by plante
# Je souhaiterai l'avoir une entre plutot de type Visualise_plant( Genotype_name, Date, plant number)

#g.properties()['order'] = orders(g)
#color_code(g)

#count = 0
def strawberry_visitor(g, v, turtle, time=0):
    """ Function that draw geometry for a given vertex. """
    #global count
    #count+=1
    geoms = Rules_production.get_symbols()
    turtle.setWidth(0.01)
    nid = g.node(v)
    label = g.label(v)

    if label in ('F', 'f'):
        turtle.rollL(Rules_production.roll_angle)
    if g.edge_type(v) == '+':
        turtle.down(30)

    turtle.setId(v)
    geoms.get(label)(g, v, turtle)

#scene = turtle.traverse_with_turtle(g, vid, visitor=strawberry_visitor)
#spgl.Viewer.display(scene)
#print count # a quoi sert le conmpteur?

#Vizalisation by genotype et par de la date
#fonction visualisation(Genotype, nb_date, nb_plante) 

def visualise_plants(g):
    t = pgl.PglTurtle()
    vids = g.component_roots_at_scale(g.root, g.max_scale())
    n= len(vids)
    x=-9
    y = -12
    dx = 2.
    dy = 4.
    scenes = pgl.Scene()
    count = 0
    for vid in vids:
        position = (x+(count%9)*dx,y+(count/9)*dy,0)
        t = pgl.PglTurtle()
        #t.move(position)
        scene = turtle.traverse_with_turtle(g, vid, visitor=strawberry_visitor, turtle=t)
        
        ds = scene.todict()
        
        for shid in ds:
            for sh in ds[shid]:
                sh.geometry = pgl.Translated(position, sh.geometry)
                scenes.add(sh)
        count += 1
    return scenes

#Vizualisation d'une plante selectionnee par genotype et par date
#fonction (Genotype~Plante selectionnee)
#fonction (All Genotype ~ Plante selectionnee)
#Comparer les Genotypes 2 a 2
