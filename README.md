братва смотрите по шагам все распишу

1)клонируете проект себе в папку
2) ставите себе на винду докер, тут уже сами как-то
3) заходите в корень проекта, который склонировали, корень это там где будет docker-compose.yml файл
4) открываете терминал в этом корне и пишете там docker compose up --build
5) ждете туда сюда пока все там поднимется
6) потом скачиваете себе на комп прогу называется ngrok просто открываете exe файл котоырй с официального сайта скачаете себе
в консоли там по инструкции с сайта пропишете все что надо, потом пишете ngroc http 80  в той же консоли ngrok
там у вас появится че то типа
Forwarding                    https://004d-176-106-245-245.ngrok-free.app -> http://localhost:80
такой строчки, потом берете первкю ссылку, которая будет https://004d-176-106-245-245.ngrok-free.app у меня вот эта у вас другие
и вставляете ее в simple_worker/tasks.py на место где у меня моя ссылка находится
потом открываете че хотите через что запросы слать, postman обычный курлом как хотите и отправляете данные как делали до этого в лабе где без rabbitmq было
или если вы не отправляете данные, а они  у вас просто в проге были написана, то поменяйте файл этот tasks.py
и не используйте там переменные из аргументов, а просто свои руками напишите и все
делаете запрос и все работает