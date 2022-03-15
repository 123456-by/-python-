from aip import AipOcr

class BaiduOcr:
    def __init__(self,file_path):
        '''初始化，传入图片地址'''
        self.file_path = file_path
        '''你的APPID AK SK'''
        APP_ID = '25703523'
        API_KEY = 'ULSbbzwt4khfGAM0zA886WOI'
        SECRET_KEY = 'UfPISnE3mkA2yMBagXzjxMuT99GPZw7N '
        self.client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

    '''读取图片'''
    def get_file_content(self):
        with open(self.file_path,'rb') as fp:
            return fp.read()

    def handel_data(self,data):
        '''提取结果'''
        data = '\n'.join([i['words'] for i in data['words_result']])
        return data

    def run(self):
        '''运行'''
        image = self.get_file_content()
        '''调用通用文字识别，图片参数为本地图片'''
        result = self.client.basicGeneral(image)
        result = self.handel_data(result)
        print(result)
        return result

if __name__=='__main__':
    ocr = BaiduOcr('1.jpg')
    ocr.run()

