#include <iostream>
#include <vector>


using namespace std;


int podzial(vector<int>& tablica, int leftMarker, int rightMarker) {
    int pivot = tablica[rightMarker];
    int i = leftMarker - 1;

    for (int j = leftMarker; j < rightMarker; j++) {
        if (tablica[j] < pivot) {
            i++;
            swap(tablica[i], tablica[j]);
        }
    }
    swap(tablica[i + 1], tablica[rightMarker]);
    return i + 1;
}

void quickSort(vector<int>& tablica, int leftMarker, int rightMarker) {

    if (leftMarker < rightMarker) 
    {
        int pi = podzial(tablica, leftMarker, rightMarker);


        quickSort(tablica, leftMarker, pi - 1);
        quickSort(tablica, pi + 1, rightMarker);
    }
}


int main() {
    int a;
    
    vector<int> exampleVector;
    // Keep reading integers until a non-integer is encountered
    while (cin >> a) {
        exampleVector.push_back(a);
    }

    quickSort(exampleVector, 0, exampleVector.size() - 1);

    cout << exampleVector.size();

    return 0;
}