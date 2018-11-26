import praw, config, time, random, reply_log, gif_links

def bot_login():
	try:
		r = praw.Reddit(
			username = config.username,
			password = config.password, 
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = 'User Agent')
		if r:
			return r
		else:
			raise Exception
	except Exception as e:
		print(f'Login failed error: {e}')

def random_gif():
	return random.choice(gif_links.gifs)

def bot_search(r, subreddit, comments_replied_to, verbose=False):
	for comment in r.subreddit(subreddit).comments(limit=1000):
		if ('test' in comment.body or 'testing' in comment.body) and not (comment.id in comments_replied_to) and (comment.author != r.user.me()):
			comment.reply(f'[Nice Test!]({random_gif()})')
			comments_replied_to.append(comment.id)
			if verbose:
				print(f'Replied to comment id: {comment.id}')
	return comments_replied_to

def write_comments_to_file(comments_replied_to):
	with open('reply_log.py', 'w') as f:
		f.write(f'comments_replied_to = {comments_replied_to}')

if __name__ == '__main__':
	
	r = bot_login()
	comments_replied_to = reply_log.comments_replied_to

	try:
		while True:
			comments_replied_to = bot_search(r, 'test', comments_replied_to, verbose=True)
			time.sleep(60)
	except Exception as e:
		print(f'Bot paused, exception: {e}')
		print('Writing comments to file ... ', end='')
		write_comments_to_file(comments_replied_to)
		print('OK')