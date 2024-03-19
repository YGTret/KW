1. Создал 2 файла
cat > "Домашние животные" <<EOF
Собаки
Кошки
Хомяки
EOF


cat > "Вьючные животные" <<EOF
Лошади
Верблюды
Ослы
EOF

2. Объединил их
cat "Домашние животные" "Вьючные животные" > "Животные

3. Переименовал файл
mv "Животные" "Друзья человека"

4. Подключение репозитория и установка пакета
sudo nano /etc/apt/sources.list.d/mysql-apt-config.list

Добавил следующую строку в этот файл 
deb http://repo.mysql.com/apt/ubuntu/ focal mysql-apt-config

Добавил GPG-ключ
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8C718D3B5072E1F5

И установил сервер MySQL
sudo apt install mysql-server

5. Установка и удаление deb-пакета
sudo dpkg -i mc_4.8.29-2_amd64.deb

sudo dpkg -r mc