from config.config import get_kakao_secret
from typing import Dict,Union,List
import os
import sys
import requests as rq

class KakaoAPI:
    def __init__(self,query:str) -> None:
        # Secret Key
        self._REST_API_KEY : str = get_kakao_secret(key='REST_API')

        # API URL
        self.api_url : str = 'https://dapi.kakao.com/v2/search/image'

        # Query
        self.query : str = query
    
    def main(self)-> None:
        # Headers
        headers: Dict[str,str] = {
            'Host': 'dapi.kakao.com','Authorization': f'KakaoAK {self._REST_API_KEY}'
            }

        # Query Data
        datas : List[Dict[str,Union[str,int]]] = [
            {
                'query': self.query,
                'page' : page,
                'size' : 50
            }
        for page in range(1,2)]
        
        with rq.Session() as session:
            items : List[Dict[str,str]] = [self.fetch(data=data,session=session,headers=headers) for data in datas]

        # 이미지 다운로드 
        with rq.Session() as session:
            self.download_image(items=items,session=session)

    def fetch(self,data:Dict[str,Union[str,int]],session,headers:Dict[str,str])-> Dict[str,str]:
        with session.get(url=self.api_url,data=data,headers=headers) as response:
            if response.ok:
                # Get Documents
                documents : List[Dict[str,Union[str,int]]] =  response.json()['documents']
                
                # image link Return
                return {f'image_link_{idx}':document['image_url'] for idx,document in enumerate(documents,1)}                
            else: 
                print(f'Failed\n{response}')
                sys.exit()
        
    def download_image(self,items,session)-> None:
        # 폴더 지정
        self.create_folder(folder_name=self.query)

        # Image URL Keys
        for item in items:
            for key in item.keys():
                img_link : str = item[key]
                
                # 다운로드 파일명 재지정
                new_file : str = self.create_file_name(img_link=img_link)

                # 다운로드
                try:
                    with session.get(url=img_link) as response:
                        if response.ok:
                            with open(os.path.join(self.query,new_file),'wb') as fp:
                                fp.write(response.content)
                                print(f'{new_file} - 저장완료!\n')
                except:
                    print(f'{new_file} - 저장실패!')
                    
    def create_file_name(self,img_link:str)-> str:
        exts : List[str] = ['.jpg','.webp','.png','.jpeg']
        new_file : str = img_link.split('/')[-1].split('%')[-1]

        file,ext = os.path.splitext(new_file)
        if ext not in exts:
            new_file = new_file + '.jpg'
        return new_file
    
    def create_folder(self,folder_name:str):
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)