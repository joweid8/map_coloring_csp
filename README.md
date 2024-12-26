# MapColoringCSP

A simple Python implementation of the **AC-3 algorithm** for map coloring. This class provides an interface for defining variables (e.g., regions on a map), their domains (possible colors), and constraints (edges between variables). It then checks for arc consistency to prune the domains, ensuring no conflicting color assignments remain.

### Features

- **Add Variables:** Define regions (variables) and their set of possible colors (domains).
- **Add Edges:** Specify adjacency constraints (edges) between regions.
- **AC-3 Algorithm:** Propagate constraints to ensure the assignment of variables remains consistent.
- **Solving:** Solve the map coloring CSP with backtracking

### Getting Started
Clone or download this repository.
Install Python (3.6+ recommended).
No extra dependencies are required beyond the Python standard library.

### Usage

Below is a minimal example demonstrating how to use the MapColoringCSP class:

```python
from map_coloring_csp import MapColoringCSP

# Create the CSP instance
csp = MapColoringCSP()

# Define variables (regions) and their possible domains (colors)
csp.add_var("WA", ["green"])
csp.add_var("NT", ["red", "green", "blue"])
csp.add_var("SA", ["red", "green", "blue"])
csp.add_var("Q",  ["red", "green", "blue"])
csp.add_var("NSW", ["red", "green", "blue"])
csp.add_var("V",  ["red"])
csp.add_var("T",  ["red", "green", "blue"])

# Define adjacency constraints (edges)
csp.add_edge("SA", "WA")
csp.add_edge("SA", "NT")
csp.add_edge("SA", "Q")
csp.add_edge("SA", "NSW")
csp.add_edge("SA", "V")
csp.add_edge("WA", "NT")
csp.add_edge("NT", "Q")
csp.add_edge("Q", "NSW")
csp.add_edge("NSW", "V")

# Run the AC-3 algorithm to check for arc consistency
is_arc_consistent = csp.ac3()

# Solve the CSP and get a valid assignment
assignment = csp.solve()
```