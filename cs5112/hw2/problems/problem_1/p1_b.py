# Problem 1b

def get_root(vertices, adjacency):
    all_children = set([child for children in adjacency.values() for child in children])
    for node in vertices:
        if node not in all_children:
            return node
    return None

def maxsum_tree_naive(vertices, adjacency) -> int:    
    root = get_root(vertices, adjacency)

    def dfs(node):
        with_current = vertices[node]
        for child in adjacency[node]:
            for grandchild in adjacency[child]:
                with_current += dfs(grandchild)
        
        without_current = 0
        for child in adjacency[node]:
            without_current += dfs(child)
        
        return max(with_current, without_current)
    
    return dfs(root)

def maxsum_tree(vertices, adjacency) -> int:    
    root = get_root(vertices, adjacency)

    memo = {}

    def dfs(node):
        if node in memo:
            return memo[node]
        
        with_current = vertices[node]
        for child in adjacency[node]:
            for grandchild in adjacency[child]:
                with_current += dfs(grandchild)

        without_current = 0
        for child in adjacency[node]:
            without_current += dfs(child)

        memo[node] = max(with_current, without_current)
        return memo[node]

    return dfs(root)

