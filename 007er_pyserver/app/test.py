from graphviz import Digraph,render
from plugins.graphviz_parser import Graphiviz_Parser
render('dot', 'svg', "relationships/index", False)
