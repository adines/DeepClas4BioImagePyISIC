from imagepy.core.engine import Free
from imagepy import IPy
from imagepy.core.util import fileio
import os
import deepclas4bio as dc4b

class Plugin(Free):
    title = 'DeepClas4BioPyISIC'
    model='ResNetISIC'
    framework='Keras'


    def run(self,para=None):
        imp=IPy.get_ips()
        if imp is None:
            IPy.alert("Please open the image you want to classify",'Error')
            return
        name=imp.title
        recent=fileio.recent
        for i in recent:
            pos1=i.rfind(os.sep)
            pos2=i.rfind('.')
            if name==i[pos1+1:pos2]:
                image=i
        className=dc4b.predict(image,self.framework,self.model)
        IPy.alert("The class which the image belongs is "+className,'Prediction')
