
class book:
    def __init__(self, book_name, book_author, book_year, book_description, book_picture):
        name = book_name
        author = book_author
        year = book_year
        description = book_description
        picture = book_picture

class user:
    def __init__(self, user_login, user_password, user_email, user_surname, user_name, user_patronymic, user_address, user_phone_number, user_avatar):
        login = user_login
        password = user_password
        email = user_email
        surname = user_surname
        name = user_name
        patronymic = user_patronymic
        address = user_address
        phone_number = user_phone_number
        avatar = user_avatar

        pass

class order:
    def __init__(self, order_book_id, order_user_id):
        book_id = order_book_id
        user_id = order_user_id