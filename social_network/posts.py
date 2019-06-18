from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.user = None
        self.text = text
        self.timestamp = timestamp
        
        
    def set_user(self, user):
        self.user = user


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        return '@{fn} {ln}: "{text}"\n\t{timestamp}'.format(fn = self.user.first_name, ln = self.user.last_name, text = self.text, timestamp = self.timestamp.strftime("%A, %b %d, %Y"))

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{fn} {ln}: "{text}"\n\t{image_url}\n\t{timestamp}'.format(fn = self.user.first_name, ln = self.user.last_name, text = self.text, image_url = self.image_url, timestamp = self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{fn} Checked In: "{text}"\n\t{lat}, {long}\n\t{timestamp}'.format(fn=self.user.first_name,text=self.text,lat=self.latitude,long=self.longitude,timestamp=self.timestamp.strftime("%A, %b %d, %Y"))
