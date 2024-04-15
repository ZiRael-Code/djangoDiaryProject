class JsonResponse:
    def __init__(self, data,  ids, diary):
        self.diary = diary
        self.data = data
        self.ids = ids

    def get_jsonResponse(self):
        diary_data = {
            'id': self.ids,
            'username': self.diary.username,
            'data': self.data,
        }
        return diary_data
