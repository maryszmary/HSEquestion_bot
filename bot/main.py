import telebot
import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


token = '401772666:AAHcnkge02VRChq5pyrWn1_IQynNA9ACq_M'
bot = telebot.TeleBot(token)

with open('../data.txt') as f:
	data = f.read().split('--*--')
df = pd.DataFrame({"ans": data})
tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word')
tfidf = tfidf.fit(df.ans)


def my_logger(q, ans):
	with open('log.txt', 'a') as f:
		f.write(q + ';' + ans + '\n')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я — бот-почемучник для ВШЭ. Отвечу на твои вопросы про вышку!")


@bot.message_handler(content_types=['text'])
def answer(message):
	ans = tfidf_chooser(message.text)
	my_logger(message.text, ans)
	bot.send_message(message.chat.id, ans)


def tfidf_chooser(msg):
	q = tfidf.transform([msg])
	candidates = []
	for i in df.index:
		cur = tfidf.transform([df.ans.iloc[i]])
		sim = cosine_similarity(cur, q)[0][0]
		candidates.append((sim, i))
	best_cand = max(candidates, key=lambda x: x[0])
	return df.ans.iloc[best_cand[1]]


bot.polling(none_stop=False)
