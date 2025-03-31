#include <iostream>
#include <vector>


int swp;



using namespace std;

void selectionSort(vector<int>& arr) 
{
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) 
    {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) 
        {
            if (arr[j] < arr[minIndex]) 
            {
                minIndex = j;
            }
        }
        swap(arr[i], arr[minIndex]);
    }
}


int main() {
    int a;
    
    vector<int> exampleVector;
    // Keep reading integers until a non-integer is encountered
    while (cin >> a) {
        exampleVector.push_back(a);
    }

    selectionSort(exampleVector);

    cout << exampleVector.size();

    return 0;
}