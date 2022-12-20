from django.shortcuts import get_object_or_404
from rest_framework import generics
from core.exceptions.common import CleanHtmlException
from core.models import WebSiteEssentials
from core.utils import text as text_utils
from core.serializers import WebsiteSerializer, WebHtmlRetrieveSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class WebsiteEssentialCreateView(generics.CreateAPIView):
    """
    A Create API: it should take a name(website name) as POST API input,
    along with HTML encoded content. The website name should always be unique.
    """

    serializer_class = WebsiteSerializer

    def create(self, request, *args, **kwargs):
        serializer: WebsiteSerializer = WebsiteSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # clean html content
                clean_html_data = text_utils.clean_html(serializer.validated_data["html_content"])
                serializer.validated_data["clean_html_content"] = clean_html_data

                # calculate word corpus
                serializer.validated_data['clean_corpus_words'] = \
                    text_utils.count_words_occurrences(clean_html_data)

            except CleanHtmlException as e:
                return Response({"message": str(e)},
                                status=e.status_code)
            finally:
                serializer.save()
            return Response({"message": "data has been added successfully.."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebHtmlRetrieveView(generics.RetrieveAPIView):
    """
    return html content if a valid website name is given as input by user.
    This api view for getting html content of website
    """
    lookup_field = 'website_name'
    queryset = WebSiteEssentials.objects.all()
    serializer_class = WebHtmlRetrieveSerializer


class TopWordsRetrieveView(generics.RetrieveAPIView):
    """
    return top n common words if a valid website name is given as input by user.
    This api view for getting n common words of website
    """
    lookup_field = 'website_name'
    queryset = WebSiteEssentials.objects.all()
    serializer_class = WebHtmlRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        page_obj = get_object_or_404(WebSiteEssentials,
                                     website_name=kwargs[self.lookup_field])
        top_words: list = list(page_obj.clean_corpus_words.keys())

        n: int = kwargs['n']  # number of words
        data: list = top_words if len(top_words) <= n else top_words[:n]

        return Response({"top_n_words": str(data)}, status=status.HTTP_200_OK)


""" App pre-stored top common words before so 
    if you will add more html content it will take less time.
"""


class WebPageDeleteView(generics.DestroyAPIView):
    """
    return html content if a valid website name is given as input by user.
    This api view for getting html content of website
    """
    lookup_field = 'website_name'
    queryset = WebSiteEssentials.objects.all()


class WebPageUpdateView(generics.UpdateAPIView):
    """
    return html content if a valid website name is given as input by user.
    This api view for getting html content of website
    """
    lookup_field = 'website_name'
    queryset = WebSiteEssentials.objects.all()
    serializer_class = WebHtmlRetrieveSerializer

    def put(self, request, *args, **kwargs):
        return Response({"message": "Not Implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)

    def patch(self, request, *args, **kwargs):
        return Response({"message": "Not Implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)
