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


class V1alpha1WorkflowTemplateUpdateRequest(object):
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
        'name': 'str',
        'namespace': 'str',
        'template': 'V1alpha1WorkflowTemplate'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'template': 'template'
    }

    def __init__(self, name=None, namespace=None, template=None):  # noqa: E501
        """V1alpha1WorkflowTemplateUpdateRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._namespace = None
        self._template = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if template is not None:
            self.template = template

    @property
    def name(self):
        """Gets the name of this V1alpha1WorkflowTemplateUpdateRequest.  # noqa: E501


        :return: The name of this V1alpha1WorkflowTemplateUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1WorkflowTemplateUpdateRequest.


        :param name: The name of this V1alpha1WorkflowTemplateUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1WorkflowTemplateUpdateRequest.  # noqa: E501


        :return: The namespace of this V1alpha1WorkflowTemplateUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1WorkflowTemplateUpdateRequest.


        :param namespace: The namespace of this V1alpha1WorkflowTemplateUpdateRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def template(self):
        """Gets the template of this V1alpha1WorkflowTemplateUpdateRequest.  # noqa: E501


        :return: The template of this V1alpha1WorkflowTemplateUpdateRequest.  # noqa: E501
        :rtype: V1alpha1WorkflowTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1alpha1WorkflowTemplateUpdateRequest.


        :param template: The template of this V1alpha1WorkflowTemplateUpdateRequest.  # noqa: E501
        :type: V1alpha1WorkflowTemplate
        """

        self._template = template

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
        if issubclass(V1alpha1WorkflowTemplateUpdateRequest, dict):
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
        if not isinstance(other, V1alpha1WorkflowTemplateUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
