class User:
    def __init__(self, name, email, image, password):
        self.name = name
        self.email = email
        self.image = image
        self.password = password

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_image(self, image):
        self.image = image

    def get_image(self):
        return self.image

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

