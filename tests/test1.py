import requests
import allure
base_address = "https://ontaxi.com.ua"

@allure.story("This story")
@allure.step("step1")
def get(path="/", params=None, headers=None):
    url = f"{base_address}{path}"
    return requests.get(url=url, params=params, headers=headers)



print(get(path="/ru/clients/kyiv").status_code)
# sd