# [Padkraduli] Binarizare globală
JIRA -> mpsproiect.atlassian.net
## FMeasure
FMeasure e calculat comform urmatorului algoritm:
Pentru un rând asociat unei imagini se obține o anumită valoare în intervalul 0-1, ex: 0.78. Valoarea respectivă se înmulțește cu 255, se aplică o operație de round pe aceasta, iar rezultatul final reprezintă un index pentru a determina care ar fi FMeasure-ul ce ar putea fi obținut pe respectiva imagine în urma rulării arborelui respectiv: 
```python
idx = round(255 * val)
```
ex: idx = round(255 * 0.78) = 198 pe baza indexului astfel obținut se caută în cele 256 de valori de FMeasure asociate diverselor praguri care ar fi valoarea arborelui pe respectiva imagine, se repetă pasul pe toate rândurile din fișierul csv și se determină un potențial FMasure pentru fiecare rând asociat unei imagini se calculează o medie a F-measure-rilor astfel obținute.

## Tree
Am folosit arborii Monte Carlo (sau ceva de genul), bazat pe următorii pași:
* Determină un arbore cu un număr aleator de niveluri, pe baza unei limite 
* Pentru fiecare nivel determină un număr aleator de noduri, la fel ca și în cazul numărului de nivele pe baza unei limite
* Pentru fiecare nivel, începând cu cel frunză și terminând cu cel rădăcină alege un nod cu o operație aleatoare și un număr de potențiale noduri copil

## Operatiuni
* max/min
```python
"""
    data - List of data.
"""
functions.min_leafs(data)
functions.max_leafs(data)
```
* medie aritmetică
```python
"""
    data - List of data.
"""
functions.arithmetic_average(data)
```
* medie geometrică
```python
"""
    data - List of data.
"""
functions.geometric_average(data)
```
* mediană
```python
"""
    data - List of data.
"""
functions.calculate_median(data)
```
* Limita sinusoidala
```python
"""
    data - List of data.
"""
functions.sin_limit(data)
```

## Rulare
Pentru rulare trebuie instalate packetele specificate in requirements.txt
```cmd
pip install -r /path/to/requirements.txt
```
Se ruleaza in felul urmator
```cmd
python .\init.py /path/to/LUTfile.csv /path/to/Globalfile.csv
```
## Echipa
Girnet Andrei

David Mihalcenco

Veacesal Cazanov

Mihaela Felicia SZŐCS

Andrei Mihai Cosmin
