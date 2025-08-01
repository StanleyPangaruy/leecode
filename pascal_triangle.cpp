#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> generate(int numRows) {
    if (numRows <= 0) return {};

    vector<vector<int>> triangle(numRows);
    for (int i = 0; i < numRows; ++i) {
        triangle[i] = vector<int>(i + 1, 1);
        for (int j = 1; j < i; ++j) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }
    return triangle;
}

int main() {
    int numRows = 5;
    auto result = generate(numRows);
    for (const auto& row : result) {
        cout << "[";
        for (size_t i = 0; i < row.size(); ++i) {
            cout << row[i];
            if (i < row.size() - 1) cout << ", ";
        }
        cout << "]\n";
    }
    return 0;
}