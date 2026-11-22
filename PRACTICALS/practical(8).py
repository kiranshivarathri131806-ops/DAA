#include <iostream>
#include <vector>
#include <queue>
#include <chrono>

using namespace std;
using namespace std::chrono;

class NetworkGraph {
    int totalNodes;
    vector<vector<int>> adjacencyMatrix;

public:
    NetworkGraph(int nodeCount) {
        totalNodes = nodeCount;
        adjacencyMatrix.resize(totalNodes);
    }

    void connectNodes(int sourceNode, int targetNode) {
        adjacencyMatrix[sourceNode].push_back(targetNode);
        adjacencyMatrix[targetNode].push_back(sourceNode);   // Remove this line for directed graph
    }

    void performDFSRecursive(int currentNode, vector<bool> &isVisited) {
        isVisited[currentNode] = true;
        cout << currentNode << " ";

        for (int adjacentNode : adjacencyMatrix[currentNode]) {
            if (!isVisited[adjacentNode])
                performDFSRecursive(adjacentNode, isVisited);
        }
    }

    void depthFirstSearch(int initialNode) {
        vector<bool> isVisited(totalNodes, false);
        performDFSRecursive(initialNode, isVisited);
    }

    void breadthFirstSearch(int initialNode) {
        vector<bool> isVisited(totalNodes, false);
        queue<int> processingQueue;

        isVisited[initialNode] = true;
        processingQueue.push(initialNode);

        while (!processingQueue.empty()) {
            int currentElement = processingQueue.front();
            processingQueue.pop();

            cout << currentElement << " ";

            for (int adjacentNode : adjacencyMatrix[currentElement]) {
                if (!isVisited[adjacentNode]) {
                    isVisited[adjacentNode] = true;
                    processingQu 
}
