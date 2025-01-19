# Обработка изображений в градациях серого

## Описание
Этот скрипт предназначен для пакетной обработки изображений, находящихся в указанной папке. Он использует многопоточность для одновременной обработки изображений, преобразуя их в градации серого и сохраняя результаты в выходной папке. Скрипт использует библиотеку `PIL` (Pillow) для работы с изображениями.

## Установка
1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.6 и выше).
2. Установите библиотеку Pillow, если она еще не установлена:
   ```bash
   pip install Pillow
## Структура папок
input_images/: Папка, содержащая изображения для обработки. Поддерживаемые форматы: PNG, JPG, JPEG, BMP, GIF.
output_images/: Папка, в которую будут сохранены обработанные изображения. Если папка не существует, она будет создана автоматически.
Использование
Поместите изображения, которые вы хотите обработать, в папку input_images.

Запустите скрипт:

python script_name.py
Замените script_name.py на имя вашего файла со скриптом.

После завершения обработки вы найдете преобразованные изображения в папке output_images.

## Как работает код
Производитель (producer): Функция producer считывает все изображения из папки input_images и помещает их пути в очередь image_queue. После завершения добавляет сигналы завершения для каждого потребителя.

Потребители (consumer): Функция consumer извлекает пути к изображениям из очереди и обрабатывает их. Каждое изображение преобразуется в градации серого и сохраняется в выходной папке. Если возникает ошибка при обработке, она будет выведена в консоль.

Скрипт использует 16 потоков (параметр num_consumers), но вы можете изменить это значение, чтобы адаптировать производительность к вашему оборудованию.

## Примечания
Убедитесь, что папка input_images не содержит слишком большого количества изображений, чтобы избежать переполнения памяти.
Обработка изображений может занять некоторое время в зависимости от количества и размера изображений.
В случае возникновения ошибок при обработке изображений, они будут выведены в консоль, и обработка продолжится для остальных изображений.

## Завершение работы
После завершения обработки скрипт выведет сообщение "Обработка изображений завершена."
