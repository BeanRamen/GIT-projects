https://github.com/user-attachments/assets/b13614ad-9790-4d78-b8bf-2fc70ee8ec3d

In captura de ecran putem observa modul in care programul functioneaza si aproximativ unde sunt pozele procesate.

In primul rand, dupa rularea programului ParkingSpacePicker.py, se deschide imaginea de baza, parcarea in totalitate. Aici selectam locurile de parcare pe car vrem sa le procesam si sunt marcate cu culoarea mov.
Dupa ce le selectam, pozitia lor este salvata in fisierul CarParkPos (car park position) in odinea coordonatelor cursorului, pentru usurinta.
Pozitia va fi afisata de fiecare data, pentru a sterge un cadran se foloseste right-click si pozitia va fi stearsa din fisier si astfel din imagine.

Cand rulam filter_newParking.ipynb, cadranele sunt decupate si redimensionate la (256,256) pentru a fi mai usor compatibile modelului tensorflow.
Pozele redimensionate sunt apoi verificare pentru a vedea daca sunt sau nu ocupate.
Informatia este salvata intr-un fisier txt numit predictions.txt, unde sunt locurile de parcare in ordinea pozitiei din CarParkPos si in dreapta lor "1" - ocupat / "0" - liber

La rularea main.py este incarcata imaginiea mare si locurile decupate. In imaginea mare cadranele mov se transforma in verde sau rosu (liber / ocupat) conform fisierului txt.

Modelul tensorflow este creat si testat in CNN_first_model.ipynb.
Modelul este antrenat pe cca 150 de poze cu locuri de parcare ocupate sau goale din appl/asset/data.
Imaginile sunt impartite automat in fucntie de subfoldere (empty/occup) in ordine alfabetica => empty -> 0 / occup -> 1.


Toate imaginile, inafara de parcare, sunt redimesnionate la (256,256).

Rosca Pavel-Daniel.
