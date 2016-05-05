# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class AuthToken(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuthToken - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'str',
            'extra_info': 'ExtraInfo',
            'id': 'int',
            'owner': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'extra_info': 'extraInfo',
            'id': 'id',
            'owner': 'owner',
            'status': 'status'
        }

        self._code = None
        self._extra_info = None
        self._id = None
        self._owner = None
        self._status = None

    @property
    def code(self):
        """
        Gets the code of this AuthToken.


        :return: The code of this AuthToken.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this AuthToken.


        :param code: The code of this AuthToken.
        :type: str
        """
        self._code = code

    @property
    def extra_info(self):
        """
        Gets the extra_info of this AuthToken.


        :return: The extra_info of this AuthToken.
        :rtype: ExtraInfo
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """
        Sets the extra_info of this AuthToken.


        :param extra_info: The extra_info of this AuthToken.
        :type: ExtraInfo
        """
        self._extra_info = extra_info

    @property
    def id(self):
        """
        Gets the id of this AuthToken.


        :return: The id of this AuthToken.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuthToken.


        :param id: The id of this AuthToken.
        :type: int
        """
        self._id = id

    @property
    def owner(self):
        """
        Gets the owner of this AuthToken.


        :return: The owner of this AuthToken.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this AuthToken.


        :param owner: The owner of this AuthToken.
        :type: str
        """
        self._owner = owner

    @property
    def status(self):
        """
        Gets the status of this AuthToken.


        :return: The status of this AuthToken.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AuthToken.


        :param status: The status of this AuthToken.
        :type: str
        """
        allowed_values = ["ACTIVE", "REVOKED", "DELETED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

