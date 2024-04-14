#!/usr/bin/env python3
from omegaconf import OmegaConf

import aws_cdk as cdk

from cost_reports.stack import CostReportsStack


app = cdk.App()

conf = OmegaConf.load("config.yaml")

CostReportsStack(
    app,
    "CostReportsStack",
    env=cdk.Environment(region=conf.aws.region, account=conf.aws.account_id),
    conf=conf,
)

app.synth()
