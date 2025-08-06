# generate_graphviz_flowchart.py

"""
Generates a vertical Graphviz PNG diagram of the LangGraph orchestration flow
and saves it to the docs/ directory.
"""

import os
from graphviz import Digraph
from IPython.display import Image, display

# Define output path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)
#from paths import DOCS_DIR
from paths import SRC_DIR

OUTPUT_PATH = os.path.join(DOCS_DIR, "publication_flowchart")

#Applied this snippet code, replacing with the correct path to the docs outside the src
#OUTPUT_DIR = Path("outputs")
#OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# Create the flowchart
dot = Digraph(comment="LangGraph Flowchart", format='png')
dot.attr(rankdir='TB', fontsize='12')

# Nodes
dot.node('Z', 'Ready Tensor dataset', shape='folder', style='filled', fillcolor='lightgray')
dot.node('A', 'select_pub1')
dot.node('C', 'select_pub2')
dot.node('B', 'analyze_pub1')
dot.node('D', 'analyze_pub2')
dot.node('E', 'compare')
dot.node('F', 'aggregate_trends')
dot.node('G', 'summarize')
dot.node('H', 'fact_check_node')
dot.node('I', 'END', shape='doublecircle')

# Edges
dot.edge('Z', 'A')
dot.edge('Z', 'C')
dot.edge('A', 'B')
dot.edge('C', 'D')
dot.edge('B', 'E')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H')
dot.edge('H', 'I')

# Generate PNG only (no .md, no .gv)
output_png_path = dot.render(filename=OUTPUT_PATH, view=False)
print(f"✅ PNG flowchart saved to: {output_png_path}")

# Display for notebooks or interactive shell
if __name__ == "__main__":
    display(Image(filename=output_png_path))
