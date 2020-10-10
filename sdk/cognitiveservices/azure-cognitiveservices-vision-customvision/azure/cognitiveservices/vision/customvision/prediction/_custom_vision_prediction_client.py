# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import CustomVisionPredictionClientConfiguration
from .operations import CustomVisionPredictionClientOperationsMixin
from . import models


class CustomVisionPredictionClient(CustomVisionPredictionClientOperationsMixin, SDKClient):
    """CustomVisionPredictionClient

    :ivar config: Configuration for client.
    :vartype config: CustomVisionPredictionClientConfiguration

    :param endpoint: Supported Cognitive Services endpoints.
    :type endpoint: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, endpoint, credentials):

        self.config = CustomVisionPredictionClientConfiguration(endpoint, credentials)
        super(CustomVisionPredictionClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '3.1'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
