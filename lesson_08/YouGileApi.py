import requests
class YouGileApi:

    def __init__(self, url):
        self.url = url

# создание и получение id компании
    def id_company(self, login='', password=''):
        creds = {
            "login": login,
            "password": password,
        }
        my_headers = {
            "Content-Type": "application/json"
        }
        company_id = requests.post(self.url + '/api-v2/auth/companies', json=creds, 
                             headers=my_headers)
        return company_id.json()['id']
        
# получене ключа
    def key(self, login='', password='', companyId=""):
        creds = {
            "login": login,
            "password": password,
            "companyId": companyId
        }
        my_headers = {
            "Content-Type": "application/json"
        }
        key = requests.post(self.url + '/api-v2/auth/keys', json=creds, 
                             headers=my_headers)
        return key.json()['key']
    
# получение списка проектов
    def list_project(self):
        my_headers = {
            "Authorization" : "",
            "Content-Type" : "application/json"
            }
        list = requests.get(self.url + '/api-v2/projects', headers=my_headers)
        return list.json()
    
# создание проекта
    def create_project(self, title):
        project = {
            "title": title,
            "users": {"b8700597-d8c5-4a40-8021-a08b763a19e5": "admin"}
        }
        my_headers = {
            "Authorization" : "",
            "Content-Type" : "application/json"
            }
        project = requests.post(self.url + '/api-v2/projects', json=project, 
                             headers=my_headers)
        return project.json()
    
    # изменение названия проекта
    def edit_progect(self, new_id_progect, new_title):
        my_headers = {
            "Authorization" : "",
            "Content-Type" : "application/json"
            }
        progect = {
            "title": new_title,
            "users": {"b8700597-d8c5-4a40-8021-a08b763a19e5": "admin"}
        }
        resp = requests.put(self.url + '/api-v2/projects/' + str(new_id_progect), headers=my_headers, json=progect)
        return resp.json()
    
    # получить проект по ID 
    def search_by_id_progect(self, new_id_progect):
        my_headers = {
            "Authorization" : "",
            "Content-Type" : "application/json"
            }
        resp = requests.get(self.url + '/api-v2/projects/' + str(new_id_progect), headers=my_headers)
        return resp.json()
    
    def list_project_negativ(self):
        my_headers = {
            "Authorization" : "",
            "Content-Type" : "application/json"
            }
        list = requests.get(self.url + '/api-v2', headers=my_headers)
        return list.json()




