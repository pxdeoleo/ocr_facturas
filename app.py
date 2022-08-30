import re
from PIL import Image
import pytesseract
import numpy as np

class Receipt():
    def __init__ (self, dir):
        self.dir = dir
        self.text = self.parse_receipt()

    def get_rnc(self):

        dirty_rnc = self.text.split('RNC:')[1][:15]

        # remove all non-numeric characters
        clean_rnc = re.sub(r'\D', '', dirty_rnc)
        return clean_rnc

    def get_date(self):
        """
        It uses a regular expression to find the first date in the text
        :return: The first date in the text.
        """
        # use regex to find the first date in the text
        return re.findall(r'\d{2}/\d{2}/\d{4}', self.text)[0]
        
    def get_ncf(self):
        """
        We split the text at the first instance of 'NCF' and then take the next 12 characters. We then
        use regex to find the NCF
        :return: The NCF
        """
        # Finding the first 'NCF' in the text
        # and then getting the next 12 characters

        # Using regex to get the NCF
        regex_res = re.search(r'B(\d){10}', self.text)
        return regex_res.group(0)

    def as_dict(self):
        return self.fields

    def parse_receipt(self):
        # TODO: IMPROVE PARSING ACCURACY
        img = np.array(Image.open(self.dir))
        text = pytesseract.image_to_string(img)
        return text
