# map_repo
Map of nearest films spots
Призначення модуля:
Модуль призначений для генерації html-карти на якій позначено місця найближчих місць зйомок фільмів певного року.

Інформацію, яку нам надає така карта;
Модуль позначає мітки місць зйомок фільмів та інформацію до них, а саме, назва локації та назва самого фільму.

Шари:
1) Основний шар
2) Шар міток
3) Шар зони де всі мітки знаходяться

Уточнення:
1) Через велику кількість данних в location.list, створив модуль get_data.py який рандомно вибирає з location.list задану кількість фільмів та зберігає в файлі small_films.list.
2) Модуль main.py працює саме small_films.list, адже в цей файл відбираються тільки фільми (без рядків верхніх рядків ініціалізації, які потрібно пропускати).
3) Через те, що деякі сцени фільмів знімали в одних місцях, модуль рандомно розтасовує ці мітки на мінімальне значення, для того щоб їх розрізняти.

Приклад:
Для прикладу були використані координати 48.444070 4.662629 (Франція) та 2003 рік як дані використано small_films.list на 15000 фільмів.

![image](https://user-images.githubusercontent.com/69431189/219314640-7791f590-9886-4bf6-8939-08a6fc5dd192.png)

Приклад тасування міток якщо вони на одному місці(Наприклад ці Paris, France)
![image](https://user-images.githubusercontent.com/69431189/219314732-8e2726aa-8591-411a-b27d-203992db02ec.png)

Керування шарами
![image](https://user-images.githubusercontent.com/69431189/219315068-3cea1a08-c588-47f4-a155-9f96de01bef3.png)
