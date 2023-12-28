from iface.Analyser import Analyser
class M3U8Analyser(Analyser):
    def __init__(self, content, website):
        super().__init__(content, website)

    def find_video_src(self):
        pass

