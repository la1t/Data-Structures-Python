"""
Кроме прохождения по всему дереву и проставления уровня узлов,
определять уровни нод можно несколькими способами:
- вычислять непосредственно при запросе, поднимаясь до родителя
- выставлять уровень при добавлении в дерево, считая его, как уровень_родителя + 1
"""


def enrich_levels(tree):
    if tree.Root:
        enrich_subtree_levels(tree.Root, 0)


def enrich_subtree_levels(node, current_level):
    node.Level = current_level
    for child in node.Children:
        enrich_subtree_levels(child, current_level + 1)
