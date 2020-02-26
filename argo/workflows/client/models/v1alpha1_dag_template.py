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


class V1alpha1DAGTemplate(object):
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
        'fail_fast': 'bool',
        'target': 'str',
        'tasks': 'list[V1alpha1DAGTask]'
    }

    attribute_map = {
        'fail_fast': 'failFast',
        'target': 'target',
        'tasks': 'tasks'
    }

    def __init__(self, fail_fast=None, target=None, tasks=None):  # noqa: E501
        """V1alpha1DAGTemplate - a model defined in Swagger"""  # noqa: E501

        self._fail_fast = None
        self._target = None
        self._tasks = None
        self.discriminator = None

        if fail_fast is not None:
            self.fail_fast = fail_fast
        if target is not None:
            self.target = target
        if tasks is not None:
            self.tasks = tasks

    @property
    def fail_fast(self):
        """Gets the fail_fast of this V1alpha1DAGTemplate.  # noqa: E501


        :return: The fail_fast of this V1alpha1DAGTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._fail_fast

    @fail_fast.setter
    def fail_fast(self, fail_fast):
        """Sets the fail_fast of this V1alpha1DAGTemplate.


        :param fail_fast: The fail_fast of this V1alpha1DAGTemplate.  # noqa: E501
        :type: bool
        """

        self._fail_fast = fail_fast

    @property
    def target(self):
        """Gets the target of this V1alpha1DAGTemplate.  # noqa: E501


        :return: The target of this V1alpha1DAGTemplate.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this V1alpha1DAGTemplate.


        :param target: The target of this V1alpha1DAGTemplate.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def tasks(self):
        """Gets the tasks of this V1alpha1DAGTemplate.  # noqa: E501


        :return: The tasks of this V1alpha1DAGTemplate.  # noqa: E501
        :rtype: list[V1alpha1DAGTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this V1alpha1DAGTemplate.


        :param tasks: The tasks of this V1alpha1DAGTemplate.  # noqa: E501
        :type: list[V1alpha1DAGTask]
        """

        self._tasks = tasks

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
        if issubclass(V1alpha1DAGTemplate, dict):
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
        if not isinstance(other, V1alpha1DAGTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
