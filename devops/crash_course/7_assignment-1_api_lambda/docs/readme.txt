-- ASSIGNMENT 1: CALLING API GATEWAY TO TRIGGER LAMBDA FUNCTION USING CI/CD --
    NOTE: After hitting my head with CFN, I decided to use SAM for this assignment.

    - Custom Policy: Create CF stack:
'''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1449904348000",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:CreateChangeSet",
                "cloudformation:ListStacks",
                "cloudformation:UpdateStack",
                "cloudformation:DescribeChangeSet",
                "cloudformation:ExecuteChangeSet"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
'''
    - Custom Policy: Create IAM role:
'''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "iam:CreateInstanceProfile",
                "iam:RemoveRoleFromInstanceProfile",
                "iam:AddRoleToInstanceProfile",
                "iam:PassRole",
                "iam:DeleteInstanceProfile"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
'''

    - Buildspec:
        - Package the template.
'''
build:
    commands:
        - aws cloudformation package --template-file template.yaml --s3-bucket faraz-raw-bucket --output-template-file out-template.yaml
'''
    - Consider a simple lambda function.
    - Create an API Gateway and Lambda that when hit, returns the message "Hello {name}, welcome to {applicationTitle}."
     where name is a parameter passed to this API. applicationTitle should be picked from lambda environment variable.
    - Implement the CI/CD process for this function using AWS services. Any environment variables should be set from CloudFormation.
    - Show the success and failure CICD scenarios. 
    - Document the services used, the steps performed and the results.
