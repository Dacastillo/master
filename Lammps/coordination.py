from ovito.io import *
from ovito.data import *
from ovito.modifiers import *
import numpy as np

node = import_file("coordination.dump", multiple_frames = True)

# Calculate coordination numbers:
modifier = CoordinationNumberModifier(cutoff=2.0)
node.modifiers.append(modifier)

# Add a user-defined modifier that counts the number of particles of type 4
# and which have a coordination equal to 1.
def count_coordinated_particles(frame, input, output):
	selection1 = (input.particle_properties['Particle Type'].array == 4) & (input.particle_properties['Coordination'].array == 4)
	output.attributes['O4'] = np.count_nonzero(selection1)

# Insert Python modifier into the data pipeline.
node.modifiers.append(PythonScriptModifier(function = count_coordinated_particles))

# Let OVITO do the computation and export the calculated numbers as a function
# of simulation time to a text file:
export_file(node, "coordination.txt", "txt",
    columns = ['Timestep', 'O4'],
    multiple_frames = True)
