from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.get_category(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.get_topic(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id: int):
        self.categories.remove(self.get_category(category_id))

    def delete_topic(self, topic_id: int):
        self.topics.remove(self.get_topic(topic_id))

    def delete_document(self, document_id: int):
        self.documents.remove(self.get_document(document_id))

    def get_category(self, category_id: int):
        return next(filter(lambda c: c.id == category_id, self.categories))

    def get_topic(self, topic_id: int):
        return next(filter(lambda t: t.id == topic_id, self.topics))

    def get_document(self, document_id: int):
        return next(filter(lambda d: d.id == document_id, self.documents))

    def __repr__(self):
        result = "\n".join([str(d) for d in self.documents])
        return result


# https://judge.softuni.org/Contests/Compete/Index/2431#2

# 3.	Document Management
# Create the following project structure
#
# Class Topic
# The Topic class should receive the following parameters upon initialization: id: int, topic: str, storage_folder: str. It should have two methods:
# •	edit(new_topic: str, new_storage_folder: str) - change the topic and the storage folder
# •	__repr__() - returns a string representation of the topic in the format: "Topic {id}: {topic} in {storage_folder}"
# Class Category
# The Category class should receive the following parameters upon initialization: id: int, name: str. The class should have two methods:
# •	edit(new_name: str) - edit the name of the category
# •	__repr__() - returns a string representation of the category in the following format: "Category {id}: {name}"
# Class Document
# The Document class should receive the following parameters upon initialization: id: int, category_id: int, topic_id: int, file_name: str. The class should also have one more attribute called tags (empty list). The class should also have 4 methods:
# •	from_instances(id: int, category: Category, topic: Topic, file_name: str) - create a new instance using the provided category and topic instances
# •	add_tag(tag_content: str) - if the tag is not already in the tags list, add it to the tags list
# •	remove_tag(tag_content:str) - if the tag is in the tags list, delete it
# •	edit(file_name: str) - change the file name with the given one
# •	__repr__() - returns a string representation of a document in the format: "Document {id}: {file_name}; category {category_id}, topic {topic_id}, tags: {tags joined by comma and space)}"
# Class Storage
# Upon initialization the class Storage will not receive any parameters. It should have 3 instance attributes: categories (empty list), topics (empty list), documents (empty list). The class should have the following methods:
# •	add_category(category:Category) - add the category if it is not in the list
# •	add_topic(topic:Topic) - add the topic if it does not exist
# •	add_document(document:Document) - add the document if it does not exist
# •	edit_category(category_id: int, new_name:str) - edit the name of the category with the provided id
# •	edit_topic(topic_id: int, new_topic: str, new_storage_folder: str) - edit the topic with the given id
# •	edit_document(document_id: int, new_file_name: str) - edit the document with the given id
# •	delete_category(category_id) - delete the category with the provided id
# •	delete_topic(topic_id) - delete the topic with the provided id
# •	delete_document(document_id) - delete the document with the provided id
# •	get_document(document_id) - return the document with the provided id
# •	__repr__() - returns a string representation of each document on separate lines
# Examples
# Test Code
# from project.category import Category
# from project.document import Document
# from project.storage import Storage
# from project.topic import Topic
#
# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
# Output
# Category 1: work
# Topic 1: daily tasks in C:\work_documents
# Document 1: finilize project; category 1, topic 1, tags: urgent, work
# Document 1: finilize project; category 1, topic 1, tags: urgent, work
