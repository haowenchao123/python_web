import tornado.web

class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("login.html", next=self.get_argument("next", "/"))

	def post(self):
		username = self.get_argument("username", "")
		password = self.get_argument("password", "")
		auth = self.db.authenticate(username, password)
		if auth:
			self.set_current_user(username)
			self.redirect(self.get_argument("next", "/"))
		else:
			error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect.")
			self.redirect(u"/login" + error_msg)