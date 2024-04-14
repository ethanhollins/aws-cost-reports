from typing import Any
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct


class CostReportsStack(Stack):

    def __init__(
        self, scope: Construct, construct_id: str, conf: Any, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # TODO Create Generate Reports Lambda
        # TODO Create Email SNS
        # TODO Create Step Function for report generation and emailing
        # TODO Create monthly scheduled Event Bridge
        # TODO (?) Create Run command for manual
        # TODO (?) Cloud Watch Alarms
