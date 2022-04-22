from rest_framework import serializers

from .models import *


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ('name',)


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ('book', 'mime_type', 'url')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('code',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'birth_year', 'death_year')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    authors = AuthorSerializer(many=True)
    languages = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    bookshelves = serializers.SerializerMethodField()
    formats = serializers.SerializerMethodField()

    lookup_field = 'gutenberg_id'

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'authors',
            'languages',
            'subjects',
            'bookshelves',
            'media_type',
            'formats',
            'download_count'
        )

    def get_bookshelves(self, obj):
        bookshelves = [bookshelf.name for bookshelf in obj.bookshelves.all()]
        bookshelves.sort()
        return bookshelves

    def get_formats(self, obj):
        return {f.mime_type: f.url for f in obj.get_formats()}

    def get_id(self, obj):
        return obj.gutenberg_id

    def get_languages(self, obj):
        languages = [language.code for language in obj.languages.all()]
        languages.sort()
        return languages

    def get_subjects(self, obj):
        subjects = [subject.name for subject in obj.subjects.all()]
        subjects.sort()
        return subjects