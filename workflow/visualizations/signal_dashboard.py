from workflow.visualizations.signal_dashboard import visualize_signal_density, load_coaching_tree

tree = load_coaching_tree("coaching_tree_matrix.json")
visualize_signal_density(tree)
