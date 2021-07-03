# Створення та привязка SSH ключа

Прописуємо в консолі ssh-keygen-t rsa -b 4096 -C “example@gmail.com”(вказавши свою електронну пошту яка привязана до github)

![изображение](https://user-images.githubusercontent.com/50421230/124351957-1e3a8c00-dc06-11eb-9906-32b3e1e60a19.png)

Вітаю він створенний, за часту він розміщений на диску C в папці користувач заходимо і шукаємо .ssh

![изображение](https://user-images.githubusercontent.com/50421230/124352074-bf294700-dc06-11eb-8735-72c3c0d8f04a.png)

Заходимо в публічний ключ та копіюємо

![изображение](https://user-images.githubusercontent.com/50421230/124352438-cd786280-dc08-11eb-88a9-442d40057212.png)

Заходимо в налаштування і знаходимо пункт SSH and GPG keys, вставляємо наш ключ і зберігаємо

![изображение](https://user-images.githubusercontent.com/50421230/124352660-652a8080-dc0a-11eb-9598-c30ebc13f434.png)

Ключ створений залишилось привязати його до репозиторія, для коцього копіємо наш репозиторій за допомогою SSH

![изображение](https://user-images.githubusercontent.com/50421230/124352761-0fa2a380-dc0b-11eb-9b58-837bcc849046.png)

Прописуємо 'git clone' плюс силку

![изображение](https://user-images.githubusercontent.com/50421230/124352785-3d87e800-dc0b-11eb-883e-d0998bb7739f.png)

