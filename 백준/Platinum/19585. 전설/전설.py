import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search_prefix(self, prefix: str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def exists(self, word: str):
        node = self.search_prefix(word)
        return node is not None and node.is_end


def check(word, color_trie, names):
    node = color_trie.root
    for i in range(len(word)):
        if node.is_end and word[i:] in names:  # 색상 부분이 존재하고, 나머지가 닉네임에 있으면
            return True
        if word[i] not in node.children:  # 색상 부분이 존재하지 않으면 종료
            return False
        node = node.children[word[i]]
    return False


def main():
    # 입력 받기
    C, N = map(int, input().split())

    color_trie = Trie()
    names = set()

    for _ in range(C):
        color_trie.insert(input().strip())

    for _ in range(N):
        names.add(input().strip())

    Q = int(input().strip())

    results = []
    for _ in range(Q):
        team_name = input().strip()
        results.append("Yes" if check(team_name, color_trie, names) else "No")

    # 결과 출력
    for res in results :
        print(res)


if __name__ == "__main__":
    main()
