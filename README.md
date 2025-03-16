# Tester algorytmów do AiSD 

## Działanie programu:
1. Losowanie liczb zgodnych z wymaganiami (losowe, rosnąco malejące, malejąco rosnące)
2. Odpalenie programu użytkownika dla wszystkich setów danych
3. Zapisanie wyników czasowych w excelu oraz wygenerowanie wykresów dla każdego typu danych
4. Ponowne losowanie danych
5. 10-cio krotne powtórzenie czynności w celu zebrania dokładniejszych danych

## How to use?
1. Pobrać lub sklonować kod robiąc to ręcznie lub wykorzystując komendę:
   ```bash
   git clone https://github.com/Misiolol/AiSD---Tester.git
   ```
2. Pobrać potrzebne biblioteki:
   ```bash
   pip install openpyxl
   pip install pandas
   pip install matplotlib
   ```
3. Zeedytować kod aby wprowadzanie danych wyglądało w następujący sposób:
   ```cpp
   int a;
    
    vector<int> exampleVector;
    // Keep reading integers until a non-integer is encountered
    while (cin >> a) {
        exampleVector.push_back(a);
    }```
4. Skomplikować kod a program wykonywalny (a.exe) umieścić w pliku razem z test.py<br>
![image](https://github.com/user-attachments/assets/1a1d2df1-1988-40ea-a13f-24da5491cc45)<br>
5. Odpalić tester komendą
  ```bash
  python test.py
```
lub
```bash
python3 test.py
```
5. Odczekać aż tester skończy swoją pracę, wszystkie informacje o pracującym programie pojawiać się będą w konsoli<br>
![image](https://github.com/user-attachments/assets/8bbd533e-65c1-4f08-9c18-18feeb4d506f)

6. Wyniki pojawią się w pliku user-outputs <br>




