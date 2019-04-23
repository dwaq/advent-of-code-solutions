# -*- coding: utf-8 -*-
from anytree import AnyNode


class DictImporter(object):

    def __init__(self, nodecls=AnyNode):
        u"""
        Import Tree from dictionary.

        Every dictionary is converted to an instance of `nodecls`.
        The dictionaries listed in the children attribute are converted
        likewise and added as children.

        Keyword Args:
            nodecls: class used for nodes.

        >>> from anytree.importer import DictImporter
        >>> from anytree import RenderTree
        >>> importer = DictImporter()
        >>> data = {
        ...     'a': 'root',
        ...     'children': [{'a': 'sub0',
        ...                   'children': [{'a': 'sub0A', 'b': 'foo'}, {'a': 'sub0B'}]},
        ...                  {'a': 'sub1'}]}
        >>> root = importer.import_(data)
        >>> print(RenderTree(root))
        AnyNode(a='root')
        ├── AnyNode(a='sub0')
        │   ├── AnyNode(a='sub0A', b='foo')
        │   └── AnyNode(a='sub0B')
        └── AnyNode(a='sub1')
        """
        self.nodecls = nodecls

    def import_(self, data):
        """Import tree from `data`."""
        return DictImporter.__import(data)

    @staticmethod
    def __import(data, parent=None):
        assert isinstance(data, dict)
        assert "parent" not in data
        attrs = dict(data)
        children = attrs.pop("children", [])
        node = AnyNode(parent=parent, **attrs)
        for child in children:
            DictImporter.__import(child, parent=node)
        return node
