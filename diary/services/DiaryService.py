from diary.dtos.request import Create_Diary_Request
from diary.dtos.response.JsonResponse import JsonResponse
from diary.models import *


class DiaryService:

    def __init__(self):
        pass

    def createDiary(self, createDiaryRequest: Create_Diary_Request):
        # if self.findDiary(createDiaryRequest.get_username()) is not None:
        #     raise Exception("Username already exists")
        if (createDiaryRequest.get_password() and
                createDiaryRequest.get_password() is not None):
            diary =  Diary.objects.create(username=createDiaryRequest.get_username(),
                                         password=createDiaryRequest.get_password())
            response = JsonResponse("", diary.id, diary).get_jsonResponse()
            return response
        else:
            raise Exception("Password or username must be provided")

    def unlockDiary(self, username, password):
        diary = self.findDiary(username)
        if diary.password == password:
            diary.isLocked = False
            diary.save()
            return diary
        else:
            raise Exception("Username or password is incorrect")

    def lockDiary(self, username):
        diary = self.findDiary(username)
        diary.isLocked = True
        diary.save()

    def createEntry(self, username, title, body):
        diary = self.findDiary(username)
        entry = Entry.objects.create(title=title, body=body)
        diary.entries.add(entry)

    def deleteEntry(self, username, dateCreated, title):
        diary = self.findDiary(username)
        entry = self.findEntry(username, dateCreated, title)
        entry.delete()
        diary.entries.remove(entry)
        diary.save()
        pass

    def findEntry(self, username, dateCreated, title):
        findEntry = self.findDiary(username).entries
        entry = Entry.objects.filter(title=title, dateCreated=dateCreated).first()
        if entry is not None:
            return findEntry[entry]
        else:
            raise Exception("Entry with title or date is not found")

    def findAllEntry(self, username):
        entries = self.findDiary(username).entries
        return entries

    def findEntryByDate(self, username, dateCreated):
        entry = self.findAllEntry(username).__contains__(dateCreated)
        return entry

    def updateEntry(self, username, title, body):
        diary = self.findDiary(username)
        diary.title = title
        diary.body = body
        diary.save()
        return diary

    def findDiary(self, username):
        diary = Diary.objects.get(username=username)
        if diary is not None:
            return diary
        else:
            raise Exception("Diary does not exist")
