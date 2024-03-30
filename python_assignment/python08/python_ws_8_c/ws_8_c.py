class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self):
        # self.data_type = data_type 
        # self.title = title 
        # self.content = content 
        # self.created_at = created_at 
        # self.updated_at = updated_at
        BaseModel.PK += 1
        self.PK = BaseModel.PK
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self):
        super().__init__()
    
class Other(BaseModel):
    TYPE = 'Other Model'
    
    def __init__(self):
        super().__init__()

    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Novel, Other):
    print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
    Extended_Type = 'Extended Type'
    def __init__(self):
        super().__init__()

    def display_info(self):
        print(f'PK: {self.PK}, Type: {self.TYPE}, Extended Type: {self.Extended_Type}')
              
    def save(self):
        print('데이터를 확장해서 저장합니다.')

    
extended_instance = ExtendedModel()
extended_instance.display_info()
extended_instance.save()