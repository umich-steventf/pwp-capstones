    def get_most_read_book(self):
		read_count = 0
		most_read_book = ""
		for book in self.books.keys():
			if self.books[book] > read_count:
				read_count = self.books[book]
				most_read_book = book.title
		print("Most read book: {name}".format(name=most_read_book))
		
	def get_n_most_read_books(self, n)
		if type(n) == int:
			books_read_sorted = [book for book in sorted(self.books, key=self.books.get, reverse=True)]
			return books_read_sorted[:n]
		else:
			return "{n_input} is not an int number, please enter an int".format(n=n_input)
			
	def get_n_most_prolific_readers(self, n):
		if type(n) == int:
			go_getter_readers = [users in users in sorted(self.users, keys=self.users.get)]