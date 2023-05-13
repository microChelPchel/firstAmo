from sklearn.preprocessing import StandardScaler
import numpy as np
import os

def data_preprocessing(path):
    # Для каждой папки (train и test) выполняем предобработку
    for folder_name in ['train', 'test']:
        # Считываем все файлы из папки
        folder_path = os.path.join(path, folder_name)
        file_names = os.listdir(folder_path)
        # Для каждого файла выполняем предобработку
        for file_name in file_names:
            # Считываем данные из файла и переводим в numpy-массив
            file_path = os.path.join(folder_path, file_name)
            data = np.loadtxt(file_path, delimiter=',', dtype=None)
            data = data.reshape(-1, 1)   # Изменяем размерность массива
            # Стандартизируем данные с помощью StandardScaler
            scaler = StandardScaler()
            data = scaler.fit_transform(data)
            # Сохраняем предобработанные данные в файл с именем 'original_name_scaled.txt'
            new_file_path = os.path.join(folder_path, file_name[:-4] + '_scaled.txt')
            np.savetxt(new_file_path, data, delimiter=',')

if __name__ == '__main__':
    # Путь к папке с тренировочными и тестовыми данными
    path = '.'
    data_preprocessing(path)