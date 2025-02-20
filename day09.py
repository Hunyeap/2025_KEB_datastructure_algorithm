class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:
        return new_node

    current = root
    while True:
        if group < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right  # move

print("BST 구성 완료")
pass

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers:
        root = insert(root, number)

    find_group = int(input())

    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.right