from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        html = ""
        for child in self.children:
            html += child.to_html()
        attributes = self.props_to_html()
        return f"<{self.tag}{attributes}>{html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children:{self.children}, {self.props})"
