#!/bin/bash

echo 'запуск скрипта создания данных'
python data_creation.py

echo 'запуск скрипта обработки и стандартизации данных'
python model_preprocessing.py

echo 'запуск скрипта создания модели и обучения'
python model_preparation.py

echo 'запуск скрипта создания модели и обучения'
python model_testing.py
