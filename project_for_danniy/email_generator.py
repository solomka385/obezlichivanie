from transliterate import translit
from random import sample
domain_lst = ['@yandex.ru', '@gmail.com', '@mail.ru', '@yahoo.com']

def email_gen(fio):
    fio = fio.replace(' ', '')
    fio_en = translit(fio, 'ru', reversed=True)
    email = fio_en + ''.join(sample(domain_lst, 1))
    return email.upper()

