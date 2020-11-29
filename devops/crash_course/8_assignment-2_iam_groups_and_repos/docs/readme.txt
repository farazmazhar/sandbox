-- ASSIGNMENT 2 - CREATING IAM GROUPS AND CODECOMMIT REPOS USING CLOUDFORMATION --
    - Restricting at branch level in CodeCommit using CloudFormation:
        a. https://aws.amazon.com/blogs/devops/refining-access-to-branches-in-aws-codecommit/
'''
    Condition:
        StringEqualsIfExists:
            - codecommit:References
            - refs/heads/master
'''