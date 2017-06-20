# -*- coding:utf-8 -*-

import math
from io import StringIO

""" 红黑树实现 """

BLACK = '◆'
RED = '◇'


class RBTreeNode:
    """ 红黑树节点定义 """

    def __init__(self, key='NIL', color=BLACK):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return '{0}{1}'.format(self.key, self.color)


class RBTree:
    def __init__(self, data):
        self.nodes = len(data)
        self.nil = RBTreeNode()
        self.root = self.nil
        self.tree = []
        if hasattr(data, '__iter__'):
            for key in data:
                self.insert(RBTreeNode(key=key))
        self.create_tree_list(self.nodes)

    def __repr__(self):
        return ''.join(self.graph())

    def create_tree_list(self, length):
        """ 生成树数组 """

        self.tree.append(self.root)
        node = self.root
        i = 1
        for _ in range(length + 1):
            if node not in [' ', self.nil]:
                self.tree.extend([node.left, node.right])
            else:
                self.tree.extend([' ', ' '])
            node = self.tree[i]
            i += 1

    def graph(self, fill=' '):
        """ 红黑树图形化 """

        output = StringIO()
        last_row = -1
        # 计算树的最大宽度
        total_width = 6 << int(math.ceil(math.log(self.nodes, 2)))
        for i, n in enumerate(self.tree):
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2 ** row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        return output.getvalue()

    def maximum(self, node=None):
        """ 返回最大节点 """

        if not node:
            node = self.root
        while node.right != self.nil:
            node = node.right
        return node

    def minimum(self, node=None):
        """ 返回最小节点 """

        if not node:
            node = self.root
        while node.left != self.nil:
            node = node.left
        return node

    def insert(self, node):
        """ 插入红黑树节点 """

        _ = self.nil
        x = self.root
        while x != self.nil:
            _ = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = _
        # 如果得到的临时节点是哨兵节点，则说明x为根节点
        # 置node为新的根节点
        if _ == self.nil:
            self.root = node
        # 否则如果x不是根节点，则将node置为_的左孩子或右孩子
        elif node.key < _.key:
            _.left = node
        else:
            _.right = node
        # 将node的左右孩子全置为哨兵节点，同时颜色置为红色
        node.left = self.nil
        node.right = self.nil
        node.color = RED
        self.insert_fix(node)

    def insert_fix(self, node):
        """ 插入节点之后进行红黑树修复 """

        while node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                _ = node.parent.parent.right
                # 如果node祖父节点的右孩子是红色
                # 则将node的父节点和祖父节点的右孩子改为黑色，将祖父节点改为红色
                # 再以此时的祖父为起点进行后续修复
                if _.color == RED:
                    node.parent.color = BLACK
                    _.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                # 如果node祖父节点的右孩子是黑色
                else:
                    # 如果node插入位置是父节点的右边，则要进行左旋
                    if node is node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            else:
                _ = node.parent.parent.left
                if _.color == RED:
                    node.parent.color = BLACK
                    _.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)
        self.root.color = BLACK

    def delete(self, node):
        """ 删除红黑树节点 """

        delete_node = node
        # 记录节点原始颜色
        original_color = delete_node.color
        # 如果左孩子是哨兵节点
        if node.left == self.nil:
            # 将node的右孩子节点和node进行替换
            _ = node.right
            self.transplant(node, node.right)
        elif node.right == self.nil:
            # 将node的左孩子节点和node进行替换
            _ = node.left
            self.transplant(node, node.left)
        else:
            delete_node = self.minimum(node.right)
            original_color = delete_node.color
            _ = delete_node.right
            if delete_node.parent == node:
                _.parent = delete_node
            else:
                self.transplant(delete_node, delete_node.right)
                delete_node.right = node.right
                delete_node.right.parent = delete_node
            self.transplant(node, delete_node)
            delete_node.left = node.left
            delete_node.left.parent = delete_node
            delete_node.color = node.color
        if original_color == BLACK:
            self.delete_fix(_)

    def delete_fix(self, node):
        """ 删除节点之后进行红黑树修复 """

        while node != self.root and node.color == BLACK:
            # 如果节点是左节点
            if node == node.parent.left:
                _ = node.parent.right
                # 因如果node的颜色为黑，则祖父节点的另外一个孩子节点也应该为黑
                # 父节点应该为红
                if _.color == RED:
                    _.color = BLACK
                    node.parent.color = RED
                    # 因改了右节点(此时_为右节点)的颜色，所以左旋
                    self.left_rotate(node.parent)
                    _ = node.parent.right
                # 两个子节点为黑，则该节点为红
                if _.left.color == BLACK and _.right.color == BLACK:
                    _.color = RED
                    node = node.parent
                # 两个子节点不都为黑
                else:
                    if _.right.color == BLACK:
                        _.left.color = BLACK
                        _.color = RED
                        # 因改变了左边节点(此时_为左节点)的颜色，所以右旋
                        self.right_rotate(_)
                        _ = node.parent.right
                    _.color = node.parent.color
                    node.parent.color = BLACK
                    _.right.color = BLACK
                    # 因改变了右节点(_.right为右节点)的颜色，所以左旋
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                _ = node.parent.left
                if _.color == RED:
                    _.color = BLACK
                    node.parent.color = RED
                    self.right_rotate(node.parent)
                    _ = node.parent.left
                if _.left.color == BLACK and _.right.color == BLACK:
                    _.color = RED
                    node = node.parent
                else:
                    if _.left.color == BLACK:
                        _.right.color = BLACK
                        _.color = RED
                        self.left_rotate(_)
                        _ = node.parent.left
                    _.color = node.parent.color
                    node.parent.color = BLACK
                    _.left.color = BLACK
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = BLACK

    def transplant(self, delete_node, node):
        """ 辅助方法 
            delete_node ： 要删除的节点
            node        ： 替换的节点
        """

        # 如果删除的节点的父节点是哨兵节点，
        # 则删除的节点是根节点，设置node为新的根节点
        if delete_node.parent == self.nil:
            self.root = node
        # 如果删除的节点是父节点的左孩子，则设置node为父节点新的左孩子
        elif delete_node == delete_node.parent.left:
            delete_node.parent.left = node
        else:
            delete_node.parent.right = node
        # 设置node为删除的节点的父节点的子节点
        node.parent = delete_node.parent

    def left_rotate(self, node):
        """ 左旋 """

        # 如果节点的右边的孩子不是哨兵节点
        right = node.right
        if right is not self.nil:
            # node的右孩子变为right的左孩子
            node.right = right.left
            # 如果right的左孩子不是哨兵节点
            # 将左孩子的父节点置为node
            if right.left != self.nil:
                right.left.parent = node
            # 将node右孩子right的父节点从node置为node的父节点
            right.parent = node.parent
            # 如果node的父节点是哨兵节点
            # 则说明node是根节点
            # 将right置为新的根节点
            if node.parent == self.nil:
                self.root = right
            # 如果node不是根节点，且node的父节点的左孩子是node
            # 则将right置为node父节点新的左孩子
            elif node == node.parent.left:
                node.parent.left = right
            # 否则将right置为node父节点新的右孩子
            else:
                node.parent.right = right
            # right的左孩子置为node
            right.left = node
            # node的父节点置为right
            node.parent = right

    def right_rotate(self, node):
        """ 右旋 """

        # 如果节点的左边孩子不是哨兵节点
        left = node.left
        if left is not self.nil:
            # node的左孩子变为left的右孩子
            node.left = left.right
            # 如果left的右孩子不是哨兵节点
            # 将右孩子的父节点置为node
            if left.right != self.nil:
                left.right.parent = node
            # 将node左孩子left的父节点从node置为node的父节点
            left.parent = node.parent
            # 如果node的父节点是哨兵节点
            # 则说明node是根节点
            # 将left置为新的根节点
            if node.parent == self.nil:
                self.root = left
            # 如果node不是根节点，且node的父节点的左孩子是node
            # 则将left置为node父节点新的左孩子
            elif node == node.parent.left:
                node.parent.left = left
            # 否则将left置为node父节点新的右孩子
            else:
                node.parent.right = left
            # left的右孩子置为node
            left.right = node
            # node的父节点置为left
            node.parent = left


if __name__ == '__main__':
    a = RBTree([2, 8, 7, 5, 4, 9, 45, 43, 14, 32, 24, 41, 25, 243, 124, 464, 12, 21, 1])
    print(a)
