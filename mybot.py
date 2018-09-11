import praw, config, time

def bot_login():
	r = praw.Reddit(username = config.username,
		password = config.password, 
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = 'User Agent')
	if r:
		#print('Logic success')
		return r
	else:
		print('Login failed')

def bot_search(r, subreddit):
	for comment in r.subreddit(subreddit).comments(limit=1000):
		if ('test' in comment.body) and not (comment.id in comments_replied_to) and (comment.author != r.user.me()):
			comment.reply("[Nice Test](https://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif)")
			comments_replied_to.append(comment.id)
			with open('comments_replied_to.txt', 'a') as f:
				f.write(comment.id)
				f.write('\n')
				#print("Replied to: " + comment.id)
	# time.sleep(30)

def read_in_comments():
	with open('comments_replied_to.txt' ,'r') as f:
		comments_replied_to = f.read()
		comments_replied_to = comments_replied_to.split('\n')
	return comments_replied_to;

r = bot_login()
comments_replied_to = read_in_comments();

if __name__ == '__main__':
	#print('Bot Searching ...')
	bot_search(r, 'test')
