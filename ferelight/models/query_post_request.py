from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from ferelight.models.base_model import Model
from ferelight import util


class QueryPostRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, database=None, similaritytext=None, ocrtext=None, limit=None):  # noqa: E501
        """QueryPostRequest - a model defined in OpenAPI

        :param database: The database of this QueryPostRequest.  # noqa: E501
        :type database: str
        :param similaritytext: The similaritytext of this QueryPostRequest.  # noqa: E501
        :type similaritytext: str
        :param ocrtext: The ocrtext of this QueryPostRequest.  # noqa: E501
        :type ocrtext: str
        :param limit: The limit of this QueryPostRequest.  # noqa: E501
        :type limit: int
        """
        self.openapi_types = {
            'database': str,
            'similaritytext': str,
            'ocrtext': str,
            'limit': int
        }

        self.attribute_map = {
            'database': 'database',
            'similaritytext': 'similaritytext',
            'ocrtext': 'ocrtext',
            'limit': 'limit'
        }

        self._database = database
        self._similaritytext = similaritytext
        self._ocrtext = ocrtext
        self._limit = limit

    @classmethod
    def from_dict(cls, dikt) -> 'QueryPostRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _query_post_request of this QueryPostRequest.  # noqa: E501
        :rtype: QueryPostRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def database(self) -> str:
        """Gets the database of this QueryPostRequest.

        The name of the database to query.  # noqa: E501

        :return: The database of this QueryPostRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database: str):
        """Sets the database of this QueryPostRequest.

        The name of the database to query.  # noqa: E501

        :param database: The database of this QueryPostRequest.
        :type database: str
        """

        self._database = database

    @property
    def similaritytext(self) -> str:
        """Gets the similaritytext of this QueryPostRequest.

        The similarity text.  # noqa: E501

        :return: The similaritytext of this QueryPostRequest.
        :rtype: str
        """
        return self._similaritytext

    @similaritytext.setter
    def similaritytext(self, similaritytext: str):
        """Sets the similaritytext of this QueryPostRequest.

        The similarity text.  # noqa: E501

        :param similaritytext: The similaritytext of this QueryPostRequest.
        :type similaritytext: str
        """

        self._similaritytext = similaritytext

    @property
    def ocrtext(self) -> str:
        """Gets the ocrtext of this QueryPostRequest.

        The OCR text.  # noqa: E501

        :return: The ocrtext of this QueryPostRequest.
        :rtype: str
        """
        return self._ocrtext

    @ocrtext.setter
    def ocrtext(self, ocrtext: str):
        """Sets the ocrtext of this QueryPostRequest.

        The OCR text.  # noqa: E501

        :param ocrtext: The ocrtext of this QueryPostRequest.
        :type ocrtext: str
        """

        self._ocrtext = ocrtext

    @property
    def limit(self) -> int:
        """Gets the limit of this QueryPostRequest.

        The maximum number of results to return.  # noqa: E501

        :return: The limit of this QueryPostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        """Sets the limit of this QueryPostRequest.

        The maximum number of results to return.  # noqa: E501

        :param limit: The limit of this QueryPostRequest.
        :type limit: int
        """

        self._limit = limit
