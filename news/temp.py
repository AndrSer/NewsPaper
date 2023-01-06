import random
import models

models.User.objects.create_user('news_user_a')
models.User.objects.create_user('news_user_b')
models.Author.objects.create(user=models.User.objects.create_user('news_user_a'))
models.Author.objects.create(user=models.User.objects.create_user('news_user_b'))
models.Category.objects.create(name='Politics')
models.Category.objects.create(name='Sport')
models.Category.objects.create(name='Incidents')
models.Category.objects.create(name='The science')

header = 'Индийский саммит G20 пройдет без Украины'
text = 'Украине не направляли приглашение для участия ' \
       'в саммите G20, сообщил официальный представитель МИД Индии Ариндам Багчи. ' \
       'Очередная встреча "двадцатки" состоится в Нью-Дели 9-10 сентября.'
author = models.Author.objects.get(id=1)
models.Post.objects.create(header=header, text=text, author=author)
header = 'Матч с возможным дебютом Роналду за "Аль-Наср" перенесли на другой день'
text = 'Матч 12-го тура чемпионата Саудовской Аравии по футболу, ' \
       'в котором в составе клуба "Аль-Наср" мог дебютировать нападающий Криштиану Роналду, ' \
       'перенесен с четверга на пятницу из-за погодных условий.'
author = models.Author.objects.get(id=2)
kind = models.Post.kind.article
models.Post.objects.create(header=header, text=text, author=author, kind=kind)
header = 'В России более 3,2 тыс. человек заболели COVID-19 за сутки'
text = 'Суточный прирост новых заболевших коронавирусной инфекцией в РФ составил ' \
       '3 274 случая, следует из данных оперативного штаба, обнародованных в четверг.'
author = models.Author.objects.get(id=1)
kind = models.Post.kind.article
models.Post.objects.create(header=header, text=text, author=author, kind=kind)

post = models.Post.objects.get(id=1)
category = models.Category.objects.get(id=1)
models.PostCategory.objects.create(post=post, category=category)
post = models.Post.objects.get(id=1)
category = models.Category.objects.get(id=3)
models.PostCategory.objects.create(post=post, category=category)
post = models.Post.objects.get(id=2)
category = models.Category.objects.get(id=2)
models.PostCategory.objects.create(post=post, category=category)
post = models.Post.objects.get(id=2)
category = models.Category.objects.get(id=3)
models.PostCategory.objects.create(post=post, category=category)
post = models.Post.objects.get(id=3)
category = models.Category.objects.get(id=4)
models.PostCategory.objects.create(post=post, category=category)
post = models.Post.objects.get(id=3)
category = models.Category.objects.get(id=3)
models.PostCategory.objects.create(post=post, category=category)

text = 'Комментарий к новости G20'
post = models.Post.objects.get(id=1)
user = models.User.objects.get(id=1)
models.Comment.objects.create(text=text, post=post, user=user)
text = 'Комментарий к статье про Роналду'
post = models.Post.objects.get(id=2)
user = models.User.objects.get(id=2)
models.Comment.objects.create(text=text, post=post, user=user)
text = 'Комментарий к статье про COVID'
post = models.Post.objects.get(id=3)
user = models.User.objects.get(id=1)
models.Comment.objects.create(text=text, post=post, user=user)
text = 'Второй комментарий к статье про G20'
post = models.Post.objects.get(id=1)
user = models.User.objects.get(id=2)
models.Comment.objects.create(text=text, post=post, user=user)

for q in list(models.Post.objects.all()):
    for i in range(1, random.randint(1, 10)):
        q.like()
    for i in range(1, random.randint(1, 10)):
        q.dislike()


for q in list(models.Comment.objects.all()):
    for i in range(1, random.randint(1, 100)):
        q.like()
    for i in range(1, random.randint(1, 100)):
        q.dislike()

for author in list(models.Author.objects.all()):
    author.update_rating()

{models.Author.objects.select_related('user').order_by('-rating').first().user.username:
 models.Author.objects.select_related('user').order_by('-rating').first().rating }

{'date_posting': str(models.Post.objects.order_by('-rating').first().date_posting),
 'username': str(models.User.objects.filter(id=models.Post.objects.order_by('-rating').first().author.id)[0]),
 'rating': models.Post.objects.order_by('-rating').first().rating,
 'header': models.Post.objects.order_by('-rating').first().header,
 'preview': (models.Post.objects.order_by('-rating').first()).preview()
             }

for d in list(models.Comment.objects.filter(post_id=models.Post.objects.order_by('-rating').first().id).values_list('text')):
    str(d[0])








