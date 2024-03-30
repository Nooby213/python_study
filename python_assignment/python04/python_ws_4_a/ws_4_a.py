# 아래에 코드를 작성하시오.
from utils import create_url
from conf import settings
name = settings.NAME
url = settings.MAIN_URL

result = create_url.create_url(name,url)
print(result)