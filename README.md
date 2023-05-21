# Проект firstAmo

Описание проекта, в котором создаются скрипты для решения задачи машинного обучения.

## Установка зависимостей

Для работы скриптов необходимо установить следующие зависимости:
- scikit-learn
- pandas

bash  
pip install scikit-learn pandas


## Структура проекта


project/  
│  
├── data_creation.py  
├── model_preprocessing.py  
├── model_preparation.py  
├── model_testing.py  
├── pipeline.sh  
│  
├── train/  
│   ├── dataset_1.csv  
│   ├── dataset_2.csv  
│   └── ...  
│  
└── test/  
    ├── dataset_1.csv  
    ├── dataset_2.csv  
    └── ...  
  

## Описание скриптов

### data_creation.py

Создает различные наборы данных, описывающие некий процесс. Некоторые наборы данных могут содержать аномалии или шумы. Часть наборов данных сохраняется в папке "train", другая часть - в папке "test".

### model_preprocessing.py

Выполняет предобработку данных с помощью sklearn.preprocessing.StandardScaler.

### model_preparation.py

Создает и обучает модель машинного обучения на данных из папки "train".

### model_testing.py

Проверяет модель машинного обучения на данных из папки "test".

### pipeline.sh

Последовательно запускает все python-скрипты.

#!/bin/bash  
python3 data_creation.py  
python3 model_preprocessing.py  
python3 model_preparation.py  
python3 model_testing.py    


## Запуск проекта

bash  
./pipeline.sh  


## Автор

- Соколов Александр (@microChelPchel)