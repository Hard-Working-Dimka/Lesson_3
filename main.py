import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

site_name = 'https://dvmn.org/referrals/PWV0aoUcF7VxdQwfdhYOcxk0gMxgQ7SWNGMwKgiZ/'
subject = 'Приглашение!'
content_type = 'text/plain; charset="UTF-8";'
letter_template = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.replace(
    '%website%', site_name).replace('%friend_name%', os.getenv('FRIEND_NAME')).replace('%my_name%', os.getenv('SENDER_NAME'))

letter = '''From: {0}
To: {1}
Subject: {2}
Content-Type: {3}

{4}
'''.format(os.getenv('MAIL_ADDRESS_FROM'), os.getenv('MAIL_ADDRESS_TO'), subject, content_type, letter_template)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(os.getenv('MAIL_ADDRESS_FROM'), os.getenv('MAIL_PASSWORD'))
server.sendmail(os.getenv('MAIL_ADDRESS_FROM'), os.getenv('MAIL_ADDRESS_TO'), letter)
server.quit()
