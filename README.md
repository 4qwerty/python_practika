# Створення та привязка SSH ключа

Прописуємо в консолі `ssh-keygen-t rsa -b 4096 -C “example@gmail.com”`(вказавши свою електронну пошту яка привязана до github)

![изображение](https://user-images.githubusercontent.com/50421230/124351957-1e3a8c00-dc06-11eb-9906-32b3e1e60a19.png)

За часту він розміщений на диску C в папці користувач заходимо і шукаємо папку .ssh

![изображение](https://user-images.githubusercontent.com/50421230/124352074-bf294700-dc06-11eb-8735-72c3c0d8f04a.png)

Знаходимо публічний ключ та копіюємо

![изображение](https://user-images.githubusercontent.com/50421230/124352438-cd786280-dc08-11eb-88a9-442d40057212.png)

В github шукаємо налаштування і пункт SSH and GPG keys, вставляємо наш ключ і зберігаємо

![изображение](https://user-images.githubusercontent.com/50421230/124352660-652a8080-dc0a-11eb-9598-c30ebc13f434.png)

Ключ створений залишилось привязати його до репозиторія, для цього копіємо наш репозиторій за допомогою SSH

![изображение](https://user-images.githubusercontent.com/50421230/124352761-0fa2a380-dc0b-11eb-9b58-837bcc849046.png)

Прописуємо 'git clone' плюс силку яку ми скопіювали попередньо

![изображение](https://user-images.githubusercontent.com/50421230/124352785-3d87e800-dc0b-11eb-883e-d0998bb7739f.png)

Ну і все ключ успішно привязаний

![изображение](https://user-images.githubusercontent.com/50421230/124352803-67d9a580-dc0b-11eb-9529-531066c43c88.png)

# Написання програми і додавання в GitHub

![изображение](https://user-images.githubusercontent.com/50421230/124354732-1be02e00-dc16-11eb-829f-e63fbc1b5c5b.png)

![изображение](https://user-images.githubusercontent.com/50421230/124354912-2ea73280-dc17-11eb-82a6-a59d12459621.png)
