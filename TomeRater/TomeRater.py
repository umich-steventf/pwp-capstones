class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
		
	def __eq__(self, other_user):
        if self.name == other_user and self.email == other_user:
            return True
        else:
            return False
	
	def __repr__(self):
        print("User: {user}, email: {email}, book(s) read: {num_books_read}".format(user=self.name, email=self.email, num_books_read=len(self.books)))
		
    def get_email(self):
        return self.email

    def change_email(self, address):
        if ".edu" not in address or ".gov" not in address or ".com" not in address or "@" not in address:
			print("Most likely not valid email address. Please try again. If issue continues, please contact support @ help@books.rating.com")
		print("Changing email address from old old address ({old_email_address}) to {new_email_address}".format(old_email_address=self.email,new_email_address=address))
		self.email = address
    
    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
		holder = 0
		rating = 0
		for books in self.books.keys():
			holder +=1
			if self.books[books] is not None:
				rating += self.books[books]
		book_average_rating = rating/holder
		return book_average_rating

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
		
    def __eq__(self, other):
        if self.title == other and self.isbn == other:
            return True
        else:
            return False
			
	def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title} with ISBN {isbn}".format(title=self.title, isbn=self.isbn)

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, updated_isbn):
		print("Changing ISBN from {old_num} to {new_num}".format(old_num=self.isbn, new_num=update_isbn))

    def add_raiting(self, raiting):
		if raiting >= 0 and raiting <=4:
			self.raiting.append(raiting)
		else:
			print("Invalid raiting!!! Raitings must be between 0 and 4.")

    def get_average_rating(self):
        combined_ratings = 0
        for raiting in self.ratings:
            combined_rating += raiting
        if len(self.ratings) == 0 or combined_rating == 0:
            avg_conbined_rating = 0
        else:
            avg_conbined_rating = combined_rating/len(self.ratings)
        return avg_conbined_rating

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)
		
	def get_author(self):
		return self.author

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
		
	def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    
class TomeRater(object):

	def __init__(self):
		self.users = {}
		self.books = {}
		
	def __eq__(seld, other):
		if self.users == other and self.books == other:
			return True
		else:
			return False
			
	def __repr__(self):
		return "Users: {users} have read these books: {books}".format(users=self.users, books=self.books)

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        novel = Fiction(title, author, isbn)
        return novel

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            self.users[email].read_book(book,rating)
            if rating is not None:
                book.add_rating(rating)
            if book is not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if user_books is not None:
            for books in user_books:
                self.add_book_to_user(books, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.keys():
            print(user)

    def most_read_book(self):
        highest_count_name = ""
        highest_read_book_count = 0

        for book in self.books.keys():
            if self.books[book].get() > highest_read_book_count:
                highest_count_name = book.title
                highest_read_book_count = self.books[book].get()
        print("The most read book: {name}, with a count of {count} reads.".format(name=highest_count_name, count=highest_read_book_count))

	def highest_rated_book(self):
		highest_rated_book = ""
		average_rating = 0
		for book in self.books.keys():
			if book.get_average_rating() > average_rating:
				average_rating = book.get_average_rating()
				highest_rated_book = book.title
		print("Highest raite book: {name}, raiting of: {rating}".format(name=highest_rated_book, rating=average_rating))
	
	def most_positive_user_user(self):
		average_rating = 0
		most_positive_user = ""
		for user in self.users.values():
            average_rating = user.get_average_rating()
            if  average_rating > average_rating:
				average_rating = average_rating
				most_positive_user = user.name
		print("Most positive user is {name} with average rating of {rating}".format(name=most_positive_user, rating=average_rating))
		
	def get_most_read_book(self):
		read_count = 0
		most_read_book = ""
		for book in self.books.keys():
			if self.books[book] > read_count:
				read_count = self.book[book]
				most_read_book = book.title
				
	def get_n_most_read_books(self, n)
		if type(n) == int:
			books_read_sorted = [book for book in sorted(self.books, key=self.books.get, reverse=True)]
			return books_read_sorted[:n]
		else:
			return "{n_input} is not an int number, please enter an int".format(n=n_input)
			
	#def get_n_most_prolific_readers(self, n):
	#	if type(n) == int:
	#		users = 