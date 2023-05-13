import random
import os

# Создаем папки "train" и "test", если их еще нет
if not os.path.exists('train'):
    os.mkdir('train')
if not os.path.exists('test'):
    os.mkdir('test')

# Функция для генерации набора данных о изменении температуры
def generate_data(start_temp, num_days, anomaly=None, noise=None):
    data = []
    temp = start_temp
    for i in range(num_days):
        if anomaly and i == anomaly[0]:
            temp += anomaly[1]
        if noise:
            temp += random.uniform(-noise, noise)
        data.append(temp)
    return data

# Создаем n наборов данных для обучения модели
def create_train_data(count):
    for i in range(count):
        data = generate_data(20, 365, anomaly=(50, -5), noise=2)
        with open(f'train/data_{i}.txt', 'w') as f:
            f.writelines(str(d) + '\n' for d in data)


# Создаем n наборов данных для тестирования модели
def create_test_data(count):
    for i in range(count):
        data = generate_data(20, 365, anomaly=(100, 10), noise=3)
        with open(f'test/data_{i}.txt', 'w') as f:
            f.writelines(str(d) + '\n' for d in data)

if __name__ == '__main__':
    create_train_data(5)
    create_test_data(2)