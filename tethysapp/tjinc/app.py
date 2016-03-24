from tethys_sdk.base import TethysAppBase, url_map_maker


class TjInc(TethysAppBase):
    """
    Tethys app class for TJ Inc.
    """

    name = 'TJ Inc'
    index = 'tjinc:home'
    icon = 'tjinc/images/icon.gif'
    package = 'tjinc'
    root_url = 'tjinc'
    color = '#2ecc71'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='tjinc',
                           controller='tjinc.controllers.home'),
        )

        return url_maps