# Manga API
from bs4 import BeautifulSoup
import requests

# Finder #
Manga_Name = {'Mangakakalot' : [['ul', 'class', 'manga-info-text'], 'h1'],
              'Manganelo' : [['div', 'class', 'story-info-right'], 'h1']
             }
Image_Link = {'Mangakakalot' : [['div', 'class', 'manga-info-pic']],
              'Manganelo' : [['div', 'class', 'story-info-left']]
             }
Manga_Genres = {'Mangakakalot' : [['ul', 'class', 'manga-info-text'], ['li', 6]],
                'Manganelo' : [['div', 'class', 'story-info-right'], ['tr', 3]]
               }
Manga_Desc = {'Mangakakalot' : [['div', 'id', 'noidungm']],
              'Manganelo' : [['div', 'id', 'panel-story-info-description']]
             }
      
Hentai_Details = {'nhentai' : [['div', 'id', 'cover'], # Cover
                               ['div', 'id', 'info'], # Container
                               ['h1', 'class', 'title'], # Title
                               ['section', 'id', 'tags'], # Inside Container
                               ['div'], # Detail Sections
                               ['span', 'class', 'name'], # Details
                              ]
                  }
##########

class Hentai:
    def __init__(Self):
        Self.StartLink = 'https://nhentai.net/g/'

    # Private
    def _GetDetails(Self, N_Code) -> dict:
        # Create Dict
        _ret_details_ = {'Code':N_Code, 'Image':'None', 'Title':'None', 'Parodies':'None', 'Characters':'None', 'Tags':'None', 'Artists':'None', 'Groups':'None', 'Languages':'None', 'Categories':'None', 'Pages':'None'}
        _details_lineup_ = ['Parodies', 'Characters', 'Tags', 'Artists', 'Groups', 'Languages', 'Categories', 'Pages', 'BREAK']
        # Get Sauce
        res = requests.get(Self.StartLink + N_Code)
        H_Src = BeautifulSoup(res.content, 'html.parser')
        # Set Finder
        Finder = Hentai_Details.get('nhentai')
        # Get Image
        H_Image = H_Src.find(Finder[0][0], {Finder[0][1]:Finder[0][2]}).find('img')['data-src']
        _ret_details_['Image'] = H_Image # Store to Dictionary
        # Get Container
        H_Src = H_Src.find(Finder[1][0], {Finder[1][1]:Finder[1][2]})
        ## Get Title
        H_Title = H_Src.find(Finder[2][0], {Finder[2][1]:Finder[2][2]}).text
        _ret_details_['Title'] = H_Title # Store to Dictionary
        ## Get Inside Container
        H_Src = H_Src.find(Finder[3][0], {Finder[3][1]:Finder[3][2]})
        ### Get Details
        Store_Details = []
        Details = H_Src.find_all(Finder[4][0])
        for Index, Detail in enumerate(Details):
            # Set Detail Title
            _DetailTitle = _details_lineup_[Index]
            if _DetailTitle == 'BREAK':
                break
            # Get Details Under Each Div
            _DetailPacker = []
            _details = Detail.find_all(Finder[5][0], {Finder[5][1]:Finder[5][2]})
            for _detail in _details:
                _DetailPacker.append(_detail.text)
            # Check For Detail Packer Content
            if len(_DetailPacker) == 0:
                _DetailPacker = ['None']
            # Push To Dictionary
            _ret_details_[_DetailTitle] = _DetailPacker
        #### Return Results ####
        return _ret_details_

    # Public
    def generate_random_sauce(Self) -> dict:
        # Get Sauce
        Code = requests.head('https://nhentai.net/random/').headers["Location"]
        Code = Code[3:-1]
        # Get Sauce Details
        r_sauce_jar = Self._GetDetails(Code)
        # Return To Me As Dictionary
        return r_sauce_jar


    
