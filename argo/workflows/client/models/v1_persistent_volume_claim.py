# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: master
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1PersistentVolumeClaim(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'metadata': 'V1ObjectMeta',
        'spec': 'V1PersistentVolumeClaimSpec',
        'status': 'V1PersistentVolumeClaimStatus'
    }

    attribute_map = {
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, metadata=None, spec=None, status=None):  # noqa: E501
        """V1PersistentVolumeClaim - a model defined in Swagger"""  # noqa: E501

        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def metadata(self):
        """Gets the metadata of this V1PersistentVolumeClaim.  # noqa: E501


        :return: The metadata of this V1PersistentVolumeClaim.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1PersistentVolumeClaim.


        :param metadata: The metadata of this V1PersistentVolumeClaim.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this V1PersistentVolumeClaim.  # noqa: E501


        :return: The spec of this V1PersistentVolumeClaim.  # noqa: E501
        :rtype: V1PersistentVolumeClaimSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this V1PersistentVolumeClaim.


        :param spec: The spec of this V1PersistentVolumeClaim.  # noqa: E501
        :type: V1PersistentVolumeClaimSpec
        """

        self._spec = spec

    @property
    def status(self):
        """Gets the status of this V1PersistentVolumeClaim.  # noqa: E501


        :return: The status of this V1PersistentVolumeClaim.  # noqa: E501
        :rtype: V1PersistentVolumeClaimStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1PersistentVolumeClaim.


        :param status: The status of this V1PersistentVolumeClaim.  # noqa: E501
        :type: V1PersistentVolumeClaimStatus
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(V1PersistentVolumeClaim, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1PersistentVolumeClaim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other