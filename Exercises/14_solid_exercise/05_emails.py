from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTMLContent(IContent):
    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class ISender(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MySender(IContent):
    def format(self):
        return ''.join(["I'm ", self.text])


class IReceiver(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyReceiver(IContent):
    def format(self):
        return ''.join(["I'm ", self.text])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        # self.content_type = content_type = None <-- Content type is now selected with a class, so this is not needed anymore
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.format()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


# email = Email('IM', 'MyML') # 'MyML' should be removed with updated code
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

# email = Email('IM', 'MyML') # 'MyML' should be removed with updated code
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

"""New Classes Included Below"""

email = Email('IM')
sender = MySender('qmal')
receiver = MyReceiver('james')
# content = MyContent('Hello, there!') # Switch between Content types (MyML or HTML)
content = HTMLContent('Hello, there!')
email.set_sender(sender)
email.set_receiver(receiver)
email.set_content(content)
print(email)


# _____________________________ BEFORE CODE _____________________________
# from abc import ABCMeta, abstractmethod
#
# class IEmail(object):
#     __metaclass__ = ABCMeta
#
#     @abstractmethod
#     def set_sender(self, sender):
#         pass
#
#     @abstractmethod
#     def set_receiver(self, receiver):
#         pass
#
#     @abstractmethod
#     def set_content(self, content):
#         pass
#
# class Email(IEmail):
#
#     def __init__(self, protocol, content_type):
#         self.protocol = protocol
#         self.content_type = content_type
#         self.__sender = None
#         self.__receiver = None
#         self.__content = None
#
#     def set_sender(self, sender):
#         if self.protocol == 'IM':
#             self.__sender = ''.join(["I'm ", sender])
#         else:
#             self.__sender = sender
#
#     def set_receiver(self, receiver):
#         if self.protocol == 'IM':
#             self.__receiver = ''.join(["I'm ", receiver])
#         else:
#             self.__receiver = receiver
#
#     def set_content(self, content):
#         if self.content_type == 'MyML':
#             self.__content = '\n'.join(['<myML>', content, '</myML>'])
#         else:
#             self.__content = content
#
#     def __repr__(self):
#
#         template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
#
#         return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)
#
#
# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)
