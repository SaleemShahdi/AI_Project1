# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    #print(problem.goal)
    stack = util.Stack()
    hasbeenVisited = []
    solutionpath = []
    startState = problem.getStartState()
    if problem.isGoalState(startState) == True:
        return solutionpath
    hasbeenVisited.append(startState)
    startSuccessors = problem.getSuccessors(startState)
    for successor in startSuccessors:
        state = successor[0]
        path = [successor[1]]
        stack.push((state, path))
    while (stack.isEmpty() == False):
        current = stack.pop()
        currentstate = current[0]
        if (currentstate in hasbeenVisited):
            continue
        hasbeenVisited.append(currentstate)
        if (problem.isGoalState(currentstate) == True):
            return current[1]
        else:
            currentSuccessors = problem.getSuccessors(currentstate)
            for successor in currentSuccessors:
                state = successor[0]
                direction = successor[1]
                path = current[1]+[direction]
                stack.push((state, path))







    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    hasbeenVisited = []
    solutionpath = []
    startState = problem.getStartState()
    #print(startState)
    if problem.isGoalState(startState) == True:
        return solutionpath
    hasbeenVisited.append(startState)
    startSuccessors = problem.getSuccessors(startState)
    for successor in startSuccessors:
        #print(successor)
        state = successor[0]
        path = [successor[1]]
        queue.push((state, path))
    while (queue.isEmpty() == False):
        current = queue.pop()
        currentstate = current[0]
        #print(currentstate)
        if (currentstate in hasbeenVisited):
            continue
        hasbeenVisited.append(currentstate)
        if (problem.isGoalState(currentstate) == True):
            return current[1]
        else:
            currentSuccessors = problem.getSuccessors(currentstate)
            for successor in currentSuccessors:
                #print(successor)
                state = successor[0]
                direction = successor[1]
                path = current[1] + [direction]
                queue.push((state, path))
    #util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    hasbeenVisited = []
    solutionpath = []
    startState = problem.getStartState()
    if problem.isGoalState(startState) == True:
        return solutionpath
    hasbeenVisited.append(startState)
    startSuccessors = problem.getSuccessors(startState)
    for successor in startSuccessors:
        state = successor[0]
        path = [successor[1]]
        bcc = successor[2]
        pq.push((state, path, bcc), bcc)
    while (pq.isEmpty() == False):
        current = pq.pop()
        currentstate = current[0]
        if (currentstate in hasbeenVisited):
            continue
        hasbeenVisited.append(currentstate)
        if (problem.isGoalState(currentstate) == True):
            return current[1]
        else:
            currentSuccessors = problem.getSuccessors(currentstate)
            for successor in currentSuccessors:
                bcc = current[2]
                state = successor[0]
                direction = successor[1]
                path = current[1] + [direction]
                priority = successor[2]
                bcc = bcc + priority
                pq.push((state, path, bcc), bcc)
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    #hasbeenVisited = dict()
    hasbeenVisited = []
    hasBeenVisitedCosts = []
    solutionpath = []
    startState = problem.getStartState()
    if problem.isGoalState(startState) == True:
        return solutionpath
    #hasbeenVisited[startState] = 0
    hasbeenVisited.append(startState)
    hasBeenVisitedCosts.append(0)
    startSuccessors = problem.getSuccessors(startState)
    for successor in startSuccessors:
        state = successor[0]
        path = [successor[1]]
        bcc = successor[2]
        fc = heuristic(state, problem)
        aStar = bcc + fc
        pq.push((state, path, bcc), aStar)
    while (pq.isEmpty() == False):
        current = pq.pop()
        currentstate = current[0]
        bcc = current[2]
        if currentstate in hasbeenVisited:
            if hasBeenVisitedCosts[hasbeenVisited.index(currentstate)] == bcc:
                continue
            if bcc < hasBeenVisitedCosts[hasbeenVisited.index(currentstate)]:
                hasBeenVisitedCosts[hasbeenVisited.index(currentstate)] = bcc
            if bcc > hasBeenVisitedCosts[hasbeenVisited.index(currentstate)]:
                continue
        else:
            hasbeenVisited.append(currentstate)
            hasBeenVisitedCosts.append(bcc)

        """if currentstate in list(hasbeenVisited):
            if hasbeenVisited.get(currentstate) == bcc:
                continue
            if bcc < hasbeenVisited.get(currentstate):
                hasbeenVisited[currentstate] = bcc
            if bcc > hasbeenVisited.get(currentstate):
                continue
        else:
            hasbeenVisited[currentstate] = bcc"""
        #hasbeenVisited[currentstate] = bcc
        #hasbeenVisited.append(currentstate)
        if (problem.isGoalState(currentstate) == True):
            return current[1]
        else:
            currentSuccessors = problem.getSuccessors(currentstate)
            for successor in currentSuccessors:
                bcc = current[2]
                state = successor[0]
                direction = successor[1]
                path = current[1] + [direction]
                priority = successor[2]
                bcc = bcc + priority
                fc = heuristic(state, problem)
                aStar = bcc + fc
                pq.push((state, path, bcc), aStar)
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
