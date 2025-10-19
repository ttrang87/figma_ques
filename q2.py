Layer System
Implement a class to manage a system of layers, where:

Each layer has an ID (like 1, 2, 3)
Each layer contains properties stored as key-value pairs
Example of a layer: Layer(1, {"color": "green"})
Part 1: Basic Operations
Implement a class with the following operations:

init()
apply(layer)
undo()
Example Flow:
# Operation 1
apply(Layer(1, {"color": "green"}))

# Operation 2
apply(Layer(2, {"shape": "triangle", "color": "blue"}))

# Operation 3
apply(Layer(1, {"color": "pink"}))

# After these operations, system state is:
# Layer 1: {"color": "pink"}
# Layer 2: {"shape": "triangle", "color": "blue"}

# After one undo(), system state becomes:
# Layer 1: {"color": "green"}
# Layer 2: {"shape": "triangle", "color": "blue"}

# After another undo(), system state becomes:
# Layer 1: {"color": "green"}
Part 2: Batch Operations
Add support for batch operations with these additional features:

commit_batch(): Groups preceding operations into a single batch
Undo should work at batch level
Example Flow with Batches:
# Batch 1
apply(Layer(1, {"color": "green"}))
apply(Layer(2, {"shape": "triangle", "color": "blue"}))
apply(Layer(1, {"color": "pink"}))
commit_batch()

# Batch 2
apply(Layer(1, {"color": "blue"}))
apply(Layer(1, {"color": "white"}))
commit_batch()

# Final state after both batches:
# Layer 1: {"color": "white"}
# Layer 2: {"shape": "triangle", "color": "blue"}

# After one undo() (reverting Batch 2):
# Layer 1: {"color": "pink"}
# Layer 2: {"shape": "triangle", "color": "blue"}
Part 3: Redo Functionality
Add redo capability:

New method: redo()
Restores previously undone operations
