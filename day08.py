class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

if __name__ == "__main__":
    groups = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
    # groups = [10, 15, 4, 3, 27, 40]
    root = None

    node = TreeNode()
    node.data = groups[0]
    root = node
    for group in groups[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
    print("BST complete")
    find_group = input()

    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다.")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다.")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다.")
                break
            current = current.right