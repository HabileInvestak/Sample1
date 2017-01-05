from django.http import request
from restapp.ExcelSheet import *


'''ApiHomeDict={}
class LoadDict():
    e = ExcelSheetAll()
    ApiHomeDict = e.apiHomeDict()
    print ApiHomeDict
class ReturnApi:
    def returnDict(self):
        return ApiHomeDict'''
'''if "ApiDictionary" in request.session:
    print 'Dictioanry is already stored in session'
else:
    e=ExcelSheetAll()
    ApiHomeDict=e.apiHomeDict()
    request.session['ApiDictionary'] = ApiHomeDict
    #print ApiHomeDict
print request.session['ApiDictionary']'''

