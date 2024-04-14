import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cost_reports.aws_cost_reports_stack import AwsCostReportsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cost_reports/aws_cost_reports_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCostReportsStack(app, "aws-cost-reports")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
