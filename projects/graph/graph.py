"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        
        # First check to see if vertex is in vertices
        if vertex not in self.vertices:
            # If not in vertices, add it
            self.vertices[vertex] = []
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # First check if edge is present
        if v1 in self.vertices:
            self.vertices[v1].append[v2]
        else:
            self.vertices[v1] = [v2]
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visisted = set()
        while q:
            vertex = q.pop(0)
            if vertex not in visisted:
                print(vertex)
                visisted.add(vertex)
                q.extend(self.vertices[vertex] - visited)
        return visisted

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # First we will take the starting vertex and push it
        # Into a newly made instance of Stack
        s = Stack()
        s.push(starting_vertex)
        # We need to store the visited points
        visited = set()
        # A loop needs to run as long as the stack isn't empty
        while s.size() > 0:
            #Pop out first vertex
            vert = s.pop()
            # If not in visited, mark it as visited
            if vert not in visited:
                print (vert)
                # TODO - finish add_vertex def!
                # visited.add(vert)
                # And then add all neighbors to stack
                for next_vert in self.vertices[vert]:
                    s.push(next_vert)
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # We will use stack here for dft
        visited, stack = set(), [starting_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                # visited.add(vertex)
                print(vertex)
                stack.extend(self.vertices[vertex] - visited)
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Here we will use a queue
        q = Queue()
        # Load up the starting vertex
        q.enqueue([starting_vertex])
        #Initialize the visisted set
        visited = set()
        # Run a loop as long as q contains anything
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                if v = destination_vertex:
                    return path
                visited.add(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.dequeue(new_path)
        return None
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # We will use a stack here
        s = Stack()
        # Next, we will load up the starting vertex
        s.push([starting_vertex])
        # Initialize visisted
        visisted = set()
        # Run a loop as long as the stack contains anything
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v not in visisted:
                if v == destination_vertex:
                    return path
                visited.add(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)
        return None

        





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
