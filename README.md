Оптимизационные задачи в машинном обучении. 


В папке TZ1 находятся функции для поиска экстремума функции двух переменных. 

Функции возвращают список координат и значение функции в точке, для всех точек локальных экстремумов,
с указанием типа экстремума (минимум, максимум, седловая точка), а также графики этих функций с изображением точек экстремума и график линий уровня.

В папке TZ2 находятся функции для поиска экстремума функций одной переменной. 

Используются методы: золотого сечения, парабол, Брента. 
                     
Функции возвращают найденную точку экстремума, значение функции в ней. 
Функция plot() визуализирует работу алгоритма золотого сечения. 

В папке TZ_3 находятся функции для поиска экстремума функции многих переменной методом градиентного спуска с постоянным шагом.

Результат работы алгоритма:
X = [0.20589113];Y = [0.04239116]
<img width="1000" alt="image" src="https://user-images.githubusercontent.com/99407452/163035557-850b41b1-a50e-48af-9b9d-4a664f3ea067.png">
<img width="979" alt="image" src="https://user-images.githubusercontent.com/99407452/163035661-58073e88-52a5-4059-86cd-9e9c15a1b12a.png">

Используются следующие функции: 
1. Функция, определяющая длину оптимального шага градиентного спуска на основе градиента и Гессиниана
Результат работы алгоритма:
X = [0.04032712 0.04032712]
Y = [0.01788904]
<img width="961" alt="image" src="https://user-images.githubusercontent.com/99407452/163035980-65e54e93-975c-477d-a61b-150744ed54bd.png">
<img width="946" alt="image" src="https://user-images.githubusercontent.com/99407452/163036005-43b47967-b869-423d-b02a-44e7fdaff8e4.png">

3. Функция, реализующАЯ алгоритм градиентного спуска с переменным шагом
Результат работы алгоритма:
X = [4.26704127e-15 4.99762838e-02]
Y = [0.00249763]
<img width="827" alt="image" src="https://user-images.githubusercontent.com/99407452/163036141-3b5397d1-cf62-45be-9619-001dc1da6237.png">
<img width="1001" alt="image" src="https://user-images.githubusercontent.com/99407452/163036191-9aeab944-491b-4d7b-ba61-4ee8e4498f60.png">

5. Функция, реализующая метод наискорейшего спуска, используящая в качестве метода одномерной оптимизации метод Брента
Результат работы алгоритма:
X = [2.92841771e-05 2.92841771e-05]
Y = [9.43319333e-09]
<img width="950" alt="image" src="https://user-images.githubusercontent.com/99407452/163036261-36f65f79-5654-464e-8c50-42993a24be40.png">

Функции возвращают найденную точку экстремума, значение функции в ней, количество итераций. 


В папке ТЗ_4 находятся функции, релизующие различные виды регрессии – линейная ,полиномиальная: L1,L2. 


Результаты работы линейной регрессии со степенью 1 и оценка синусоидальной функции с использованием полиномиальной регрессии со степенями x от 1 до 15.
<img width="679" alt="image" src="https://user-images.githubusercontent.com/99407452/163722121-0b4682c1-b7d2-40ff-b0af-056ff2d8ec0b.png">

Для удобства анализа реализован альтернативный формат отображения:
<img width="1157" alt="image" src="https://user-images.githubusercontent.com/99407452/163722261-19b9fe11-1190-44a5-b3a9-261c586e5422.png">

Ridge Regression(L2) с различными степенями alpha:
<img width="742" alt="image" src="https://user-images.githubusercontent.com/99407452/163722608-af3498d3-2a5b-442a-a075-bbfbc66172d2.png">

Для удобства анализа реализован альтернативный формат отображения:
<img width="1241" alt="image" src="https://user-images.githubusercontent.com/99407452/163722381-db1a964e-aba8-443c-8a6d-a4a7431037f2.png">

Lasso Regression(L1) с различными степенями alpha:

<img width="735" alt="image" src="https://user-images.githubusercontent.com/99407452/163722548-14fdaf27-0422-4512-8235-8d6d21374706.png">

Для удобства анализа реализован альтернативный формат отображения:
<img width="1282" alt="image" src="https://user-images.githubusercontent.com/99407452/163722567-3085dd85-2737-4225-b2a2-b6a8b8482236.png">
